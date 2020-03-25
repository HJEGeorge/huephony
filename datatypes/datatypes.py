from enum import Enum


class Brightness(Enum):
    """0-254"""
    OFF = 0
    VERY_DIM = 0.2 * 254
    DIM = 0.4 * 254
    NORMAL = 0.6 * 254
    BRIGHT = 0.8 * 254
    VERY_BRIGHT = 254


class Hue(Enum):
    """0-65535"""
    RED = 0
    GREEN = 25500
    BLUE = 46920


class ColorTemp(Enum):
    """Colour temperature measured in mireds [154-500]"""
    COOLEST = 154
    COOL = 154 + 0.25 * (500 - 154)
    NEUTRAL = 154 + 0.5 * (500 - 154)
    WARM = 154 + 0.75 * (500 - 154)
    WARMEST = 500