"""
Motor Settings
"""

# Left Motor Pins
L_IN_1 = 20
L_IN_2 = 21
L_EN = 12

# Right Motor Pins
R_IN_1 = 26
R_IN_2 = 19
R_EN = 13

# PWM Frequency
PWM_FREQ = 100

"""
Differential Driving Settings
"""
# Joystick Parameters and Speed Definitions
MAX_JOYSTICK = 1
MIN_JOYSTICK = -1
MAX_SPEED = 1
MIN_SPEED = -1


"""
Ultrasonic Sensor Settings
"""
# Distance Threshold (m)
US_THRESHOLD = 0.2
US_ADDITIONAL_DISTANCE = 10
US_LATENCY = 300

# GPIO Pins for Ultrasonic Sensors
# Front Ultrasonic Sensor
F_GPIO_TRIGGER = 18
F_GPIO_ECHO = 24

# Back Ultrasonic Sensor
B_GPIO_TRIGGER = 22
B_GPIO_ECHO = 23
