# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola, Ruud Schramp
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x70).
# Page 7 of PCA9685 docs
pwm = Adafruit_PCA9685.PCA9685(0x70)

#The Adafruit Motor Shield v2.3 has 4 pins as generic PWM:

GEN1=15
GEN2=14
GEN3=1
GEN4=0

#The rest is coupled to two TB6612FNG, a dual DC motor driver.
#It allows thus for 4 motors.

AIN1 = 10
AIN2 = 9
PWMA = 8

BIN1 = 11
BIN2 = 12
PWMB = 13

#using C and D for second chip:

CIN1 = 4
CIN2 = 3
PWMC = 2

DIN1 = 5
DIN2 = 6
PWMD = 7

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)


# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#>>> for A in range(0,15):
#...     pwm.set_pwm(A,0,4095)
#...     print A
#...     time.sleep(1)




print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)
