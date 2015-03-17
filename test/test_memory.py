""" Test Memory """
import sys
import os
import unittest
from source.memory import Memory

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

class TestMemory(unittest.TestCase):
    """TestMemory"""
    def test_validate_process(self):
        """test_validate_process"""
        ram = Memory

