""" TEST Process Panel """
from unittest import TestCase
from memsim.process_panel import Processpanel
import tkinter as tk


class TestProcessPanel(TestCase):
    """TestProcessPanel"""
    def test_new_process(self):
        """test_new_process"""
        new_process = Processpanel(tk.Tk())

