class Parser:
    # *** TO OVERRIDE ***
    """
        convert array to text line according to the definition
    """

    def format(self, array_data):
        raise NotImplementedError()

    # *** TO OVERRIDE ***
    """
        parse text line to array according to the definition    
    """

    def parse(self, text_line):
        raise NotImplementedError()

    # *** TO OVERRIDE ***
    def get_fields(self):
        raise NotImplementedError()

    def parse_int(self, value, default=0):
        try:
            return int(float(value.strip()))
        except:
            return default

    def csv(self, array_data, delimiter=','):
        return delimiter.join(array_data)

    def parse_float(self, value, default=0.0):
        try:
            return float(value.strip())
        except:
            return default

    def substr(self, text, start, length):
        return text[start:start + length]
