""" TestMain """
import unittest
from memsim.main import Mainwindow
import tkinter as tk


class TestMain(unittest.TestCase):
    """TestMain"""
    def test_mainwindow_can_be_created(self):
        """test_create_mainwindow"""
        root = tk.Tk()
        window = Mainwindow(root)
