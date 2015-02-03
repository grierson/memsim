""" Test Process Panel Module """
import unittest
from memsim.process_panel import ProcessPanel
import tkinter


class TestProcessPanel(unittest.TestCase):
    """TestProcessPanel"""
    def setUp(self):
        """setUp"""
        self.new_panel = ProcessPanel(tkinter.Tk())
        pass

