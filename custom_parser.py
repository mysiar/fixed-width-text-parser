from parser import Parser


class CustomParser(Parser):
    def __init__(self, definition_array=None):
        if definition_array is None:
            definition_array = []
        self.format_array = definition_array

    def parse(self, text_line):
        data = []
        for f in self.format_array:
            data.append(self.substr(text_line, f[1], f[2]).strip())

        return data

    def get_fields(self):
        fields = []
        for f in self.format_array:
            fields.append(f[0])

        return fields
