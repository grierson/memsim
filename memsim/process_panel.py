#!/usr/bin/env python
""" Main File """
import tkinter as tk
import tkinter.messagebox


class Processpanel(tk.LabelFrame):
    """process_panel

    Create the Process Panel so that users can input Process Details.

    :param parent:
    The Parent parameter is the Main Window (root)
    This panel is just part of that main window.
    """
    def __init__(self, parent):
        """__init__

        :param parent:
        :param controller:
        """
        tk.LabelFrame.__init__(self, parent, text="Create Process")
        tk.Label(self, text="Process Name:").grid(row=0)
        process_name = tk.Entry(self).grid(row=0, column=1)
        tk.Label(self, text="Process Size:").grid(row=1)
        process_size = tk.Entry(self).grid(row=1, column=1)

        tk.Button(self, text="Create Process", command=lambda:
                  self.validate_details(process_name.get(),
                                        process_size.get())).grid(row=2,
                                                                  column=1)

    def validate_details(self, process_name, process_size):
        """validate_details"""
        pass

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
