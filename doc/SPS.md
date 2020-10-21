# SPS - Shell Processing Support

## Version 2.1, Jan 2006

### Point record
```
H00 SPS format version num.     SPS 2.1, JAN2006
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
```

### Relation record

```
H00 SPS format version number   SPS 2.1, JAN2006
H26 ---------------------------------------------------------------------------
H26 Item  Definition of field       Cols   Format  Min to Max     Default Units
H26 ----  -------------------       ----   ------  ----------     ------- -----
H26 0     Record identification     1-1    A1      'X'            None    -
H26 1     Field tape number (r adj) 2-7    3A2     Free           None    -
H26 2     Field record number       8-15   I8      0-16777216     None    -
H26 3     Field record increment    16-16  I1      1-9            1       -
H26 4     Instrument code           17-17  A1      1-9            1       -
H26 5     Line name (r adj)         18-27  F10.2   -999999.99 to  None    -
H26                                                9999999.99
H26 6     Point number (r adj)      28-37  F10.2   -999999.99 to  None    -
H26                                                 9999999.99
H26 7     Point index               38-38  I1      1-9            1       -
H26 8     From channel              39-43  I5      1-99999        None    -
H26 9     To channel                44-48  I5      1-99999        None    -
H26 10    Channel increment         49-49  I1      1-9            None    -
H26 11    Line name (r adj)         50-59  F10.2   -999999.99 to  None    -
H26                                                 9999999.99
H26 12    From receiver (r adj)     60-69  F10.2   -999999.99 to  None    -
H26                                                 9999999.99
H26 13    To receiver (r adj)       70-79  F10.2   no default     None    -
H26 14    Receiver Index            80-80  I1      1-9            1       -
X  1001   8287311  19248.00  27516.001    1  4351  27023.00  18875.00  19743.001
X  1001   8287311  19248.00  27516.001  436  8711  27039.00  18873.00  19743.001
```