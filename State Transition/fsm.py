from dataclasses import dataclass
from enum import Enum
from state_control_vars import StateControlVars
from operational_control_vars import OperationalControlVars

class S1(Enum):
    # Set initialize mode
    TRANSMIT = "off"
    MODULATION = "off"
    PERSISTENCE: bool = False
    SS: int = 0
    X: int = 0
    Y: int = 0
    Z: int = 0
    WT: int = 0
    CARRIER_LOSS_TIMER: int = 0
    PLCW_TIMER: int = 0
    SEQ_CTRL_FSN: int = 0
    EXP_FSN: int = 0

class FullDuplexFSM:
    def __init__(self):
        self.state_vars = StateControlVars()
        self.op_vars = OperationalControlVars()
        self.vars.reset_for_session_start()

        self.duplex = duplex
        self.current_state_key = "S1"
        self.states = {**STATES_TABLE_5_1, **STATES_TABLE_5_2}
        self.vars = SessionControlVars()

    def event_
    @property
    def state(self) -> ProtocolState:
        return self.states[self.current_state_key]

    def transition_to(selfself, state_key: str):
        if state_key not in self.states:
            raise ValueError(f"Invalid state: {state_key}")
        self.current_state_key = state_key
        print(f"{self.state}")

    def check_conditions(self) -> bool:
        s = self.state
        return (self.vars.TX == s.T and sel)