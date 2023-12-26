# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.md for details.

import functools
from copy import deepcopy
from OPi.constants import BOARD, BCM, SUNXI, CUSTOM


class _sunXi(object):

    def __getitem__(self, value):

        offset = ord(value[1]) - 65
        pin = int(value[2:])

        assert value[0] == "P"
        assert 0 <= offset <= 25
        assert 0 <= pin <= 31

        return (offset * 32) + pin


def get_gpio_map():
    import subprocess
    result = subprocess.run(['gpio', 'readall'], stdout=subprocess.PIPE)
    lines = result.stdout.decode().split('\n')
    map = {}
    for line in lines:
        if not line or '+' in line:
            continue
        args = [x.strip() for x in line.split('|')]
        if args[1].isdigit():
            physical = int(args[1])
            gpio = int(args[6])
            map[gpio] = physical
        if args[-2].isdigit():
            physical = int(args[-2])
            gpio = int(args[-7])
            map[gpio] = physical
    return map


physical_to_gpio = get_gpio_map()

# RPi BCM to Physical
# For compatibility with zerogpio
bcm_to_physical = {
    2:  3,
    3:  5,
    4:  7,
    14: 8,
    15: 10,
    17: 11,
    18: 12,
    27: 13,
    22: 15,
    23: 16,
    24: 18,
    10: 19,
    9:  21,
    25: 22,
    11: 23,
    8:  24,
    7:  26,
    0:  27,
    1:  28,
    5:  29,
    6:  31,
    12: 32,
    13: 33,
    19: 35,
    16: 36,
    26: 37,
    20: 38,
    21: 40,
}

bcm_to_gpio = {k: physical_to_gpio[v] for k, v in bcm_to_physical.items() if v in physical_to_gpio}


_pin_map = {
    # Physical pin to actual GPIO pin
    #BOARD: {
    #    3: 12,
    #    5: 11,
    #    7: 6,
    #    8: 198,
    #    10: 199,
    #    11: 1,
    #    12: 7,
    #    13: 0,
    #    15: 3,
    #    16: 19,
    #    18: 18,
    #    19: 15,
    #    21: 16,
    #    22: 2,
    #    23: 14,
    #    24: 13,
    #    26: 10
    #},
    BOARD: physical_to_gpio,

    # BCM pin to actual GPIO pin
    # BCM: {
    #     2: 12,
    #     3: 11,
    #     4: 6,
    #     7: 10,
    #     8: 13,
    #     9: 16,
    #     10: 15,
    #     11: 14,
    #     14: 198,
    #     15: 199,
    #     17: 1,
    #     18: 7,
    #     22: 3,
    #     23: 19,
    #     24: 18,
    #     25: 2,
    #     27: 0
    # },
    BCM: bcm_to_gpio, 

    SUNXI: _sunXi(),

    # User defined, initialized as empty
    CUSTOM: {}
}


def set_custom_pin_mappings(mappings):
    _pin_map[CUSTOM] = deepcopy(mappings)


def get_gpio_pin(mode, channel):
    assert mode in [BOARD, BCM, SUNXI, CUSTOM]
    return _pin_map[mode][channel]


bcm = functools.partial(get_gpio_pin, BCM)
board = functools.partial(get_gpio_pin, BOARD)
sunxi = functools.partial(get_gpio_pin, SUNXI)
custom = functools.partial(get_gpio_pin, CUSTOM)
