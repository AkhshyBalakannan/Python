# TESTING FRAME WORK ARE    UNITTEST(D)    NOSE    PYTEST

#   PYTEST -H WILL GIVE ALL THE FLAGS

# ASSERT ARE STATEMENT WHICH ARE USED TO CHECK THE FUNCTION WITH EXPECTED VALUES

import math_func.py


def test_add():  # we need to import the file
    assert math_func.add(7, 3) == 10
    assert math_func.add(5, 5) == 10
