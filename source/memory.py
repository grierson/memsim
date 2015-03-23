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
        """__init__

        :param parent:
        """
        tk.Canvas.__init__(self,
                           parent,
                           bg="white",
                           width=M_WIDTH,
                           height=M_HIGHT)
        self.processes = []
        self.colours = ["red", "blue", "green", "cyan", "yellow", "magenta"]

    def check_process_exists(self, process_name):
        """ Check whether process name is in Process List """
        return any([self.gettags(process)[0] for process in self.processes if
                    self.gettags(process)])


    def validate_process(self, process_name, process_size):
        """validate_process_details
        Validate the users input is correct otherwise show error.

        :param process_name -> String:
        Must only be Letters
        :param process_size -> Int:
        Must only be Numbers
        """

        if not process_name.isalpha():
            messagebox.showerror("Error!",
                                 "Name must only contain letters")
            raise TypeError

        elif not str(process_size).isdigit():
            messagebox.showerror("Error!",
                                 "Size must only contain numbers")
            raise TypeError

        elif int(process_size) <= 0:
            messagebox.showerror("Error!",
                                 "Size must be larger than 0")
            raise ValueError

        else:
            self.create_process(process_name, process_size)
            return True

    def first_fit(self, process_name, process_size):
        """first_fit

        :param process_name:
        :param process_size:
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
                    address += process["Size"]
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

    def create_process(self, process_name, process_size):
        """create_process

        :param process_name:
        :param process_size:
        """
        self.processes.append(
            self.create_rectangle(0,
                                  0,
                                  M_WIDTH,
                                  process_size,
                                  fill=random.choice(self.colours),
                                  width=1,
                                  tag=process_name
                                  )
        )

    def kill(self, process_name):
        """kill"""
        if self.find_withtag(process_name):
            self.delete(process_name)
