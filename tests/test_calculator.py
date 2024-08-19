# tests/test_calculator.py
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from calculator import add, substract, multiply, calculator

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0

def test_substract():
    assert substract(5, 3) == 2
    assert substract(-1, -1) == 0
    assert substract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, -1) == 1
    assert multiply(-1, 1) == -1

def test_calculator():
    assert calculator(3, 2, '+') == 5
    assert calculator(5, 3, '-') == 2
    assert calculator(2, 3, '*') == 6
    assert calculator(5, 3, '/') == "Invalid operator"  # Test for invalid operator
    assert calculator(0, 0, '+') == 0
    assert calculator(1, 0, '-') == 1
    assert calculator(0, 1, '*') == 0
