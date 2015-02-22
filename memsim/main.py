#!/usr/bin/env python
""" Main File """
import tkinter as tk
from process_panel import Processpanel
from ram import Ram

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
        container.pack(side="top", fill="both", expand=True)

        ram = Ram(container)
        processpanel = Processpanel(container, ram)
        processpanel.grid(row=0, column=0, sticky="news")

        ram.grid(row=0, column=1, sticky="news", rowspan=2)



if __name__ == "__main__":
    ROOT = Mainwindow()
    ROOT.mainloop()
