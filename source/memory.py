#!/usr/bin/env python3
""" Memory Canvas """
try:
    import tkinter as tk
    import tkinter.messagebox as messagebox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as messagebox
import random

M_WIDTH = 200
M_HIGHT = 450


class Memory(tk.Canvas):
    """Ram"""
    def __init__(self, parent):
        """ (Tk.Frame) -> None

        Create Process List
        """
        tk.Canvas.__init__(self,
                           parent,
                           bg="white",
                           width=M_WIDTH,
                           height=M_HIGHT)
        self.processes = []
        self.colours = ["red", "blue", "green", "cyan", "yellow", "magenta"]
        self.allocation_policies = [self.first_fit,
                                    self.best_fit,
                                    self.worst_fit]
        self.selected_policy = 1

    def set_selected_policy(self, value):
        """ set self.selected_policies """
        self.selected_policy = value

    def get_process_list(self):
        """ Get Process List """
        return [process.get("name") for process in self.processes]

    def check_process_exists(self, process_name):
        """ (string) -> Bool

        Check whether process name is in Process List
        """
        return any(True
                   for process in self.processes
                   if process_name == process.get("name"))

    def get_process_size(self, process_name):
        """ (string) -> int

        Get process size
        """
        return next(process.get("size")
                    for process in self.processes
                    if process_name == process.get("name"))

    def get_process_address(self, process_name):
        """ (string) -> int

        Get process address
        """
        return next(process.get("address")
                    for process in self.processes
                    if process_name == process.get("name"))

    def validate_process(self, name, size):
        """ (string, int) -> None

        Validate the users input is correct otherwise show error.
        """
        if not name.isalpha():
            messagebox.showerror("Error!",
                                 "Name must only contain letters")
        elif not str(size).isdigit():
            messagebox.showerror("Error!",
                                 "Size must only contain numbers")
        elif int(size) <= 10:
            messagebox.showerror("Error!",
                                 "Size must be greater than 10")
        elif self.check_process_exists(name):
            messagebox.showerror("Error!",
                                 "Process Already Exists")
        else:
            self.allocation_policies[self.selected_policy](name, size)

    def create_process(self, name, size, address):
        """ (string, int, int) -> Tk.Rectangle

        Create Tk.Rectangle which represents a Process
        """
        self.processes.append({"name": name,
                               "size": size,
                               "address": address,
                               "colour": random.choice(self.colours)}.copy())
        self.update_memory()

    def update_memory(self):
        """ (string, int, int) -> Tk.Rectangle

        Create Tk.Rectangle which represents a Process
        [x1, y1, x2, y2]
        """
        # Clear Canvas
        self.delete("all")

        # Redraw Processes
        for process in self.processes:
            # TEMP variables to make code cleaner
            name = process.get("name")
            address = process.get("address")
            size = process.get("size")

            self.create_rectangle(0,
                                  address,
                                  M_WIDTH,
                                  address + size,
                                  fill=process.get("colour"),
                                  width=1,
                                  tag=name)
            self.create_text((M_WIDTH / 2),
                             address + (size / 2),
                             text="{} : {}".format(name, size))
            self.create_text(22,
                             address + 6,
                             text="{}".format(hex(address)))


    def kill(self, process_name):
        """ (string) -> None

        Kill process in Process list
        """
        self.processes[:] = [item
                             for item in self.processes
                             if item.get("name") != process_name]
        self.update_memory()


    """
    -------------------------------
            Policies
    ------------------------------- 
    """
    def find_holes(self):
        """ Find all Holes in Memory """
        address = 0
        hole_size = 0
        hole_address = 0
        holes = []

        if len(self.processes) <= 0:
            return [{"address": 0, "size": M_HIGHT}]

        while address <= M_HIGHT:
            for process in self.processes:
                if address == process.get("address") or address == M_HIGHT:
                    address += process.get("size")
                    holes.append({"address": hole_address,
                                  "size": hole_size})
                    hole_size = 0
                    hole_address = address
                elif address == M_HIGHT:
                    holes.append({"address": hole_address,
                                  "size": hole_size})
                    hole_size = 0
                    hole_address = address
            hole_size += 1
            address += 1

        for hole in holes[1:]:
            self.create_text(M_WIDTH / 2,
                             hole.get("address") + 5,
                             text="Hole {}".format(hole.get("size")))


        # Need to remove First Element which includes address: 0, size: 0
        return holes[1:]

    def first_fit(self, process_name, process_size):
        """ (string, int) -> None

        First Fit using find_holes
        """
        for hole in self.find_holes():
            if hole.get("size") >= process_size:
                self.create_process(process_name,
                                    process_size,
                                    hole.get("address"))
                return

    def best_fit(self, process_name, process_size):
        """ (string, int) -> None

        Best Fit using find_holes
        """
        smallest_hole = max(hole.get("size") for hole in self.find_holes())
        best_address = 0

        for hole in self.find_holes():
            diff = hole.get("size") - process_size
            if diff < smallest_hole and diff >= 0:
                smallest_hole = diff
                best_address = hole.get("address")


        self.create_process(process_name,
                            process_size,
                            best_address)

        return

    def worst_fit(self, process_name, process_size):
        """ (string, int) -> None

        Worst Fit using find_holes
        """
        biggest_hole = max(hole.get("size") for hole in self.find_holes())

        for hole in self.find_holes():
            if hole.get("size") == biggest_hole:
                self.create_process(process_name,
                                    process_size,
                                    hole.get("address"))
                return

    def compact(self):
        """ Compact """
        for _ in range(len(self.processes)):
            prev_address = 0
            prev_size = 0
            for process in self.processes:
                temp_address = process.get("address")
                process["address"] = prev_address + prev_size
                prev_address = temp_address
                prev_size = process.get("size") + 1 # Plus one so no overlap

        self.update_memory()
