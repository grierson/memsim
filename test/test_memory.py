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

    def test_check_process_exists(self):
        """ Test that a process name is in the Process List """
        self.ram.create_process("Wonderland", 200, 0)
        self.assertTrue(self.ram.check_process_exists("Wonderland"))

    def test_get_process_coords(self):
        """ Test Return Process Coords """
        self.ram.create_process("Wonderland", 333, 100)
        self.assertEqual(self.ram.get_process_coords("Wonderland"),
                         [0, 100, 200, 333])

    def test_get_process_size(self):
        """ Test Return Process Size """
        self.ram.create_process("Blankspace", 123, 0)
        self.assertEqual(self.ram.get_process_size("Blankspace"), 123)

    def test_get_process_address(self):
        """ Test Return Process Address

        Note: create_process(process_name, process_size, address)
        """
        self.ram.create_process("Style", 200, 333)
        self.assertEqual(self.ram.get_process_address("Style"), 333)
