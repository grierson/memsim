#!/usr/bin/env python
""" Main File """
import tkinter as tk
from tkinter import (StringVar,
                     IntVar)


def processpanel(parent, sch):
    """process_panel

    Create the Process Panel so that users can input Process Details.

    :param parent:
    The Parent parameter is the Main Window (root)
    This panel is just part of that main window.
    """
    frame = tk.LabelFrame(parent,
                          text="Create Process",
                          padx=5,
                          pady=5)
    frame.pack(anchor="nw", padx=5, pady=5)

    # Create Name
    tk.Label(frame, text="Process Name: ").pack()
    process_name = StringVar()
    entry_name = tk.Entry(frame, textvariable=process_name)
    entry_name.pack(pady=5)

    # Create Size
    tk.Label(frame, text="Process Size: ").pack()
    process_size = IntVar()
    entry_size = tk.Entry(frame, textvariable=process_size)
    entry_size.pack(pady=5)

    # Create Process Button
    # Disable Unnecessary Lambda Call because it is to prevent tkinter from
    # running the code when first loaded
    # pylint: disable=W0108
    button = tk.Button(frame,
                       text="Create Process",
                       command=lambda:
                       sch.validate_process_details(process_name.get(),
                                                    process_size.get()))
    button.pack()

    button1 = tk.Button(frame,
                        text="Print Processes",
                        command=lambda: sch.print_list())
    button1.pack()
