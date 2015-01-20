""" Main File """
import tkinter as tk
from tkinter import StringVar


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
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.pack(pady=5)

        # Process Size
        tk.Label(self.frame, text="Process Size: ").pack()
        self.entry_size = tk.Entry(self.frame)
        self.entry_size.pack(pady=5)

        # Create Process Button
        self.button = tk.Button(self.frame,
                                text="Create Process",
                                command=self.check_process_details)
        self.button.pack()

    def check_process_details(self):
        """get_process"""
        if self.entry_name.get().isalpha():
            print("Yes!")
        else:
            print("No!")
