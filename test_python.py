import pytest
import math
from others_fanc import *

list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
numbers = [10, 15, 7]

def test_filter():
    assert list(filter(str.isdigit, list_of_strings)) == ['100', '1', '50']

def test_map():
    assert list(map(lambda x: x * 2 + 3, numbers)) == [23, 33, 17]

def test_sorted():
    assert sorted(numbers) == [7, 10, 15]

def test_math_pi():
    assert math.pi == 3.141592653589793

def test_math_sqrt():
    assert math.sqrt(9) == 3.0

def test_math_pow():
    assert math.pow(2,2) == 4.0

def test_math_hypot():
    assert math.hypot(-2, 0) == 2.0





