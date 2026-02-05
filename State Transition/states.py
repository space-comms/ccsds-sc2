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
STATES_DUPLEX_HALF = {
    "S11": ProtocolState("Start Hail Action", "off", "async", "connecting-T", "on", 1),
    "S12": ProtocolState("Send Hail Acquisition", "off", "async", "connecting-T", "on", 2),
    "S13": ProtocolState("Send Hail Directives", "off", "async", "connecting-T", "on", 3),
    "S14": ProtocolState("Send Hail Tail", "off", "async", "connecting-T", "on", 4),
    "S36": ProtocolState("Wait for Hail Response", "on", "off", "connecting-T", "off", 5),
    "S51": ProtocolState("Radiation Carrier Only", "off", "sync", "active", "on", 1),
    "S52": ProtocolState("Radiate Acquisition Idle", "off", "sync", "active", "on", 2),
    "S50": ProtocolState("Data services (send)", "off", "sync", "active", "on", 0),
    "S54": ProtocolState("Terminate Reply", "off", "sync")
}

# State Transition Session Establishment Table 5-6 (DUPLEX=Full)
# State Transition Comm Change Table 5-7 (DUPLEX=Full)
# State Transition Session Termination Table 5-8 (DUPLEX=Full)