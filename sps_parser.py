from parser import Parser

SRC_DATA_RECORD = 'S'
RCV_DATA_RECORD = 'R'
REL_DATA_RECORD = 'X'
HEADER_RECORD = 'H'

"""
H00 SPS format version num.     SPS 2.1, JAN2006;                                                                                           
H26                                                                             
H26 Item  Definition of field       Cols   Format  Min to Max     Default  Units
H26 ----  -------------------       ----   ------  ----------     -------  -----
H26 0     Record identification     1-1    A1      R or S         None     -    
H26 1     Line name    (right)      2-11   F10.2                  None     -    
H26 2     Point number (right)      12-21  F10.2                  None     -    
H26 3     Point index               24-24  I1      1   9          1        -    
H26 4     Point code                25-26  A2      Free           None     -
H26 5     Static correction         27-30  I4      -999 - 999     Blank    Msec
H26 6     Point Depth               31-34  F4.1    0 - 99.9       None     Metre
H26 7     Seismic datum             35-38  I4      -999 - 9999    None     Metre
H26 8     Uphole time               39-40  I2      0 - 99         Blank    Msec
H26 9     Water depth               41-46  F6.1    0 to 9999.9    Blank    Metre
H26 10    Map grid easting          47-55  F9.1    Free           None     metre
H26 11    Map grid northing         56-65  F10.1   Free           None     metre
H26 12    Map grid elevation        66-71  F6.1    -999.9 9999.9  None     metre
H26 13    Day of Year               72-74  I3      1 999          None     -    
H26 14    Time hhmmss               75-80  3I2     000000 235959  None     -    
H26      1         2         3         4         5         6         7         8
H26 5678901234567890123456789012345678901234567890123456789012345678901234567890
S   3762.00   3961.00  1A2     7.2   0    64.8 454773.4 3008241.9  -0.2177042821
S   3762.00   3959.00  1A2     7.2   0    64.7 454762.9 3008193.0  -0.2177042841
"""

sps21definition = [
    ['RECORD_ID', 0, 1],
    ['LINE', 1, 10],
    ['POINT', 11, 10],
    ['POINT_IDX', 23, 1],
    ['POINT_CODE', 24, 2],
    ['STATIC_COR', 26, 4],
    ['POINT_DEPTH', 30, 4],
    ['DATUM', 34, 4],
    ['UPHOLE_TIME', 38, 2],
    ['WATER_DEPTH', 40, 6],
    ['EASTING', 46, 9],
    ['NORTHING', 55, 10],
    ['ELEVATION', 65, 6],
    ['DAY_OF_YEAR', 71, 3],
    ['TIME', 74, 6],
]


class Sps21Parser(Parser):

    def parse(self, textline):

        record_typ = self.substr(textline, sps21definition[0][1], sps21definition[0][2]).strip()

        if not record_typ in (SRC_DATA_RECORD, RCV_DATA_RECORD, REL_DATA_RECORD):
            return

        if record_typ in (SRC_DATA_RECORD, RCV_DATA_RECORD):
            return self.parse_point_record(textline)

        if record_typ in REL_DATA_RECORD:
            return self.parse_relational_record(textline)

    def get_fields(self):
        fields = []
        for f in sps21definition:
            fields.append(f[0])

        return fields

    def parse_point_record(self, text_line):
        data = []
        for f in sps21definition:
            data.append(self.substr(text_line, f[1], f[2]).strip())

        data[1] = self.parse_float(data[1])
        data[2] = self.parse_float(data[2])
        data[3] = self.parse_int(data[3], 1)
        data[5] = self.parse_int(data[5])
        data[6] = self.parse_float(data[6])
        data[7] = self.parse_int(data[7])
        data[8] = self.parse_int(data[8])
        data[9] = self.parse_float(data[9])
        data[10] = self.parse_float(data[10])
        data[11] = self.parse_float(data[11])
        data[12] = self.parse_float(data[12])
        data[13] = self.parse_int(data[13])

        return data

    def parse_relational_record(self, text_line):
        raise NotImplementedError()
