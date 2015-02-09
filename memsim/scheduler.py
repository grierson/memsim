""" Process Scheduler """
import tkinter as tk
import tkinter.messagebox
import random


class Scheduler():
    """Schduler"""
    def __init__(self, parent):
        """__init__

        :param parent:
        """
        frame = tk.Frame(parent)
        frame.place(in_=parent, anchor="n")
        self.ram = tk.Canvas(frame, bg="white", height=600, width=200)
        self.ram.pack(anchor="e")
        self.processes = {}
        self.ram_size = 0

    def validate_process_details(self, process_name, process_size):
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

        :param process:
        """
        self.processes[process_name] = process_size
        self.update_ram()

    def get_process_size(self, process_name):
        """get_process_size

        :param process_name:
        """
        if process_name in self.processes:
            return self.processes[process_name]

    def update_ram(self):
        """update_ram"""
        colours = ["red", "orange", "yellow", "green", "blue", "violet"]
        for process in self.processes:
            self.ram.create_rectangle(0, self.ram_size, 0, process,
                                      fill=random.choice(colours))
            self.ram_size = process
            if self.ram_size >= 1000:
                tkinter.messagebox.showerror("Error!",
                                             "Buffer Overflow")

    def print_list(self):
        """print_list"""
        print(self.processes)
