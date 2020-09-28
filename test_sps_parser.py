import unittest
from sps_parser import Sps21Parser


class Sps21ParserTest(unittest.TestCase):
    def test_get_fields(self):
        parser = Sps21Parser()
        fields = parser.get_fields_point()

        self.assertEqual(15, len(fields))
        self.assertEqual('EASTING', fields[10])

    def test_parse(self):
        parser = Sps21Parser()
        record = 'S  21528.00  27830.00  1P1             0       756755.8 2561875.5 138.1265120558'

        data = parser.parse_point(record)
        self.assertEqual('S', data[0])
        self.assertEqual(21528.00, data[1])
        self.assertEqual(27830.00, data[2])
        self.assertEqual(1, data[3])
        self.assertEqual('P1', data[4])
        self.assertEqual(0, data[5])
        self.assertEqual(0.0, data[6])
        self.assertEqual(0, data[7])
        self.assertEqual(0, data[8])
        self.assertEqual(0.0, data[9])
        self.assertEqual(756755.8, data[10])
        self.assertEqual(2561875.5, data[11])
        self.assertEqual(138.1, data[12])
        self.assertEqual(265, data[13])
        self.assertEqual('120558', data[14])

    def test_parse_wrong_record(self):
        parser = Sps21Parser()
        record = 'B  21528.00  27830.00  1P1             0       756755.8 2561875.5 138.1265120558'

        data = parser.parse_point(record)
        self.assertIsNone(data)

    def test_parse_not_implemented(self):
        parser = Sps21Parser()
        record = 'X  21528.00  27830.00  1P1             0       756755.8 2561875.5 138.1265120558'

        with self.assertRaises(Exception):
            parser.parse(record)

    def test_format_not_implemented(self):
        parser = Sps21Parser()

        with self.assertRaises(Exception):
            parser.format([])

    def test_csv(self):
        parser = Sps21Parser()

        data = parser.get_fields_point()
        csv = parser.csv_from_array(data)
        self.assertEqual(
            'RECORD_ID,LINE,POINT,POINT_IDX,POINT_CODE,STATIC_COR,POINT_DEPTH,DATUM,UPHOLE_TIME,WATER_DEPTH,EASTING,NORTHING,ELEVATION,DAY_OF_YEAR,TIME',
            csv
        )


if __name__ == '__main__':
    unittest.main()
