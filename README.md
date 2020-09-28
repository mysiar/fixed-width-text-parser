# Fixed width text parser to array

Parsing different defined text formats to array data

Specified format parsers
* **Sps21Parser** - SPS format version num.     SPS 2.1, JAN2006

**CustomParser** - parse anything according to the format definition

Format definition:
 
```python

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
```

Field definition ```['FIELD_6', 26, 4]``` 
* 'FIELD_6' - field name
* 26 - index of text line where the field starts (count starts from 0)
* 4 - field length in characters 
