class Parser:
    def __init__(self, definition=None):
        """
            text line format definition
        """
        self.definition = definition

    def set_definition(self, definition):
        self.definition = definition

    def parse(self, text_line):
        self.is_definition()
        data = []
        for f in self.definition:
            parsed_val = self.substr(text_line, f[1], f[2]).strip()

            data.append(self.convert(f[3], parsed_val))

        return data

    def get_fields(self):
        self.is_definition()
        fields = []
        for f in self.definition:
            fields.append(f[0])

        return fields

    def parse_int(self, value, default=0):
        try:
            return int(float(value.strip()))
        except:
            return default

    def csv_from_array(self, array_data, delimiter=','):
        return delimiter.join(array_data)

    def array_from_csv(self, csv, delimiter=','):
        return csv.split(delimiter)

    def parse_float(self, value, default=0.0):
        try:
            return float(value.strip())
        except:
            return default

    def substr(self, text, start, length):
        return text[start:start + length]

    def convert(self, value_type, string_value):
        if 'string' == value_type:
            return string_value
        elif 'integer' == value_type:
            return self.parse_int(string_value, 0)
        elif 'float' == value_type:
            return self.parse_float(string_value, 0.0)
        else:
            return string_value

    def is_definition(self):
        if self.definition is None:
            raise Exception('Text line format definition missing !')

    # *** TO OVERRIDE ***
    """
        convert array to text line according to the definition
    """
    def format(self, array_data):
        raise NotImplementedError()
