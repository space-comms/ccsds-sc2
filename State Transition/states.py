@dataclass
class ProtocolState:
    name: str # S1, S,2, S31, etc.
    receive_state_desc: str # "off", "on", "connecting-L", "active"
    send_state_desc: str # "off", "async", "sync", "connecting-T"
    MODE: str # "inactive", "connecting-L/T", "active"
    T: str # "off", "on"
    SS: int # 0,1,2,3,4,5,6

    def __str__(self):
        return f"S{self.SS if self.SS else ""}: {self.name} | MODE = {self.MODE} | T = {self.T}"

# State Table 5-1 (DUPLEX Independent)
DUPLEX_INDEPENDENT_STATES = {
    "S1": ProtocolState("Inactive", "off", "off", "inactive", "off", 0),
    "S2": ProtocolState("Waiting for Hail", "on", "off", "connecting-L", "off", 0),
    "S80": ProtocolState("Reconnect", "on", "off", "active", "off", 0),
}

# State Table 5-2 (DUPLEX=Full)
DUPLEX_FULL_STATES = {
    "S31": ProtocolState("Start Hail Action", "on", "async", "connecting-T", "on", 1),
    "S32": ProtocolState("Send Hail Acquisition", "on", "async", "connecting-T", "on", 2),
    "S33": ProtocolState("Send Hail Disrectives", "on", "async", "connecting-T", "on", 3),
    "S34": ProtocolState("Send Hail Tail", "on", "async", "connecting-T", "on", 4),
    "S35": ProtocolState("Wait for Hail Response", "on", "async", "connecting-T", "off", 5),
    "S41": ProtocolState("Radiate Carrier Only", "on","sync", "active", "on", 1),
    "S42": ProtocolState("Radiate Acquisition Idle", "on", "sync", "active", "on", 2),
    "S40": ProtocolState("Data services", "on", "sync", "active", "on", 0),
    "S48": ProtocolState("Comm_Change", "on", "sync", "active", "on", 6),
    "S45": ProtocolState("Terminating Tail", "on", "sync", "active", "on", 4),
}

# State Table 5-3 (DUPLEX=Half)
DUPLEX_HALF_STATES = {
    "S11": ProtocolState("Start Hail Action", "off", "async", "connecting-T", "on", 1),
    "S12": ProtocolState("Send Hail Acquisition", "off", "async", "connecting-T", "on", 2),
    "S13": ProtocolState("Send Hail Directives", "off", "async", "connecting-T", "on", 3),
    "S14": ProtocolState("Send Hail Tail", "off", "async", "connecting-T", "on", 4),
    "S36": ProtocolState("Wait for Hail Response", "on", "off", "connecting-T", "off", 5),
    "S51": ProtocolState("Radiation Carrier Only", "off", "sync", "active", "on", 1),
    "S52": ProtocolState("Radiate Acquisition Idle", "off", "sync", "active", "on", 2),
    "S50": ProtocolState("Data services (send)", "off", "sync", "active", "on", 0),
    "S54": ProtocolState("Terminate Reply", "off", "sync", "active", "on", 3),
    "S55": ProtocolState("Tail before Quit", "off", "sync", "active", "on", 7),
    "S56": ProtocolState("Token Pass or COMM CHANGE", "off", "sync", "active", "on", 6),
    "S58": ProtocolState("Tail before Switch", "off", "sync", "active", "on", 4),
    "S60": ProtocolState("Data Services (receive)", "on", "off", "active", "off", 0),
    "S61": ProtocolState("Awaiting First Frame", "on", "off", "active", "off", 1),
    "S62": ProtocolState("Wait for Carrier", "on", "off", "active", "off", 2),
}

# State Table 5-4 (DUPLEX=Simplex)
DUPLEX_SIMPLEX_STATES = {
    "S71": ProtocolState("Simplex Transmit", "off", "on", "active", "on", 0),
    "S72": ProtocolState("Simplex Receive", "on", "off", "active", "off", 0),
}
# State Transition Session Establishment Table 5-6 (DUPLEX=Full)
# State Transition Comm Change Table 5-7 (DUPLEX=Full)
# State Transition Session Termination Table 5-8 (DUPLEX=Full)