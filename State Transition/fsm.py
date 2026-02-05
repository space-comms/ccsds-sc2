from dataclasses import dataclass
from enum import Enum



# State Table 5-1 (DUPLEX Independent)
STATES_TABLE_5_1 = {
    "S1": ProtocolState("Inactive", "off", "off", "inactive", "off", 0),
    "S2": ProtocolState("Waiting for Hail", "on", "off", "connecting-L", "off", 0),
    "S80": ProtocolState("Reconnect", "on", "off", "active", "off", 0),
}

# State Table 5-2 (DUPLEX=Full)
STATES_TABLE_5_2 = {
    "S31": ProtocolState("Start Hail Action", "on", "async", "connecting-T", "on", 1),
    "S32": ProtocolState("Send Hail Acquisition", "on", "async", "connecting-T", "on", 2),
    "S33": ProtocolState("Send Hail Directives", "on", "async", "connecting-T", "on", 3),
    "S34": ProtocolState("Send Hail Tail", "on", "async", "connecting-T", "on", 4),
    "S35": ProtocolState("Wait for Hail Response", "on", "async", "connecting-T", "on", 5),
    "S41": ProtocolState("Radiate Carrier Only", "on","sync", "active", "on", 1),
    "S42": ProtocolState("Radiate Acqusition Idle", "on", "sync", "active", "on", 2),
    "S40": ProtocolState("Data services", "on", "sync", "active", "on", 0),
    "S48": ProtocolState("Comm_Change", "on", "sync", "active", "on", 6),
    "S45": ProtocolState("Terminating Tail", "on", "sync", "active", "on", 4),
}

# State Table 5-3 (DUPLEX=Half)
STATES_TABLE_5_3 = {
    "S11"
}

# State Transition Session Establishment Table 5-6 (DUPLEX=Full)
# State Transition Comm Change Table 5-7 (DUPLEX=Full)
# State Transition Session Termination Table 5-8 (DUPLEX=Full)


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

class Table56Event(Enum):
    E1_MODE_CONNECTING_L = "E1: Local Directive connecting-L"
    E2_MODE_CONNECTING_T = "E2: Local Directive connecting-T"
    E3_HAIL_RCVD = "E3: HAIL Directives Received"
    E4_CARRIER_ONLY_EXP = "E4: WT=1 Carrier_Only_Duration"
    E5_ACQ_IDLE_EXP = "E5: WT=1 Acquisition_Idle_Duration"
    E6_FIFO_EMPTY = "E6: Output FIFO=empty"
    E7_TAIL_IDLE_EXP = "E7: WT=1 Tail_Idle_Duration"
    E8_HAIL_WAIT_EXP = "E8: WT=1 Hail_Wait_Duration"
    E9_VALID_FRAME = "E9: Valid Transfer Frame Received"
    E10_CARRIER_ONLY_EXP_S41 = "E10: WT=1 Carrier_Only (S41→S42)"
    E11_ACQ_IDLE_EXP_S42 = "E11: WT=1 Acquisition_Idle (S42→S40)"
    E80_CALLER_CARRIER_LOSS = "E80: Caller CARRIER_LOSS_TIMER"
    E81_RECONNECT_WAIT_EXP = "E81: WT=1 Reconnect_Wait_Duration"
    E82_RESPONDER_CARRIER_LOSS = "E82: Responder CARRIER_LOSS_TIMER"

class FullDuplexFSM:
    def __init__(self, duplex: DuplexMode = DuplexMode.FULL):
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