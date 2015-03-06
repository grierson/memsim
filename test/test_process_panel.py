#!/usr/bin/env python3
""" TEST Process Panel """
from unittest import TestCase
from memsim.main import Mainwindow
from memsim.process_panel import ProcessPanel
from memsim.memory import Memory
import tkinter as tk


class TestProcessPanel(TestCase):
    """TestProcessPanel"""
    def test_new_process(self):
        """test_new_process"""
        master = Mainwindow()
        ram = Memory(master)
        processpanel = ProcessPanel(master, ram)

        processpanel.process_name = "Firefox"
        processpanel.process_size = 200

        self.assertEquals(processpanel.process_name, "Firefox")
        self.assertEquals(processpanel.process_size, 200)
