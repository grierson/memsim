""" Main File """
import tkinter as tk

class Process:
    """Process:"""
    def __init__(self, parent):
        """__init__

        :param parent:
        """
        self.frame = tk.LabelFrame(parent,
                                   text="Create Process",
                                   padx=5,
                                   pady=5)
        self.frame.pack(anchor="nw", padx=5, pady=5)

        # Process Name
        tk.Label(self.frame, text="Process Name: ").pack()
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.pack(pady=5)

        # Process Size
        tk.Label(self.frame, text="Process Size: ").pack()
        self.entry_size = tk.Entry(self.frame)
        self.entry_size.pack(pady=5)

        # Create Process Button
        tk.Button(self.frame,
                  text="Create Process",
                  command=self.get_process).pack()


    def get_process(self):
        """get_process"""
        return self.entry_name.get(), self.entry_size.get()
