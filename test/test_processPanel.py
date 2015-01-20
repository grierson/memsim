""" Test ProcessPanel """
from unittest import TestCase
from memsim.process_panel import ProcessPanel
import tkinter


class TestProcessPanel(TestCase):
    """TestProcessPanel"""
    def setUp(self):
        """setUp"""
        self.new_panel = ProcessPanel(tkinter.Tk())

    def test_process_details(self):
        """test_process_details"""
        self.new_panel.entry_name = "Firefox"
        self.new_panel.entry_size = 500
        self.assertTrue(self.new_panel.entry_name.isalpha())
        self.assertTrue(self.new_panel.entry_size, 500)
