ConsoleTable
============

Pretty print tabular data to console.

```python
from datetime import date
from consoletable.table import Table

data = [
    ("Date", "Group", "Value1", "Value2"),
    (date(2014, 5, 11), "A", 4, 1.5),
    (date(2014, 5, 12), "A", 3, 2.5),
    (date(2014, 5, 12), "A", 1, 1.5),
    (date(2014, 5, 14), "A", 6, 3.7),
    (date(2014, 5, 14), "A", 1, 7),
    (date(2014, 5, 11), "B", 2, 6.7),
    (date(2014, 5, 11), "B", 1, 0),
    (date(2014, 5, 11), "B", 1, 2.7),
    (date(2014, 5, 14), "B", 1, 1.2),
    (date(2014, 5, 12), "C", 4, 2.7),
    (date(2014, 5, 12), "C", 8, 0.7),
    (date(2014, 5, 13), "C", 1, 0),
    (date(2014, 5, 13), "C", 2, 3.3),
    (date(2014, 5, 14), "C", 1, 6.3),
]

print Table(data)
```

       2014-05-11  2014-05-12  2014-05-13  2014-05-14
    -------------------------------------------------
    A        4.00        4.00           -        7.00
    B        4.00           -           -        1.00
    C           -       12.00        3.00        1.00


Alternative axes and values can be specified by their indexes through keyword arguments:

```python
print Table(data, x=1, value=3)
```

                    A     B     C
    -----------------------------
    2014-05-11   1.50  9.40     -
    2014-05-12   4.00     -  3.40
    2014-05-13      -     -  3.30
    2014-05-14  10.70  1.20  6.30


Additional printing options can be accessed through the `pretty` method and its keyword arguments:

```python
print Table(data, x=1, value=3).pretty(padding=" | ", header_char="=")
```

               |     A |    B |    C
    ================================
    2014-05-11 |  1.50 | 9.40 |    -
    2014-05-12 |  4.00 |    - | 3.40
    2014-05-13 |     - |    - | 3.30
    2014-05-14 | 10.70 | 1.20 | 6.30


This is a technology demonstration and is not meant for use in production.

-aodin, 2014
