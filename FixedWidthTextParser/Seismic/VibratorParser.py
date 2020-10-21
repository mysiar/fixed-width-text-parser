"""
    Vibrator Parser
"""
from FixedWidthTextParser.Parser import Parser

# H26 APS Vibrator Attributes
# H26
# H26 Item	Definition of field  		Cols  	Format	Min to Max      		Default	Units
# H26 ----	---------------------		------	------	----------------		-------	-----
# H26 1   	Record identification		1-1   	%1s   	A               		None   	-
# H26 2   	Line name            		2-17  	%16.1f	Free            		None   	-
# H26 3   	Point number         		18-25 	%8.1f 	Free            		None   	-
# H26 4   	Point index          		26-26 	%1d   	1 to 9          		1      	-
# H26 5   	Vibrator fleet number		27-27 	%1d   	Free            		None   	-
# H26 6   	Vibrator number      		28-29 	%2d   	Free            		None   	-
# H26 7   	Vibrator drive level 		30-32 	%3d   	0 to 100        		None   	%
# H26 8   	Average phase        		33-36 	%4d   	-180 to 180     		None   	deg
# H26 9   	Peak phase           		37-40 	%4d   	-180 to 180     		None   	deg
# H26 10  	Average distortion   		41-42 	%2d   	0 to 99         		None   	%
# H26 11  	Peak distortion      		43-44 	%2d   	0 to 99         		None   	%
# H26 12  	Average force        		45-46 	%2d   	0 to 99         		None   	%
# H26 13  	Peak force           		47-49 	%3d   	Free            		None   	%
# H26 14  	Average ground stiffness		50-52 	%3d   	Free            		None   	-
# H26 15  	Average ground viscosity		53-55 	%3d   	Free            		None   	-
# H26 16  	Vib. position easting		56-64 	%9.1f 	Free            		None   	metre
# H26 17  	Vib. position northing		65-74 	%10.1f	Free            		None   	metre
# H26 18  	Vib. position elevation		75-80 	%6.1f 	-999.9 to 9999.9		None   	metre
# H26
# H26      1         2         3         4         5         6         7         8
# H26 5678901234567890123456789012345678901234567890123456789012345678901234567890
# H26
#
# A         19064.0 25360.01222 70   1   2101863 71 56 72 725883.0 2531118.2 121.6

aps = [
    ['RECORD_ID', 0, 1, 'string', None],
    ['LINE', 1, 16, 'float', None],
    ['POINT', 17, 8, 'float', None],
    ['POINT_IDX', 25, 1, 'integer', 1],
    ['VIB_FLEET_NO', 26, 1, 'integer', None],
    ['VIB_NO', 27, 2, 'integer', None],
    ['VIB_DRIVE_LEVEL', 29, 3, 'integer', None],
    ['PHASE_AVG', 32, 4, 'integer', None],
    ['PHASE_PEAK', 36, 4, 'integer', None],
    ['DIST_AVG', 40, 2, 'integer', None],
    ['DIST_PEAK', 42, 2, 'integer', None],
    ['FORCE_AVG', 44, 3, 'integer', None],
    ['FORCE_PEAK', 46, 3, 'integer', None],
    ['STIFF', 49, 3, 'integer', None],
    ['VISC', 52, 3, 'integer', None],
    ['EASTING', 55, 9, 'float', None],
    ['NORTHING', 64, 10, 'float', None],
    ['ELEVATION', 74, 10, 'float', None],
]


class ApsParser(Parser):
    def __init__(self):
        super().__init__()
        self.set_definition(aps)

    def parse_point(self, text_line):
        record_type = self.substr(text_line, aps[0][1], aps[0][2]).strip()

        if record_type != 'A':
            return None

        return self.parse(text_line)

    def parse_point2obj(self, text_line):
        data = self.parse_point(text_line)

        if data is not None:
            return ApsPoint(data)
        else:
            return


class ApsPoint:
    def __init__(self, data_array):
        self.type = data_array[0]
        self.line = data_array[1]
        self.point = data_array[2]
        self.point_idx = data_array[3]
        self.vib_fleet_no = data_array[4]
        self.vib_no = data_array[5]
        self.vib_drive_level = data_array[6]
        self.phase_avg = data_array[7]
        self.phase_peak = data_array[8]
        self.dist_avg = data_array[9]
        self.dist_peak = data_array[10]
        self.force_avg = data_array[11]
        self.force_peak = data_array[12]
        self.stiff = data_array[13]
        self.visc = data_array[14]
        self.easting = data_array[15]
        self.northing = data_array[16]
        self.elevation = data_array[17]
