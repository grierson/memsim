""" RAM Canvas """
import tkinter as tk
import tkinter.messagebox
import random


class Ram(tk.Canvas):
    """Ram"""
    def __init__(self, parent):
        """__init__

        :param parent:
        """
        tk.Canvas.__init__(self, parent, bg="white", width=200, height=450)
        self.processes = {"red", "green", "blue"}

    def validate_process(self, process_name, process_size):
        """validate_process_details
        Validate the users input is correct otherwise show error.

        :param process_name -> String:
        Must only be Letters
        :param process_size -> Int:
        Must only be Numbers
        """
        if not process_name.isalpha():
            tkinter.messagebox.showerror("Error!",
                                         "Name must only contain letters")
        elif not str(process_size).isdigit():
            tkinter.messagebox.showerror("Error!",
                                         "Size must only contain numbers")
        elif process_size <= 0:
            tkinter.messagebox.showerror("Error!",
                                         "Size must be larger than 0")
        elif process_name in self.processes:
            tkinter.messagebox.showerror("Error!",
                                         "Process Already Exists")
        else:
            self.add_process(process_name, process_size)

    def add_process(self, process_name, process_size):
        """add_process
        Added new process to Processes List

        :param process_name:
        :param process_size:
        """
        colours = ["red", "orange", "yellow", "green", "blue", "violet"]

        self.processes[process_name] = process_size
        # X, Y, Width (FIXED), Height, Fill
        self.create_rectangle(0,
                              0,
                              200,
                              200,
                              fill=random.choice(colours))

    def kill_process(self):
        """kill_process"""
        self.processes.pop()
