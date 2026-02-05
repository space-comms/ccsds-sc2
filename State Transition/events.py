# Session Control Variable Initialization Table

# Variables - Value
# TRANSMIT, MODULATION, PERSISTENCE = off, off, false
# SS, X, Y, Z = 0
# WAIT TIMER (WT), CARRIER_LOSS_TIMER, PLCW_TIMER = 0
# SEQUENCE CONTROLLED (SEQ_CTRL_FSN) = 0
# EXPEDITED FRAME SEQUENCE COUNTERS (EXP_FSN) = 0

from typing import Dict, Callable, Tuple
from enum import Enum

class Event(Enum):
    E1 = "E1"
    E2 = "E2"
    E3 = "E3"
    E4 = "E4"
    E5 = "E5"
    E6 = "E6"
    E7 = "E7"
    E8 = "E8"
    E9 = "E9"
    E10 = "E10"
    E11 = "E11"
    E80 = "E80"
    E81 = "E81"
    E82 = "E82"

# Action functions

def e2_actions(vars):
    vars.WT = vars.carrier_only_duration
    vars.PERSISTENCE = True

def e3_actions(vars):
