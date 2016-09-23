# Adafruit Python PCA9685
Python code to use the PCA9685 PWM servo/LED controller with a Raspberry Pi or BeagleBone black.

## Installation

To install the library from source (recommended) run the following commands on a Raspberry Pi or other Debian-based OS system:

    sudo apt-get install git build-essential python-dev
    cd ~
    git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
    cd Adafruit_Python_PCA9685
    sudo python setup.py install

Alternatively you can install from pip with:

    sudo pip install adafruit-pca9685

Note that the pip install method **won't** install the example code.

## Usage

For a servo, for example::

	import time
	import Adafruit_PCA9685

	# Initialise the PCA9685 using the default address (0x40).
	pwm = Adafruit_PCA9685.PCA9685()
	
	# Alternatively specify a different address and/or bus:
	#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

	# Set frequency to 60hz, good for servos.
	pwm.set_pwm_freq(60)
	
	# Configure min and max servo pulse lengths
	servo_min = 150  # Min pulse length out of 4096 <=> 3.66% duty cycle
	servo_max = 600  # Max pulse length out of 4096 <=> 14.5% duty cycle

	print('Moving servo on channel 0, press Ctrl-C to quit...')
	while True:
	    # Move servo on channel O between extremes.
	    pwm.set_pwm(0, 0, servo_min)
	    time.sleep(1)
	    pwm.set_pwm(0, 0, servo_max)
	    time.sleep(1)
	