#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
#GPIO_TRIGGER = 18
#GPIO_ECHO = 24
#GPIO_TRIGGER_2 = 22 # Pin 19 for Pi4 
#GPIO_ECHO_2 = 23

#set GPIO direction (IN / OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.IN)
  
def distance(GPIO_TRIGGER, GPIO_ECHO):
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    #GPIO.output(GPIO_TRIGGER_2, True)
        
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    #GPIO.output(GPIO_TRIGGER_2, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    #StartTime_2 = time.time()
    #StopTime_2 = time.time()  
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        
    #while GPIO.input(GPIO_ECHO_2) == 0:
        #StartTime_2 = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        
    #while GPIO.input(GPIO_ECHO_2) == 1:
        #StopTime_2 = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    #TimeElapsed2 = StopTime_2 - StartTime_2
    
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    
    distance = (TimeElapsed * 34300) / 2
    #distance2 = (TimeElapsed2 * 34300) / 2
    
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist  = distance(18, 24)
            dist2 = distance(22, 23)
            
            print ("Measured Distance = %.1f cm" % dist)
            print ("Measured Distance 2 = %.1f cm" % dist2)
            
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()