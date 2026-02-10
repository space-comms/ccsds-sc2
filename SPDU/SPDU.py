import SPDU_type_1
class SPDU:
    def __init__(self):
        self.parameter = {
            "TX_MODE": None,
            "TX_DATA_RATE": None,
            "TX_MODULATION": None,
            "TX_ENCODING": None,
            "TX_FREQUENCY": None,

            "TIME_SAMPLE": None,
            "DUPLEX": None,
            "RMND": None,
            "TOKEN": None,

            "RX_MODE": None,
            "RX_DATA_RATE": None,
            "RX_MODULATION": None,
            "RX_ENCODING": None,
            "RX_FREQUENCY": None,

            "SEQ_CTRL_FSN": None,

            "STATUS_REPORT_REQUEST": None,
            "TIME_TAG_REQUEST": None,
            "PCID0": None,
            "PCID1": None,

            "DIRECTION": None,
            "FREQUENCY_TABLE": None,
            "RATE_TABLE": None,
            "CARRIER_MODULATION": None,
            "DATA_MODULATION": None,
            "MODE_SELECT": None,
            "SCRAMBLER": None,
            "DIFF_ENCODING": None,
            "RS_CODE": None,

            "SCID": None,

            "DEMAND": None,
            "QUERY_RESPONSE": None,
            "POLARISATION": None,
            "MODULATION_INDEX": None,
            "INSTANT_SNR": None,

            "DIRECTIVE_FUNCTION": None,
            "COHERENCE": None,
            "AOS_FRAME": None
        }

    # Iterate through all the keys in the returned library and update the main library
    def update_parameter(self, dictionary):
        for key in dictionary:
            if key in self.parameter:
                self.parameter[key] = dictionary[key]

    def decode(self,type,data):
        match type:
            case 0:
                spdu = SPDU_type_1(data)
                self.t_mode = spdu.t_mode
                self.t_data_rate = spdu.t_data_rate
                self.t_modulation = spdu.t_modulation
                self.t_encoding = spdu.t_encoding
                self.t_frequency = spdu.t_frequency

                self.time_sample = spdu.time_sample
                self.duplex = spdu.duplex
                self.rmnd = spdu.rmnd
                self.token = spdu.token

                self.r_mode = spdu.r_mode
                self.r_data_rate = spdu.r_data_rate
                self.r_modulation = spdu.r_modulation
                self.r_encoding = spdu.r_encoding
                self.r_frequency = spdu.r_frequency

                self.SEQ_CTRL_FSN = spdu.SEQ_CTRL_FSN

                self.status_report_request = spdu.status_report_request
                self.time_tag_request = spdu.time_tag_request
                self.PCID0 = spdu.PCID0
                self.PCID1 = spdu.PCID1

                self.direction = spdu.direction
                self.frequency_table = spdu.frequency_table
                self.rate_table = spdu.rate_table
                self.carrier_mod = spdu.carrier_mod
                self.data_mod = spdu.data_mod
                self.mode_select = spdu.mode_select
                self.scrambler = spdu.scrambler
                self.Diff_Encoding = spdu.Diff_Encoding
                self.RS_code = spdu.RS_code
                self.SCID = spdu.SCID
            case 3:



