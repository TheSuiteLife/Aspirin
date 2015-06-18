"""
Typical game settings
"""

import os
import math
from collections import OrderedDict

HEADER = 'header'

PROPERTIES_FILE = os.path.join(os.path.dirname(__file__), 'game_settings.ini')

DEFAULT_CONTROLS = (
    (HEADER     ,   'Controls'),
    ('UP'    ,   'w'),
    ('DOWN'  ,   's'),
    ('LEFT'  ,   'a'),
    ('RIGHT' ,   'd'),
    ('FOCUS' ,   'space')
)

DEFAULT_CHARACTER = (
    (HEADER     ,   'Character'),
    ('SPEED'    ,   0.400),
    ('FOCUS'    ,   0.234)
)

DEFAULT_MISSILE = (
    (HEADER             ,   'Missile'),
    ('SPEED LOWER'      ,   10),
    ('SPEED UPPER'      ,   30),
    ('SPEED MULTIPLIER' ,   0.0234375)
)

DEFAULT_HOMING_MISSILE = (
    (HEADER             ,   'Homing Missile',),
    ('SPEED LOWER'      ,   5),
    ('SPEED UPPER'      ,   10),
    ('ANGLE LOWER'      ,   math.radians(75)),
    ('ANGLE UPPER'      ,   math.radians(150)),
    ('SPEED MULTIPLIER' ,   0.0176)
)

DEFAULT_CONTROLS        =   OrderedDict(DEFAULT_CONTROLS)
DEFAULT_CHARACTER       =   OrderedDict(DEFAULT_CHARACTER)
DEFAULT_MISSILE         =   OrderedDict(DEFAULT_MISSILE)
DEFAULT_HOMING_MISSILE  =   OrderedDict(DEFAULT_HOMING_MISSILE)