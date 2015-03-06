#!/usr/bin/env python3
""" Main File """
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


class PoliciesPanel(tk.LabelFrame):
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
        tk.LabelFrame.__init__(self, parent, text="Policies")

        tk.Label(self, text="Allocation Policies").grid(row=0, column=0)

        tk.Radiobutton(self, text="First Fit", value=1).grid(row=1, column=0)
        tk.Radiobutton(self, text="Best Fit", value=2).grid(row=2, column=0)
        tk.Radiobutton(self, text="Worst Fit", value=3).grid(row=3, column=0)

        tk.Button(self, text="Compact").grid(row=4, column=0)

        tk.Label(self, text="Process List").grid(row=5, column=0)
        self.var = tk.StringVar()
        self.var.set(ram.processes[0])
        self.selected = tk.OptionMenu(self,
                                      self.var,
                                      *ram.processes).grid(row=5, column=1)
        tk.Button(self,
                  text="Kill Process",
                  command=lambda:
                  ram.kill(self.var.get())).grid(row=6, column=0)
