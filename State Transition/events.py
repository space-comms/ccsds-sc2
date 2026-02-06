# Session Control Variable Initialization Table

# Session Control Variables - Value
# TRANSMIT, MODULATION, PERSISTENCE = off, off, false
# SS, X, Y, Z = 0
# WAIT TIMER (WT), CARRIER_LOSS_TIMER, PLCW_TIMER = 0
# SEQUENCE CONTROLLED (SEQ_CTRL_FSN) = 0
# EXPEDITED FRAME SEQUENCE COUNTERS (EXP_FSN) = 0

# State Control Variables
# MODE (inactive, connecting-T, connecting-L, active)
# DUPLEX (full, half, simplex transmit, simplex receive)
# TRANSMIT (off, on)
# SUB-STATE

from state_control_vars import StateControlVars
from operational_control_vars import OperationalControlVars

from typing import Dict, Callable, Tuple
from enum import Enum

@dataclass
class Event:
    event_no: str
    description: str
    from_state: Optional[str] = None
    from_states: Optional[List[str]] = None
    to_state: str
    actions: List[str]

# Full Duplex Session Establishment and Data Services


# Full Duplex Communication Change State
# Full Duplex Session Termination State


# Half Duplex Session Establishment and Data Services
# Half Duplex Communication Change State
# Half Duplex Session Termination State

# Simplex State Transition