#!/usr/bin/env python3
""" TEST Process Panel """
from unittest import TestCase
from source.process_panel import ProcessPanel
from source.memory import Memory
import tkinter as tk


class TestProcessPanel(TestCase):
    """TestProcessPanel"""
    def setUp(self):
        parent = tk.Tk()
        ram = Memory(parent)
        self.processpanel = ProcessPanel(parent, ram)

    def test_should_store_process_name(self):
        """test_new_process"""
        self.processpanel.process_name = "Firefox"
        self.assertEquals(self.processpanel.process_name, "Firefox")

    def test_should_store_process_size(self):
        """test_new_process"""
        self.processpanel.process_size = 200
        self.assertEquals(self.processpanel.process_size, 200)
