""" Test Process Creation """
import unittest
import process

class TestProcess(unittest.TestCase):
    """Test_Process"""
    def test_create_process(self):
        """test_create_process"""
        process = Process("Firefox", 500)
