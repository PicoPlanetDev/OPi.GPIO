# OPi.GPIO EX

![](https://img.shields.io/pypi/pyversions/OPi.GPIO-ex.svg)
![](https://img.shields.io/pypi/v/OPi.GPIO-ex.svg)
![](https://img.shields.io/maintenance/yes/2024.svg)

**An experimental fork that use `gpio readall` for mapping instead of map manually.**

A drop-in replacement library for [RPi.GPIO](https://sourceforge.net/projects/raspberry-gpio-python) for the Orange Pi Zero and other SBCs.
Only the basic GPIO functions are **replicated**, using sysfs: this allows the GPIO pins to be accessed from user space.

See the [documentation](https://opi-gpio.readthedocs.io) for install instructions and detailed API usage.
*Note: this documentation is not specific to this fork.*

## Installation

In the virtual environment that you are using for your project, run:

`pip3 install OPi.GPIO-ex`

OPi.GPIO is now accessible like this:
```python
import OPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
# or GPIO.setmode(GPIO.BCM)

# setup inputs, outputs, event detection etc as per the documentation linked above
```

## Notes

### Non-Root Access

OPi.GPIO generally needs root access, but this might be inconvenient in some cases. The official documentation has
[instructions](https://opi-gpio.readthedocs.io/en/latest/install.html#non-root-access) for non-root access, but this
solution did not work correctly for me, so your mileage may vary here.

Running a Python script with `sudo` does not work correctly when a virtual environment is activated. However,
you can run `sudo venv/bin/python3 myscript.py` which will work correctly. This is my (probably not best-practices)
solution for the time being. It does not, however, allow you to run it without root entirely.

### Testing

Only tested with my Orange Pi Zero 2W and a e-Paper module (see [Waveshare_e-Paper](https://github.com/zetaloop/Waveshare_e-Paper), not finished yet)

## Changelog

| Version   | Description                                              | Date       |
| --------- | -------------------------------------------------------- | ---------- |
| **0.5.5** | Add OrangePi Zero 2W pin mappings                        | 2023/12/26 |
| **0.5.4** | Add OrangePi Zero3 pin mappings                          | 2023/08/06 |
| **0.5.3** | Add Radxa Zero pin mappings                              |            |
|           | Add OrangePi Zero2 pin mappings                          | 2022/06/20 |
| **0.5.2** | Add full 40-pin header for Orange Pi 4(B)                | 2021/10/22 |
| **0.5.1** | Updated Orange Pi 4B mappings                            | 2021/08/19 |
| **0.5.0** | Add Hardware PWM Control                                 |            |
|           | Add support for the NanoPi M4 family                     |            |
|           | Add OrangePi 4 & 4B pin mappings                         |            |
|           | Add rockpi/rockpi s packages added                       |            |
|           | Fix OrangePi PC BCM Pin map                              | 2021/04/25 |
| **0.4.0** | Add various new pin mappings for Orange Pi variants      | 2019/10/21 |
| **0.3.6** | Expose pullup resistor constants to API users            |            |
|           | Add OrangePi Prime pin mappings                          | 2019/01/14 |
| **0.3.5** | Add OrangePi Lite & One pin mappings                     | 2018/11/10 |
| **0.3.4** | Add more OrangePi and NanoPi pin mappings                | 2018/09/16 |
| **0.3.3** | Add waits for UDEV rules                                 | 2018/09/15 |
| **0.3.2** | Add OrangePi PC pin mappings                             | 2018/03/04 |
| **0.3.1** | Add NanoPi DUO pin mappings                              | 2018/01/01 |
| **0.3.0** | Add alternate pin mappings                               | 2017/12/31 |
| **0.2.5** | sysfs: set output() value to 0 or 1                      | 2017/07/15 |
| **0.2.4** | Add compatibility for pull up/down and bouncetime params | 2017/05/27 |
| **0.2.3** | Make worker threads daemonic (can't exit otherwise)      | 2017/05/26 |
| **0.2.2** | ``GPIO.setup()`` catches IOError and re-exports          | 2017/03/28 |
| **0.2.1** | Minor bug fixes                                          |            |
|           | Additional tests                                         | 2017/03/14 |
| **0.2.0** | Add edge detection and eventing                          | 2017/03/14 |
| **0.1.0** | Initial version                                          | 2017/03/11 |
