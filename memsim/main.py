#!/usr/bin/env python
""" Main File """
import tkinter as tk
from process_panel import processpanel
from scheduler import Scheduler

class Mainwindow(tk.Frame):
    """__init__

    :param parent:
    """
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        parent.title("MemSim")
        parent.geometry("800x640")

        sch = Scheduler(parent)
        processpanel(parent, sch)


def main():
    """main"""
    root = tk.Tk()
    Mainwindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
