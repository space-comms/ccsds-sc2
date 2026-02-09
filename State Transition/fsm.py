from dataclasses import dataclass
from enum import Enum
from state_control_vars import StateControlVars
from operational_control_vars import OperationalControlVars
from states import ProtocolState, DUPLEX_FULL_STATES, DUPLEX_INDEPENDENT_STATES

class SessionFSM:
    def __init__(self, duplex_mode = "full"):
        self.state_dict = DUPLEX_FULL_STATES
        self.state = DUPLEX_INDEPENDENT_STATES["S1"]
        self.current_state_key = current_state_key
    def transition_to(self, new_key):
        if new_key in self.state_dict:
            self.current_state_key = new_key
            self.state = self.state_dict[new_key]

fsm = SessionFSM()
fsm.transition_to("S40")
print(fsm.state)