#!/usr/bin/env python3
""" Main File """
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


class ProcessPanel(tk.LabelFrame):
    """process_panel

    Create the Process Panel so that users can input Process Details.

    :param parent:
    The Parent parameter is the Main Window (root)
    This panel is just part of that main window.
    """
    def __init__(self, parent, ram):
        """__init__

        :param parent:
        :param controller:
        """
        tk.LabelFrame.__init__(self, parent, text="Create Process")

        # Process Name
        tk.Label(self, text="Process Name:").grid(row=0)
        process_name = tk.StringVar()
        tk.Entry(self, textvariable=process_name).grid(row=0, column=1)

        # Process Size
        tk.Label(self, text="Process Size:").grid(row=1)
        process_size = tk.IntVar()
        tk.Entry(self, textvariable=process_size).grid(row=1, column=1)

        # Button
        tk.Button(self, text="Create Process",
                  command=lambda:
                  ram.validate_process(process_name.get(),
                                       process_size.get())).grid(row=2,
                                                                 column=1)

