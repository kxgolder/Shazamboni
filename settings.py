"""
Motor Settings
"""

# Left Motor Pins
L_IN_1 = 26
L_IN_2 = 19
L_EN = 13

# Right Motor Pins
R_IN_1 = 20
R_IN_2 = 16
R_EN = 12

# PWM Frequency
PWM_FREQ = 100

"""
Differential Driving Settings
"""
# Joystick Parameters and Speed Definitions
MAX_JOYSTICK = 1
MIN_JOYSTICK = -1
MAX_SPEED = 100
MIN_SPEED = -100


"""
Ultrasonic Sensor Settings
"""
# Distance Threshold (cm)
US_THRESHOLD = 7

# GPIO Pins for Ultrasonic Sensors
# Front Ultrasonic Sensor
F_GPIO_TRIGGER = 18
F_GPIO_ECHO = 24

# Back Ultrasonic Sensor
B_GPIO_TRIGGER = 22
B_GPIO_ECHO = 23
