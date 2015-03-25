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
        """ Test Return Process Address """
        self.ram.create_process("Style", 200, 123)
        self.assertEqual(self.ram.get_process_address("Style"), 123)


    def test_first_fit(self):
        """
        | Address: 0   |
        | Wonderland   |
        | Size: 200    |
        |              |
        | Hole: 125    | (Style Should go here)
        |              |
        | Address: 325 |
        | Red          |
        | Size: 300    |
        """
        self.ram.create_process("Wonderland", 200, 0)
        self.ram.create_process("Red", 300, 325)
        self.ram.create_process("Style", 500, 100)
        self.assertEqual(self.ram.get_process_address("Style"), 100)


    """
    ERROR!
    Tests indirectly call TKERRORMESSAGE which requires user to close
    (Tests are not automated)

    def test_validate_process_name_isalpha(self):
        self.assertTrue(self.ram.validate_process("Firefox", 200))
        self.assertRaises(TypeError, self.ram.validate_process, "", 200)

    def test_validate_process_size_isdigit(self):
        self.assertRaises(TypeError, self.ram.validate_process, "Vim", "aaa")

    def test_validate_process_size_greater_than_zero(self):
        self.assertRaises(ValueError, self.ram.validate_process, "Vim", 0)
    """
