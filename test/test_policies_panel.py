""" TEST POLICIES """
from source.memory import Memory
from source.policies_panel import PoliciesPanel
import tkinter
import unittest


class TestPloiciesPanel(unittest.TestCase):
    """ TEST Memory Class """
    def setUp(self):
        """ Create Memory Panel """
        parent = tkinter.Tk()
        self.ram = Memory(parent)
        self.panel = PoliciesPanel(parent, self.ram)

    def test_update_list(self):
        """ Test Update list

        Added Temp Processes that should be added to the process list once the
        update_list method is called
        """
        self.ram.create_process("Style", 200, 0)
        self.ram.create_process("Red", 150, 500)
        self.assertEqual(self.ram.get_process_list(), ["Style", "Red"])

        self.panel.update_list(self.ram.get_process_list())

        """ FIND menu GET LIST VALUES
        self.assertEqual(self.panel.menu.cget('list'), ["Style", "Red"])
        """
