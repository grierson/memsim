#!/usr/bin/env python3
""" Memory Canvas """
try:
    import tkinter as tk
    import tkinter.messagebox as messagebox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as messagebox

M_WIDTH = 200


class Memory(tk.Canvas):
    """Ram"""
    def __init__(self, parent):
        """__init__

        :param parent:
        """
        tk.Canvas.__init__(self, parent, bg="white", width=M_WIDTH, height=450)
        self.processes = ["vim", "firefox", "word"]

    def validate_process(self, process_name, process_size):
        """validate_process_details
        Validate the users input is correct otherwise show error.

        :param process_name -> String:
        Must only be Letters
        :param process_size -> Int:
        Must only be Numbers
        """
        if not process_name.isalpha():
            messagebox.showerror("Error!",
                                 "Name must only contain letters")
            return TypeError
        elif not str(process_size).isdigit():
            messagebox.showerror("Error!",
                                 "Size must only contain numbers")
            return TypeError
        elif int(process_size) <= 0:
            messagebox.showerror("Error!",
                                 "Size must be larger than 0")
            return ValueError
        elif self.find_withtag(process_name):
            messagebox.showerror("Error!",
                                 "Process Already Exists")
            return ValueError
        else:
            self.create_rectangle(0,
                                  0,
                                  M_WIDTH,
                                  process_size,
                                  fill="red",
                                  tag=process_name)
            self.processes.append(process_name)

    def kill(self, process_name):
        """kill"""
        print(process_name)
        if self.find_withtag(process_name):
            self.delete(process_name)
