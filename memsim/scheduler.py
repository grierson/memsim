""" Process Scheduler """
import tkinter as tk
import tkinter.messagebox
import random


PROCESS_LIST = [{"name": "Hello", "size": 50},
                {"name": "Other", "size": 90},
                {"name": "Big", "size": 190}]


def add_process(process_name, process_size):
    """add_process

    :param process:
    """
    PROCESS_LIST.append({"name": process_name,
                         "size": process_size})


def print_process_list():
    """print_process_list"""
    print(PROCESS_LIST)


def ram_canvas(parent):
    """ram_canvas

    :param parent:
    """
    ram = tk.Canvas(parent, bg="white", height=600, width=200)
    ram.pack(anchor="e")
    ram_size = 0
    colours = ["red", "orange", "yellow", "green", "blue", "violet"]
    for process in PROCESS_LIST:
        ram.create_rectangle(0, ram_size, 200, process["size"],
                             fill=random.choice(colours))
        ram_size = process["size"]
        if ram_size >= 1000:
            tkinter.messagebox.showerror("Error!",
                                         "Buffer Overflow")
    ram.update()
