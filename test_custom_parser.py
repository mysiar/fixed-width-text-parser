import unittest
import custom_parser

definition = [
    ['FIELD_1', 0, 1],
    ['FIELD_2', 1, 10],
    ['FIELD_3', 11, 10],
    ['FIELD_4', 23, 1],
    ['FIELD_5', 24, 2],
    ['FIELD_6', 26, 4],
    ['FIELD_7', 30, 4],
    ['FIELD_8', 34, 4],
]


class CustomParserTest(unittest.TestCase):
    def test_parse_empty_format(self):
        parser = custom_parser.CustomParser()
        record = 'S  21528.00  27830.00  1P1             0       756755.8 2561875.5 138.1265120558'

        data = parser.parse(record)
        self.assertEqual(0, len(data))

    def test_parse(self):
        parser = custom_parser.CustomParser(definition)
        record = 'S  21528.00  27830.00  1P1             0       756755.8 2561875.5 138.1265120558'

        data = parser.parse(record)

        self.assertEqual('S', data[0])
        self.assertEqual('21528.00', data[1])
        self.assertEqual('27830.00', data[2])
        self.assertEqual('1', data[3])
        self.assertEqual('P1', data[4])
        self.assertEqual('', data[5])
        self.assertEqual('', data[6])
        self.assertEqual('', data[7])

    def test_csv(self):
        parser = custom_parser.CustomParser(definition)

        data = parser.get_fields()
        csv = parser.csv(data)
        self.assertEqual('FIELD_1,FIELD_2,FIELD_3,FIELD_4,FIELD_5,FIELD_6,FIELD_7,FIELD_8', csv)


if __name__ == '__main__':
    unittest.main()
