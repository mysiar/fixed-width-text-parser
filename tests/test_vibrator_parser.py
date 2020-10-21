import unittest
from FixedWidthTextParser.Seismic.VibratorParser import ApsParser


class ApsParserTest(unittest.TestCase):
    def test_parse_point(self):
        parser = ApsParser()

        record = 'H26 5678901234567890123456789012345678901234567890123456789012345678901234567890'
        data = parser.parse_point(record)

        self.assertIsNone(data)

        record = 'A         19064.0 25360.01222 70   1   2101863 71 56 72 725883.0 2531118.2 121.6'
        data = parser.parse_point(record)

        self.assertEqual('A', data[0])
        self.assertEqual(19064.0, data[1])
        self.assertEqual(25360.0, data[2])
        self.assertEqual(1, data[3])
        self.assertEqual(2, data[4])
        self.assertEqual(22, data[5])
        self.assertEqual(70, data[6])
        self.assertEqual(1, data[7])
        self.assertEqual(2, data[8])
        self.assertEqual(10, data[9])
        self.assertEqual(18, data[10])
        self.assertEqual(63, data[11])
        self.assertEqual(71, data[12])
        self.assertEqual(56, data[13])
        self.assertEqual(72, data[14])
        self.assertEqual(725883.0, data[15])
        self.assertEqual(2531118.2, data[16])
        self.assertEqual(121.6, data[17])

    def test_parse_point2obj(self):
        parser = ApsParser()

        record = 'H26 5678901234567890123456789012345678901234567890123456789012345678901234567890'
        obj = parser.parse_point2obj(record)

        self.assertIsNone(obj)

        record = 'A         19064.0 25360.01222 70   1   2101863 71 56 72 725883.0 2531118.2 121.6'
        obj = parser.parse_point2obj(record)

        self.assertEqual('A', obj.type)
        self.assertEqual(19064.0, obj.line)
        self.assertEqual(25360.0, obj.point)
        self.assertEqual(1, obj.point_idx)
        self.assertEqual(2, obj.vib_fleet_no)
        self.assertEqual(22, obj.vib_no)
        self.assertEqual(70, obj.vib_drive_level)
        self.assertEqual(1, obj.phase_avg)
        self.assertEqual(2, obj.phase_peak)
        self.assertEqual(10, obj.dist_avg)
        self.assertEqual(18, obj.dist_peak)
        self.assertEqual(63, obj.force_avg)
        self.assertEqual(71, obj.force_peak)
        self.assertEqual(56, obj.stiff)
        self.assertEqual(72, obj.visc)
        self.assertEqual(725883.0, obj.easting)
        self.assertEqual(2531118.2, obj.northing)
        self.assertEqual(121.6, obj.elevation)

