#!/usr/bin/env python3
""" TEST Process Panel """
from unittest import TestCase
from source.process_panel import ProcessPanel
import tkinter as tk


class TestProcessPanel(TestCase):
    """TestProcessPanel"""
    def test_new_process(self):
        """test_new_process"""
        processpanel = ProcessPanel

        processpanel.process_name = "Firefox"
        processpanel.process_size = 200

        self.assertEquals(processpanel.process_name, "Firefox")
        self.assertEquals(processpanel.process_size, 200)
