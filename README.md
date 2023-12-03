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
# Changelog

| Version   | Description                                                    | Date       |
|-----------|----------------------------------------------------------------|------------|
| **0.5.4** | Add OrangePi Zero3 pin mappings                                | 2023/08/06 |
| **0.5.3** | Add Radxa Zero pin mappings                                    | 2022/06/20 |
|           | Add OrangePi Zero2 pin mappings                                |            |
| **0.5.2** | Add full 40-pin header for Orange Pi 4(B)                      | 2021/10/22 |
| **0.5.1** | Updated Orange Pi 4B mappings                                  | 2021/08/19 |
| **0.5.0** | Add Hardware PWM Control                                       | 2021/04/25 |
|           | Add support for the NanoPi M4 family                           |            |
|           | Add OrangePi 4 & 4B pin mappings                               |            |
|           | Add rockpi/rockpi s packages added                             |            |
|           | Fix OrangePi PC BCM Pin map                                    |            |
| **0.4.0** | Add various new pin mappings for Orange Pi variants            | 2019/10/21 |
| **0.3.6** | Expose pullup resistor constants to API users                  | 2019/01/14 |
|           | Add OrangePi Prime pin mappings                                |            |
| **0.3.5** | Add OrangePi Lite & One pin mappings                           | 2018/11/10 |
| **0.3.4** | Add more OrangePi and NanoPi pin mappings                      | 2018/09/16 |
| **0.3.3** | Add waits for UDEV rules                                       | 2018/09/15 |
| **0.3.2** | Add OrangePi PC pin mappings                                   | 2018/03/04 |
| **0.3.1** | Add NanoPi DUO pin mappings                                    | 2018/01/01 |
| **0.3.0** | Add alternate pin mappings                                     | 2017/12/31 |
| **0.2.5** | sysfs: set output() value to 0 or 1                            | 2017/07/15 |
| **0.2.4** | Add compatibility for pull up/down and bouncetime params       | 2017/05/27 |
| **0.2.3** | Make worker threads daemonic (can't exit otherwise)            | 2017/05/26 |
| **0.2.2** | ``GPIO.setup()`` catches IOError and re-exports                | 2017/03/28 |
| **0.2.1** | Minor bug fixes                                                | 2017/03/14 |
|           | Additional tests                                               |            |
| **0.2.0** | Add edge detection and eventing                                | 2017/03/14 |
| **0.1.0** | Initial version                                                | 2017/03/11 |
