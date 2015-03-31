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

    def test_check_process_does_not_exists(self):
        """ Test that a process name is in the Process List """
        self.assertFalse(self.ram.check_process_exists("Forbidden"))

    def test_get_process_address_when_process_size_larger(self):
        """ Test Get Process Address

        Test when the Process Size is larger than the Address
        Note: create_process(process_name, process_size, address)
        """
        self.ram.create_process("Style", 333, 111)
        self.assertEqual(self.ram.get_process_address("Style"), 111)

    def test_get_process_address_when_process_size_smaller(self):
        """ Test Return Process Address

        When the Process Size is smaller than the Address
        Note: create_process(process_name, process_size, address)
        """
        self.ram.create_process("Adam", 111, 222)
        self.assertEqual(self.ram.get_process_address("Adam"), 222)

    def test_get_process_coords(self):
        """ Test Return Process Coords
        Test when the Process size is Greater than the Address

        NOTE:
        create_process(process_name, process_size, address)
        [x1, y1, x2, y2] -> [X, Address, WIDTH, Process Size]
        """
        self.ram.create_process("Wonderland", 333, 100)
        self.assertEqual(self.ram.get_process_coords("Wonderland"),
                         [0, 100, 200, 333])

    def test_get_process_size(self):
        """ Test Return Process Size """
        self.ram.create_process("Blankspace", 123, 0)
        self.assertEqual(self.ram.get_process_size("Blankspace"), 123)

