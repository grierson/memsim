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
        self.ram.create_process("Style", 200, 0)
        self.assertTrue(self.ram.check_process_exists("Style"))

    # Process Size
    def test_get_process_size(self):
        """ Test Return Process Size """
        self.ram.create_process("Blankspace", 123, 0)
        self.assertEqual(self.ram.get_process_size("Blankspace"), 123)

    def test_get_process_address(self):
        """ Test Get Process Address

        Note: create_process(process_name, process_size, address)
        """
        self.ram.create_process("Red", 333, 111)
        self.assertEqual(self.ram.get_process_address("Red"), 111)

    def test_kill(self):
        """ Create Process then Kill it """
        self.ram.create_process("Dave", 666, 0)
        self.assertTrue(self.ram.check_process_exists("Dave"))
        self.ram.kill("Dave")
        self.assertFalse(self.ram.check_process_exists("Dave"))

    def test_first_fit(self):
        """ Test First Fit Allocation

        Process Size: 110
        10 Bytes to big for the first hole

        |----------------------------| Address: 0
        |    FavoriteThings: 99      |
        |----------------------------| Address: 100
        |    Hole: 100               | * Process to big for this hole
        |----------------------------| Address: 201
        |    IWillSurvive: 99        |
        |----------------------------| Address: 300
        |    Hole: abs(memory)       | * Process should go here
        |----------------------------|
        """
        # Create Processes to simulate real word
        self.ram.create_process("FavoriteThings", 99, 0)
        self.ram.create_process("IWillSurvive", 99, 201)

        # Actually Past Process through First Fit alloction
        self.ram.first_fit("Summertime", 110)
        self.assertEqual(self.ram.get_process_address("Summertime"), 301)
