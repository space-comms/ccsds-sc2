# -------- DECODER HELPERS: TURN VALUES INTO TEXT --------

def describe_x(x: XState, duplex: str) -> str:
    if x == XState.BI_DIRECTIONAL:
        return "X=0: Bi-directional data passing in progress; neither side has declared no-more-data."
    if x == XState.LNMD_LOCAL:
        return "X=1: Local has no more data (LNMD), but this is a half-duplex-only sub-state."
    if x == XState.SENDING_RNMD:
        return "X=2: Local has accepted LNMD and is sending RNMD to the remote; termination will start once RNMD is exchanged."
    if x == XState.GOT_RNMD_HAVE_DATA:
        return "X=3: Local still has data, but it has received RNMD from the remote (half-duplex only)."
    if x == XState.GOT_RNMD_WAIT_LOCAL_EMPTY:
        return "X=4: Local has received RNMD; when local runs out of data it will send RNMD back and complete termination."
    if x == XState.BOTH_EMPTY:
        return "X=5: Both local and remote have no more data; after RNMD exchange the session terminates and X resets to 0."
    return "Unknown X value."

def describe_y(y: YState, duplex: str) -> str:
    if y == YState.IDLE:
        return "Y=0: No Comm_Change is in progress."
    if y == YState.LOCAL_COMM_CHANGE:
        return "Y=1: Local was told to initiate a Physical Layer Comm_Change."
    if y == YState.SENDING_COMM_CHANGE:
        return "Y=2: Comm_Change directive is currently being sent across the link."
    if y == YState.WAIT_ACK:
        return "Y=3: Comm_Change directive sent; waiting for Comm_Change acknowledgement."
    if y == YState.RCCD_RECEIVED:
        if duplex.lower().startswith("half"):
            return "Y=4 is defined for full duplex only; in half duplex this condition is handled in other states."
        return "Y=4: Remote Comm_Change Directive (RCCD) has been received (full duplex only)."
    if y == YState.ACT_ON_RCCD:
        if duplex.lower().startswith("half"):
            return "Y=5 is defined for full duplex only; in half duplex acting on RCCD is covered elsewhere."
        return "Y=5: Acting upon the received RCCD (full duplex only)."
    return "Unknown Y value."

def describe_z(z: ZState) -> str:
    if z == ZState.INLOCK_TRUE:
        return "Z=0: SYMBOL_INLOCK_STATUS has NOT gone false yet during Comm_Change."
    if z == ZState.INLOCK_FALSE:
        return "Z=1: SYMBOL_INLOCK_STATUS has gone false at least once during Comm_Change."
    return "Unknown Z value."

def describe_modulation(mod: ModulationState) -> str:
    if mod == ModulationState.ON:
        return "Modulation=on: Coded symbols are being modulated onto the RF carrier (data/control frames can be sent)."
    else:
        return "Modulation=off: RF carrier may be present, but it is unmodulated (e.g., for acquisition/ranging/idle carrier)."

def describe_boolflag(name: str, val: BoolVar) -> str:
    if name == "NEED_PLCW":
        if val == BoolVar.TRUE:
            return "NEED_PLCW=true: A PLCW should be selected for output when possible."
        else:
            return "NEED_PLCW=false: The last PLCW has been selected for output; no immediate PLCW requirement."
    if name == "NEED_STATUS_REPORT":
        if val == BoolVar.TRUE:
            return "NEED_STATUS_REPORT=true: A status report should be selected for output when possible."
        else:
            return "NEED_STATUS_REPORT=false: A status report was just selected; no immediate status report requirement."
    return f"{name}={val.name.lower()}: generic boolean flag."


def describe_ids(remote_scid, recv_scid, recv_pcid):
    lines = []
    lines.append(f"REMOTE_SCID_BUFFER={remote_scid}: value used when testing frames whose ID field is interpreted as destination.")
    if recv_scid is None:
        lines.append("Receiving_SCID_Buffer=None: receiver will adopt the SCID from the first valid frame or be set by directive.")
    else:
        lines.append(f"Receiving_SCID_Buffer={recv_scid}: incoming frames are checked against this SCID for validation.")
    if recv_pcid is None:
        lines.append("Receiving_PCID_Buffer=None: receiver will adopt PCID from first valid frame or be set by directive.")
    else:
        lines.append(f"Receiving_PCID_Buffer={recv_pcid}: incoming frames are checked against this PCID (0 or 1).")
    return "\n".join(lines)


