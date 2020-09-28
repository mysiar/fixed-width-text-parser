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

sps21point = [
    ['RECORD_ID', 0, 1, 'string'],
    ['LINE', 1, 10, 'float'],
    ['POINT', 11, 10, 'float'],
    ['POINT_IDX', 23, 1, 'integer', 1],
    ['POINT_CODE', 24, 2, 'string'],
    ['STATIC_COR', 26, 4, 'integer'],
    ['POINT_DEPTH', 30, 4, 'float'],
    ['DATUM', 34, 4, 'integer'],
    ['UPHOLE_TIME', 38, 2, 'integer'],
    ['WATER_DEPTH', 40, 6, 'float'],
    ['EASTING', 46, 9, 'float'],
    ['NORTHING', 55, 10, 'float'],
    ['ELEVATION', 65, 6, 'float'],
    ['DAY_OF_YEAR', 71, 3, 'integer'],
    ['TIME', 74, 6, 'string'],
]


class Sps21Parser(Parser):

    def parse_point(self, text_line):
        record_type = self.substr(text_line, sps21point[0][1], sps21point[0][2]).strip()
        if not record_type in (SRC_DATA_RECORD, RCV_DATA_RECORD):
            return
        self.set_definition(sps21point)
        return self.parse(text_line)

    def parse_relation(self, text_line):
        record_type = self.substr(text_line, sps21point[0][1], sps21point[0][2]).strip()
        if not record_type in REL_DATA_RECORD:
            return

        self.set_definition(None)
        return self.parse(text_line)

    def get_fields_point(self):
        self.set_definition(sps21point)
        return self.get_fields()

    def get_fields_relation(self):
        # self.set_definition(sps21point)
        return self.get_fields()
