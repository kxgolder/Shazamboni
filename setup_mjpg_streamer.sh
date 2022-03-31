#!/bin/bash
PWD=$HOME
cd PWD
git clone https://github.com/ArduCAM/mjpg-streamer.git
git clone https://git.libcamera.org/libcamera/libcamera.git
apt install -y g++ gcc cmake python3-yaml python3-ply python3-jinja2 libgnutls28-dev openssl libdw-dev libunwind-dev libboost-dev python3-pip libjpeg62-turbo-dev:armhf libjpeg62-turbo-dev
pip3 install meson
ln -s /usr/local/bin/meson /usr/bin/meson

# Compile libcamera
cd libcamera
meson build
ninja -C build install
cd PWD

# Compile mjpg-streamer
cd mjpg-streamer/mjpg-streamer-experimental
make
make install
useradd -m webcam
adduser webcam video
usermod -a -G video webcam

cd scripts/
cp mjpg-streamer.default /etc/default/mjpg-streamer
cat > mjpg-streamer <<EOF
#!/bin/bash

### BEGIN INIT INFO
# Provides:          mjpg-streamer
# Required-Start:    $local_fs networking
# Required-Stop:
# Should-Start:
# Should-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: mjpg-streamer daemon
# Description:       Starts the mjpg-streamer daemon with the user specified in
#                    /etc/default/mjpg-streamer.
### END INIT INFO

# Author: Sami Olmari & Gina Häußge

# Set to true to aid in debugging with this script fails to
# start.
debug_me=false
VERBOSE=true

if [[ "$debug_me" == "true" ]]; then
	echo "OK"
	# Close STDOUT
	exec 1<&-
	# Close STDERR
	exec 2<&-

	LOG_FILE=/home/pi/mjpg_streamer.log

	# Open STDOUT as $LOG_FILE file for read and write.
	exec 1<>$LOG_FILE

	# Redirect STDERR to STDOUT
	exec 2>&1

	# Display shell commands with expanded args
	set -x
fi

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DESC="mjpg-streamer Daemon"
NAME="mjpg-streamer"
PKGNAME=mjpg-streamer
PIDFILE=/var/run/$PKGNAME.pid
SCRIPTNAME=/etc/init.d/$PKGNAME
DEFAULTS=/etc/default/$PKGNAME

# Read configuration variable file if it is present
[ -r $DEFAULTS ] && . $DEFAULTS

# Define LSB log_* functions.
# Depend on lsb-base (>= 3.0-6) to ensure that this file is present.
. /lib/lsb/init-functions

# Exit if the DAEMON is not set
if [ -z "$DAEMON" ]
then
    log_warning_msg "Not starting $PKGNAME, DAEMON not set in $DEFAULTS."
    exit 0
fi

# Exit if the DAEMON is not installed
[ -x "$DAEMON" ] || exit 0

# Load the VERBOSE setting and other rcS variables
[ -f /etc/default/rcS ] && . /etc/default/rcS

if [ -z "$START" -o "$START" != "yes" ]
then
   log_warning_msg "Not starting $PKGNAME, edit $DEFAULTS to start it."
   exit 0
fi

if [ -z "$MJPG_STREAMER_USER" ]
then
    log_warning_msg "Not starting $PKGNAME, MJPG_STREAMER_USER not set in $DEFAULTS."
    exit 0
fi

#
# Function to verify if a pid is alive
#
is_alive()
{
   pid=`cat $1` > /dev/null 2>&1
   kill -0 $pid > /dev/null 2>&1
   return $?
}

#
# Function that starts the daemon/service
#
do_start()
{
   # Return
   #   0 if daemon has been started
   #   1 if daemon was already running
   #   2 if daemon could not be started

   is_alive $PIDFILE
   echo "Starting..."
   echo "${INPUT_UVC_LIB} ${CAMERA_OPTIONS}" -o "${OUTPUT_HTTP_LIB} -w ${WWW_ROOT}"
   /usr/local/bin/mjpg_streamer -i "${LIB_DIR}/input_libcamera.so" -o "${OUTPUT_HTTP_LIB} -w /var/local/www"
}

#
# Function that stops the daemon/service
#
do_stop()
{
   # Return
   #   0 if daemon has been stopped
   #   1 if daemon was already stopped
   #   2 if daemon could not be stopped
   #   other if a failure occurred

   start-stop-daemon --stop --quiet --retry=TERM/30/KILL/5 --user $MJPG_STREAMER_USER --pidfile $PIDFILE
   RETVAL="$?"
   [ "$RETVAL" = "2" ] && return 2

   rm -f $PIDFILE

   [ "$RETVAL" = "0"  ] && return 0 || return 1
}

case "$1" in
  start)
   [ "$VERBOSE" != no ] && log_daemon_msg "Stardting $DESC" "$NAME"
   echo "Got start"
   do_start
   case "$?" in
      0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
      2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
   esac
   ;;
  stop)
   [ "$VERBOSE" != no ] && log_daemon_msg "Stopping $DESC" "$NAME"
   do_stop
   case "$?" in
      0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
      2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
   esac
   ;;
  status)
   status_of_proc -p $PIDFILE $DAEMON $NAME && exit 0 || exit $?
   ;;
  restart)
   log_daemon_msg "Restarting $DESC" "$NAME"
   do_stop
   case "$?" in
     0|1)
      do_start
      case "$?" in
         0) log_end_msg 0 ;;
         1) log_end_msg 1 ;; # Old process is still running
         *) log_end_msg 1 ;; # Failed to start
      esac
      ;;
     *)
        # Failed to stop
      log_end_msg 1
      ;;
   esac
   ;;
  *)
   echo "Usage: $SCRIPTNAME {start|stop|status|restart}" >&2
   exit 3
   ;;
esac
EOF

mv mjpg_streamer /etc/init.d/mjpg-streamer
update-rc.d mjpg-streamer defaults
systemctl daemon-reload

cat > mjpg-streamer.service <<EOF
[Unit]
Description=A Linux-UVC streaming application with Pan/Tilt
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=pi
ExecStart=/etc/init.d/mjpg-streamer start

[Install]
WantedBy=multi-user.target
EOF

mv mjpg_streamer.service /etc/systemd/system/mjpg-streamer.service
systemctl enable mjpg-streamer.service
reboot
