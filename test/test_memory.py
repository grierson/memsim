from source.memory import Memory
import tkinter as tk
import unittest


class TestMemory(unittest.TestCase):
    def setUp(self):
        """ Create Memory Panel """
        parent = tk.Tk()
        self.ram = Memory(parent)

    def test_init(self):
        self.assertEqual(self.ram.processes, [])

    def test_validate_process_name_isalpha(self):
        self.assertTrue(self.ram.validate_process("Firefox", 200))
        self.assertRaises(TypeError, self.ram.validate_process, "", 200)

    def test_validate_process_size_isdigit(self):
        self.assertRaises(TypeError, self.ram.validate_process, "Vim", "aaa")

    def test_validate_process_size_greater_than_zero(self):
        self.assertRaises(ValueError, self.ram.validate_process, "Vim", 0)
