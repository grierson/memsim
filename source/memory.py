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
        return any([self.gettags(process)[0] for process in self.processes if
                    process_name in self.gettags(process)])

    def get_process_coords(self, process_name):
        """ (string) -> list of int

        Get address for process
        0 -> FIXED X Position 0 (Should fixed to the left side of canvas)
        1 -> Process Address
        2 -> FIXED WIDTH (M_WIDTH)
        3 -> Process Size
        """
        return list(map(int, self.coords(process_name)))

    def get_process_size(self, process_name):
        """ (string) -> int

        Get process size
        """
        return int(self.coords(process_name)[3])

    def get_process_address(self, process_name):
        """ (string) -> int

        Get process address
        """
        return int(self.coords(process_name)[1])

    def validate_process(self, process_name, process_size):
        """ (string, int) -> None

        Validate the users input is correct otherwise show error.
        """
        if not process_name.isalpha():
            messagebox.showerror("Error!",
                                 "Name must only contain letters")
        elif not str(process_size).isdigit():
            messagebox.showerror("Error!",
                                 "Size must only contain numbers")
        elif int(process_size) <= 0:
            messagebox.showerror("Error!",
                                 "Size must be larger than 0")
        else:
            self.first_fit(process_name, process_size)

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

    def create_process(self, process_name, process_size, address):
        """ (string, int, int) -> Tk.Rectangle

        Create Tk.Rectangle which represents a Process
        """
        self.processes.append(
            self.create_rectangle(0,
                                  address,
                                  M_WIDTH,
                                  process_size,
                                  fill=random.choice(self.colours),
                                  width=1,
                                  tag=process_name
                                  )
        )

    def kill(self, process_name):
        """ (string) -> None

        Kill process in Process list
        """
        if self.find_withtag(process_name):
            self.delete(process_name)
