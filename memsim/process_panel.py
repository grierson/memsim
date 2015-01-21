""" Main File """
import tkinter as tk
import tkinter.messagebox
from tkinter import (StringVar,
                     IntVar)


class ProcessPanel:
    """Process:"""
    def __init__(self, parent):
        """__init__
        Create the Process Panel so that users can input Process Details.

        :param parent:
        The Parent parameter is the Main Window (root) because this panel is
        just part of that main window.
        """
        self.frame = tk.LabelFrame(parent,
                                   text="Create Process",
                                   padx=5,
                                   pady=5)
        self.frame.pack(anchor="nw", padx=5, pady=5)

        # Process Name
        tk.Label(self.frame, text="Process Name: ").pack()
        self.process_name = StringVar()
        self.entry_name = tk.Entry(self.frame, textvariable=self.process_name)
        self.entry_name.pack(pady=5)

        # Process Size
        tk.Label(self.frame, text="Process Size: ").pack()
        self.process_size = IntVar()
        self.entry_size = tk.Entry(self.frame, textvariable=self.process_size)
        self.entry_size.pack(pady=5)

        # Create Process Button
        self.button = tk.Button(self.frame,
                                text="Create Process",
                                command=lambda: self.validate_process_details())
        self.button.pack()

    def validate_process_details(self):
        """get_process"""
        if not self.process_name.get().isalpha():
            tkinter.messagebox.showerror("Error!",
                                         "Name must only contain letters")
        elif type(self.process_size.get()) is not int:
            tkinter.messagebox.showerror("Error!",
                                         "Size must only contain numbers")
        elif self.process_size.get() <= 0:
            tkinter.messagebox.showerror("Error!",
                                         "Size must be larger than 0")
        #elif self.entry_name in process_list:
        else:
            print("Create Process")
            return True
