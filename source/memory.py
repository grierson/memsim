#!/usr/bin/env python3
""" Memory Canvas """
try:
    import tkinter as tk
    import tkinter.messagebox as messagebox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as messagebox
import random

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
                   if process_name == process.get("name"))

    def get_process_size(self, process_name):
        """ (string) -> int

        Get process size
        """
        return next(process.get("size")
                    for process in self.processes
                    if process_name == process.get("name"))

    def get_process_address(self, process_name):
        """ (string) -> int

        Get process address
        """
        return next(process.get("address")
                    for process in self.processes
                    if process_name == process.get("name"))

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
        elif self.check_process_exists(name):
            messagebox.showerror("Error!",
                                 "Process Already Exists")
        else:
            self.first_fit(name, size)


    def create_process(self, name, size, address):
        """ (string, int, int) -> Tk.Rectangle

        Create Tk.Rectangle which represents a Process
        """
        self.processes.append({"name": name,
                               "size": size,
                               "address": address}.copy())
        self.update_memory()

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
                                  process.get("address", None),
                                  M_WIDTH,
                                  process.get("address") + process.get("size"),
                                  fill=random.choice(self.colours),
                                  width=1,
                                  tag=process.get("name"))

    def kill(self, process_name):
        """ (string) -> None

        Kill process in Process list
        """
        self.processes[:] = [item
                             for item in self.processes
                             if item.get("name") != process_name]


    """
    -------------------------------
            Policies
    ------------------------------- 
    """
    def first_fit(self, process_name, process_size):
        """ (string, int) -> None

        First Fit Allocation
        """
        address = 0
        hole_size = 0
        hole_address = 0

        while address <= M_HIGHT:
            for process in self.processes:
                if address == process.get("address"):
                    address += process.get("size")
                    hole_size = 0
                    hole_address = address
                    break

            if hole_size >= process_size:
                self.create_process(process_name, process_size, hole_address)
                break
            else:
                hole_size += 1
                address += 1