# -------- INTERACTIVE DEMO --------

def ask_int(prompt, allowed):
    while True:
        try:
            val = int(input(prompt))
            if val in allowed:
                return val
            print(f"Please enter one of {sorted(allowed)}.")
        except ValueError:
            print("Please enter a valid integer.")

def ask_choice(prompt, choices):
    choices_str = "/".join(choices)
    while True:
        val = input(f"{prompt} ({choices_str}): ").strip().lower()
        if val in [c.lower() for c in choices]:
            return val
        print(f"Please enter one of: {choices_str}.")

def main():
    print("=== Operational Control Variables Demo ===")
    print("This tool asks you for raw values and decodes them into human-readable states.\n")

    duplex = ask_choice("Link mode", ["full-duplex", "half-duplex"])

    # X, Y, Z
    x_val = ask_int("Enter X (0–5): ", set(range(0, 6)))
    y_val = ask_int("Enter Y (0–5): ", set(range(0, 6)))
    z_val = ask_int("Enter Z (0 or 1): ", {0, 1})

    # Modulation
    mod_choice = ask_choice("Modulation state", ["on", "off"])
    mod = ModulationState.ON if mod_choice == "on" else ModulationState.OFF

    # Flags
    plcw_choice = ask_choice("NEED_PLCW", ["true", "false"])
    need_plcw = BoolVar.TRUE if plcw_choice == "true" else BoolVar.FALSE

    status_choice = ask_choice("NEED_STATUS_REPORT", ["true", "false"])
    need_status = BoolVar.TRUE if status_choice == "true" else BoolVar.FALSE

    # ID buffers
    remote_scid = ask_int("REMOTE_SCID_BUFFER (0–1023): ", set(range(0, 1024)))

    def ask_optional_int(label, allowed):
        txt = input(f"{label} (enter blank for None, or value in {min(allowed)}–{max(allowed)}): ").strip()
        if txt == "":
            return None
        try:
            val = int(txt)
            if val in allowed:
                return val
        except ValueError:
            pass
        print("Invalid; treating as None.")
        return None

    recv_scid = ask_optional_int("Receiving_SCID_Buffer", set(range(0, 1024)))
    recv_pcid = ask_optional_int("Receiving_PCID_Buffer", {0, 1})

    # Decode
    x = XState(x_val)
    y = YState(y_val)
    z = ZState(z_val)

    print("\n=== Decoded Operational State ===")
    print(f"Link mode: {duplex}")

    print("\nSession Termination (X):")
    print(" ", describe_x(x, duplex))

    print("\nComm_Change (Y):")
    print(" ", describe_y(y, duplex))

    print("\nSYMBOL_INLOCK_STATUS (Z):")
    print(" ", describe_z(z))

    print("\nModulation:")
    print(" ", describe_modulation(mod))

    print("\nPLCW / Status Report Flags:")
    print(" ", describe_boolflag("NEED_PLCW", need_plcw))
    print(" ", describe_boolflag("NEED_STATUS_REPORT", need_status))

    print("\nID Buffers:")
    print(describe_ids(remote_scid, recv_scid, recv_pcid))

    # ---- VALIDITY WARNINGS BASED ON DUPLEX MODE ----
    print("\nValidity checks for chosen duplex mode:")

    if duplex.startswith("full"):
        # X=1 and X=3 are half-duplex-only in the spec
        if x == XState.LNMD_LOCAL or x == XState.GOT_RNMD_HAVE_DATA:
            print("  Warning: X=1 or X=3 are defined only for half-duplex; this combo would not occur in a true full-duplex link.")
        # Y=4 and Y=5 are allowed (full-duplex-only), so no warning here
    else:  # half-duplex
        # X=1 and X=3 are fine here
        # Y=4 and Y=5 are full-duplex-only in the spec
        if y in (YState.RCCD_RECEIVED, YState.ACT_ON_RCCD):
            print("  Warning: Y=4 and Y=5 are defined only for full-duplex; this combo would not occur in a true half-duplex link.")

    print("\nTip: Try switching between full- and half-duplex with the same X/Y to see which combinations are valid or flagged.")


if __name__ == "__main__":
    main()