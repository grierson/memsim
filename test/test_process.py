""" Test Process Creation """
import unittest
from mock import Mock
from memsim.process import Process

class TestProcess(unittest.TestCase):
    """Test_Process"""
    def test_create_process(self):
        """test_create_process"""
        process = Process(mock.ANY)
        p_name, p_size = process.get_process()
        if p_name.isaplha() and p_size.isnum():
            self.assertTrue(True)
        else:
            self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
