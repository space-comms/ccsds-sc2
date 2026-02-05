# Operational Control Variables
# X (0,1,2,3,4,5) Session Termination
# Y (0,1,2,3,4,5) COMM change
# Z (0,1) Symbol inlock status

# MODULATION

from enum import IntEnum
from dataclasses import dataclass, field
from typing import Optional, Dict, List

# X (Session Termination)
class XSessionTermination(IntEnum):
    BIDIRECTIONAL = 0             # Bi-directional data passing
    LMND_LOCAL = 1                # Local No More Data (half-duplex)
    SENDING_RNMD = 2              # Sending Remote No More Data
    GOT_RNMD_HAVE_DATA = 3        # Got RNMD, have local data (half-duplex)
    GOT_RNMD_WAIT_LOCAL_EMPTY = 4 # Got RNMD, waiting local empty
    BOTH_EMPTY = 5                # Both no more data, terminate

# Y (Comm Change)
class YCommChange(IntEnum):
    NO_CHANGE = 0 # No Comm_Change in progress
    LOCAL_INIT = 1 # Local directive received
    SENDING_DIRECTIVE = 2 # Sending Comm_change directive
    WAIT_ACK = 3 # Waiting acknowledgement
    RECEIVE_RCCD = 4 # Receive Remote Comm_change (full-duplex)
    ACT_ON_RNMD = 5 # Act on received RCCD (full-duplex)

# Z (Symbol Inlock Status)
class ZSymbolInLock(IntEnum):
    NOT_FAILED = 0 # SYMBOL_INLOCK_STATUS true
    FAILED = 1 # SYMBOL_INLOCK_STATUS false

@dataclass
class OperationalControlVars:
    X: XSessionTermination = XSessionTermination.BIDIRECTIONAL
    Y: YCommChange = YCommChange.NO_CHANGE
    Z: ZSymbolInLock = ZSymbolInLock.NOT_FAILED
    MODULATION: str = "off"
    PERSISTENCE: bool = False
    NEED_PLCW: bool = False
    NEED_STATUS_REPORT: bool = False
    REMOTE_SCID_BUFFER: Optional[int] = None
    COMMUNICATION_VALUE_BUFFER: Dict[str, List[str]] = field(default_factory=dict)
    RECEIVING_SCID_BUFFER: Optional[int] = None
    RECEIVING_PCID_BUFFER: Optional[int] = None

    def reset_for_session_start(self):
        self.X = XSessionTermination.BIDIRECTIONAL
        self.Y = YCommChange.NO_CHANGE
        self.Z = ZSymbolInLock.NOT_FAILED
        self.MODULATION = "off"
        self.PERSISTENCE = False
        self.NEED_PLCW = True
        self.NEED_STATUS_REPORT = True