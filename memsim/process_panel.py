""" Main File """
import tkinter as tk
import tkinter.messagebox
from tkinter import (StringVar,
                     IntVar)
from scheduler import add_process


def process_panel(parent):
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
                       validate_process_details(process_name.get(),
                                                process_size.get()))
    button.pack()


def validate_process_details(process_name, process_size):
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
    else:
        add_process(process_name, process_size)
