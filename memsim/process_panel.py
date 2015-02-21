#!/usr/bin/env python
""" Main File """
import tkinter as tk


class Processpanel(tk.LabelFrame):
    """process_panel

    Create the Process Panel so that users can input Process Details.

    :param parent:
    The Parent parameter is the Main Window (root)
    This panel is just part of that main window.
    """
    def __init__(self, parent, ram):
        """__init__

        :param parent:
        :param controller:
        """
        tk.LabelFrame.__init__(self, parent, text="Create Process")
        tk.Label(self, text="Process Name:").grid(row=0)
        self.process_name = tk.StringVar()
        tk.Entry(self, textvariable=self.process_name).grid(row=0, column=1)
        tk.Label(self, text="Process Size:").grid(row=1)
        self.process_size = tk.IntVar()
        tk.Entry(self, textvariable=self.process_size).grid(row=1, column=1)
        tk.Button(self, text="Create Process",
                  command=lambda: self.check_process(ram)).grid(row=2, column=1)

        tk.Label(self, text="Allocation Policies").grid(row=3, column=0)

        tk.Radiobutton(self, text="First Fit", value=1).grid(row=4, column=0)
        tk.Radiobutton(self, text="Best Fit", value=2).grid(row=5, column=0)
        tk.Radiobutton(self, text="Worst Fit", value=3).grid(row=6, column=0)

        tk.Button(self, text="Compact").grid(row=7, column=0)

    def check_process(self, ram):
        """check_process"""
        ram.validate_process(self.process_name.get(), self.process_size.get())
