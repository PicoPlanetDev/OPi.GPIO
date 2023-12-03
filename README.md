# OPi.GPIO

**My attempt at maintaining OPi.GPIO for at least the Orange Pi Zero 3**

A drop-in replacement library for RPi.GPIO for the Orange Pi Zero and other SBCs.
Only the basic GPIO functions are replicated, using sysfs: this allows the GPIO pins to be accessed from user space.

See the [documentation](https://opi-gpio.readthedocs.io) for install instructions and detailed API usage.
*Note: this documentation is not specific to this fork.*

## Installation

In the virtual environment that you are using for your project, run:
`pip install OPi.GPIO-PicoPlanetDev==0.5.4`

OPi.GPIO is now accessible like so:
```python
import OPi.GPIO as GPIO
import orangepi.zero3

GPIO.setmode(orangepi.zero3.BOARD)

# setup inputs, outputs, event detection etc as per the documentation linked above
```

## Version

0.5.4 - Added Orange Pi Zero 3 pin mappings 2023/08/06