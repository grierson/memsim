""" Test Process """
import unittest
from memsim.process import Process


class TestProcess(unittest.TestCase):
    """TestProcess"""
    def test_get_name(self):
        """test_get_name"""
        new_process = Process("Vim", 500)
