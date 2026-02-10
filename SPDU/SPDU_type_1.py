# Directives/Reports for UHF operations
import json
class SPDU_type_1:
    def __init__(self,data):
        self.data = data
        self.directive = data[13:15]
        self.parameter = dict()
        self.select()
    def decode(self):{

    }

    def select(self):
        match self.directive:
            case 0x00:
                self.parameter = {
                    "TX_FREQUENCY":  self.data[10:12],
                    "TX_ENCODING":self.data[8:9],
                    "TX_MODULATION": self.data[7],
                    "TX_DATA_RATE": self.data[3:6],
                    "TX_MODE":self.data[0:2]
                }
            case 0x01:
                self.parameter = {
                    "TOKEN": self.data[12],
                    "RMND": self.data[11],
                    "DUPLEX": self.data[6:8],
                    "TIME_SAMPLE": self.data[0:5]
                }
            case 0x02:
                self.parameter = {
                    "RX_FREQUENCY":  self.data[10:12],
                    "RX_ENCODING":self.data[8:9],
                    "RX_MODULATION": self.data[7],
                    "RX_DATA_RATE": self.data[3:6],
                    "RX_MODE":self.data[0:2]
                }
            case 0x03:
                self.parameter = {
                    "SEQ_CTRL_FSN": self.data[0:7]
                }
            case 0x04:
                self.parameter = {
                    "PCID1": self.data[12],
                    "PCID0": self.data[11],
                    "TIME_TAG_REQUEST": self.data[8:10],
                    "STATUS_REPORT_REQUEST": self.data[3:7]
                }
            case 0x06:
                self.parameter = {
                    "DIRECTION": self.data[0],
                    "FREQUENCY_TABLE": self.data[1],
                    "RATE_TABLE": self.data[2],
                    "CARRIER_MODULATION": self.data[3:4],
                    "DATA_MODULATION": self.data[5:6],
                    "MODE_SELECT": self.data[7,8],
                    "SCRAMBLER": self.data[9:10],
                    "DIFF_ENCODING": self.data[11],
                    "RS_CODE": self.data[12]
                }
            case 0x07:
                self.parameter = {
                    "SCID": self.data[0:9]
                }