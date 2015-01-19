""" Main File """
import tkinter as tk

class Process:
    """Process:"""
    def __init__(self, parent):
        """__init__

        :param parent:
        """
        self.frame = tk.LabelFrame(parent, text="Process", padx=5, pady=5)
        self.frame.pack()
        tk.Label(self.frame, text="Process Name: ").pack()
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.pack()

        tk.Label(self.frame, text="Process Size: ").pack()
        self.entry_size = tk.Entry(self.frame)
        self.entry_size.pack()

        tk.Button(self.frame,
                  text="Create Process",
                  command=self.get_process,
                  padx=5,
                  pady=5).pack()


    def get_process(self):
        """get_process"""
        print(self.entry_name.get())
        print(self.entry_size.get())
