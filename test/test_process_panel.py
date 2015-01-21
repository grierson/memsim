""" Test Process Panel Module """
import unittest
from memsim.process_panel import ProcessPanel
import tkinter


class TestProcessPanel(unittest.TestCase):
    """TestProcessPanel"""
    def setUp(self):
        """setUp"""
        self.new_panel = ProcessPanel(tkinter.Tk())

    def test_process_details(self):
        """test_process_details"""
        self.new_panel.process_name.set("Firefox")
        self.new_panel.process_size.set(500)
        self.assertTrue(self.new_panel.validate_process_details())
