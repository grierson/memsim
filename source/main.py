#!/usr/bin/env python3
""" Main File """
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from policies_panel import PoliciesPanel
from process_panel import ProcessPanel
from memory import Memory

class Mainwindow(tk.Tk):
    """Mainwindow"""
    def __init__(self, *args, **kwargs):
        """__init__

        :param *args:
        :param **kwargs:
        """
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "MemSim")
        tk.Tk.wm_geometry(self)

        container = tk.Frame(self, bg="red")
        container.pack()

        ram = Memory(container)
        processpanel = ProcessPanel(container, ram)
        policiespanel = PoliciesPanel(container, ram)

        processpanel.grid(row=0, column=0, sticky="news")
        policiespanel.grid(row=1, column=0, sticky="news")
        ram.grid(row=0, column=1, sticky="news", rowspan=2)


if __name__ == "__main__":
    ROOT = Mainwindow()
    ROOT.mainloop()
