""" TEST MEMORY """
from source.memory import Memory
import tkinter
import unittest


class TestMemory(unittest.TestCase):
    """ TEST Memory Class """
    def setUp(self):
        """ Create Memory Panel """
        parent = tkinter.Tk()
        self.ram = Memory(parent)

    # Process Exists
    def test_check_process_exists(self):
        """ Test that a process name is in the Process List """
        self.ram.create_process("Blink", 200, 0)
        self.assertTrue(self.ram.check_process_exists("Blink"))

    # Process Size
    def test_get_process_size(self):
        """ Test Return Process Size """
        self.ram.create_process("Blankspace", 123, 0)
        self.assertEqual(self.ram.get_process_size("Blankspace"), 123)

    def test_get_process_address(self):
        """ Test Get Process Address

        Note: create_process(process_name, process_size, address)
        """
        self.ram.create_process("Style", 333, 111)
        self.assertEqual(self.ram.get_process_address("Style"), 111)
