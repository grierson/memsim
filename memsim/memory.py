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
            return TypeError
        elif not str(process_size).isdigit():
            messagebox.showerror("Error!",
                                 "Size must only contain numbers")
            return TypeError
        elif int(process_size) <= 0:
            messagebox.showerror("Error!",
                                 "Size must be larger than 0")
            return ValueError
        elif self.find_withtag(process_name):
            messagebox.showerror("Error!",
                                 "Process Already Exists")
            return ValueError
        else:
            self.first_fit(process_name, process_size)

    def first_fit(self, process_name, process_size):
        """first_fit

        :param process_name:
        :param process_size:
        """
        hole = 0
        hole_address = 0

        for address in range(M_HIGHT):
            for process in self.processes:
                if address == self.coords(process)[0]:
                    address += self.coords(process)[3]
                    hole_address = address
                    hole = 0
            if process_size == hole:
                self.create_process(process_name, process_size, hole_address)
                break
            else:
                hole += 1

    def create_process(self, process_name, process_size, address):
        """create_process

        :param process_name:
        :param process_size:
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
        """kill"""
        print(process_name)
        if self.find_withtag(process_name):
            self.delete(process_name)
