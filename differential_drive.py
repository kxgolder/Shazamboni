import math

# http://savagemakers.com/joystick-differential-drive-python/
def joystickToDiff(angle, distance, minJoystick, maxJoystick, minSpeed, maxSpeed):
    # If x and y are 0, then there is not much to calculate...
    angle = (angle + 90) % 360
    # http://squircular.blogspot.com/2015/09/mapping-circle-to-square.html

    u = round(distance * math.cos((angle * math.pi) / 180), 4)
    v = round(distance * math.sin(angle * math.pi / 180), 4)
    u2 = u * u
    v2 = v * v
    twosqrt2 = 2.0 * math.sqrt(2.0);
    subtermx = 2.0 + u2 - v2;
    subtermy = 2.0 - u2 + v2;
    termx1 = subtermx + u * twosqrt2;
    termx2 = subtermx - u * twosqrt2;
    termy1 = subtermy + v * twosqrt2;
    termy2 = subtermy - v * twosqrt2;
    try:
        sqx = math.sqrt(termx1)
        sqy = math.sqrt(termx2)
    except:
        return None, None
    x = 0.5 * sqx - 0.5 * sqy;
    # print(x)
    y = 0.5 * math.sqrt(termy1) - 0.5 * math.sqrt(termy2);
    # print(y)
    # x = (0.5 * math.sqrt(2 + (2 * math.sqrt(2) * u) + math.pow(u, 2) - math.pow(v, 2))) - (0.5 * math.sqrt(
        # 2 - (2 * math.sqrt(2) * u) + math.pow(u, 2) - math.pow(v, 2)))
    # y = (0.5 * math.sqrt(2 + (2 * math.sqrt(2) * v) + math.pow(u, 2) - math.pow(v, 2))) - (0.5 * math.sqrt(
    #     2 - (2 * math.sqrt(2) * v) + math.pow(u, 2) - math.pow(v, 2)))
    if x == 0 and y == 0:
        return 0, 0

    # First Compute the angle in deg
    # First hypotenuse
    z = math.sqrt(x * x + y * y)

    # angle in radians
    rad = math.acos(math.fabs(x) / z)

    # and in degrees
    angle = rad * 180 / math.pi

    # Now angle indicates the measure of turn
    # Along a straight line, with an angle o, the turn co-efficient is same
    # this applies for angles between 0-90, with angle 0 the coeff is -1
    # with angle 45, the co-efficient is 0 and with angle 90, it is 1

    tcoeff = -1 + (angle / 90) * 2
    turn = tcoeff * math.fabs(math.fabs(y) - math.fabs(x))
    turn = round(turn * 100, 0) / 100

    # And max of y or x is the movement
    mov = max(math.fabs(y), math.fabs(x))

    # First and third quadrant
    if (x >= 0 and y >= 0) or (x < 0 and y < 0):
        rawLeft = mov
        rawRight = turn
    else:
        rawRight = mov
        rawLeft = turn

    # Reverse polarity
    if y < 0:
        rawLeft = 0 - rawLeft
        rawRight = 0 - rawRight

    # minJoystick, maxJoystick, minSpeed, maxSpeed
    # Map the values onto the defined rang
    rightOut = map(rawRight, minJoystick, maxJoystick, minSpeed, maxSpeed)
    leftOut = map(rawLeft, minJoystick, maxJoystick, minSpeed, maxSpeed)

    return (rightOut, leftOut)


def map(v, in_min, in_max, out_min, out_max):
    # Check that the value is at least in_min
    if v < in_min:
        v = in_min
    # Check that the value is at most in_max
    if v > in_max:
        v = in_max
    return (v - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
