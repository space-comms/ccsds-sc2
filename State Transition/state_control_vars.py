from enum import Enum
from dataclasses import dataclass
from typing import Optional

class ModeState(Enum):
    INACTIVE = "inactive"
    CONNECTING_T = "connecting-T" # Transmit + Hail
    CONNECTING_L = "connecting-L" # Listen for hail
    ACTIVE = "active" # Data services

class DuplexMode(Enum):
    FULL = "full"
    HALF = "half"
    SIMPLEX_TRANSMIT = "simplex_transmit"
    SIMPLEX_RECEIVE = "simplex_receive"

class TransmitState(Enum):
    OFF = "off"
    ON = "on"

@dataclass
class StateControlVars:

    MODE: ModeState = ModeState.INACTIVE
    DUPLEX: DuplexMode = DuplexMode.FULL
    TRANSMIT: TransmitState = TransmitState.OFF
    SS: int = None# sub-state table 5-12

    def set_mode(self, mode: ModeState):
        self.MODE = mode

    def set_duplex(self, duplex: DuplexMode):
        self.DUPLEX = duplex

    def initialize_mode(self):
        self.MODE = ModeState.INACTIVE
        self.SS = None

    def __str__(self):
        return(f"MODE={self.MODE.value} | DUPLEX={self.DUPLEX.value} | TRANSMIT={self.TRANSMIT.value} |",
               F"TX={self.TRANSMIT.value} | SS={self.SS}")