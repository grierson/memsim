#!/usr/bin/env python3
""" Memory Canvas """
try:
    import tkinter as tk
    import tkinter.messagebox as messagebox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as messagebox
import random
from source.process import Process

M_WIDTH = 200
M_HIGHT = 450


class Memory(tk.Canvas):
    """Ram"""
    def __init__(self, parent):
        """ (Tk.Frame) -> None

        Create Process List
        """
        tk.Canvas.__init__(self,
                           parent,
                           bg="white",
                           width=M_WIDTH,
                           height=M_HIGHT)
        self.processes = []
        self.colours = ["red", "blue", "green", "cyan", "yellow", "magenta"]

    def check_process_exists(self, process_name):
        """ (string) -> Bool

        Check whether process name is in Process List
        """
        return any(True for process in self.processes
                   if process_name == process.name)

    def get_process_size(self, process_name):
        """ (string) -> int

        Get process size
        """
        return next(process.size
                    for process in self.processes
                    if process_name == process.name)

    def get_process_address(self, process_name):
        """ (string) -> int

        Get process address
        """
        return next(process.address
                    for process in self.processes
                    if process_name == process.name)

    def validate_process(self, name, size):
        """ (string, int) -> None

        Validate the users input is correct otherwise show error.
        """
        if not name.isalpha():
            messagebox.showerror("Error!",
                                 "Name must only contain letters")
        elif not str(size).isdigit():
            messagebox.showerror("Error!",
                                 "Size must only contain numbers")
        elif int(size) <= 0:
            messagebox.showerror("Error!",
                                 "Size must be larger than 0")
        else:
            self.create_process(name, size, 0)


    def create_process(self, name, size, address):
        """ (string, int, int) -> Tk.Rectangle

        Create Tk.Rectangle which represents a Process
        """
        self.processes.append(Process(name, size, address))

    def update_memory(self):
        """ (string, int, int) -> Tk.Rectangle

        Create Tk.Rectangle which represents a Process
        [x1, y1, x2, y2]
        """
        # Clear Canvas
        self.delete("ALL")

        # Redraw Processes
        for process in self.processes:
            self.create_rectangle(0,
                                  process.address,
                                  M_WIDTH,
                                  process.address + process.size,
                                  fill=random.choice(self.colours),
                                  width=1,
                                  tag=process.name)

    def kill(self, process_name):
        """ (string) -> None

        Kill process in Process list
        """
        if self.find_withtag(process_name):
            self.delete(process_name)


    """ -------------------------------
            OTHER
    ------------------------------- """
    def first_fit(self, process_name, process_size):
        """ (string, int) -> None

        First Fit Allocation
        """
        plist = []
        for process in self.processes:
            temp = {"Address": int(self.coords(process)[0]),
                    "Size": int(self.coords(process)[3])}
            plist.append(temp.copy())

        address = 0
        hole_size = 0
        hole_address = 0

        while address <= M_HIGHT:
            for process in plist:
                if address == process.get("Address", None):
                    address += process.get("Size", None)
                    hole_size = 0
                    hole_address = address
                    break

            if hole_size >= process_size:
                self.create_process(process_name, process_size, hole_address)
                address = 1000
                break
            else:
                hole_size += 1
                address += 1
