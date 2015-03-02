""" RAM Canvas """
try:
    import Tkinter as tk
    import tkMessageBox as messagebox
except:
    import tkinter as tk
    import tkinter.messagebox as messagebox


class Ram(tk.Canvas):
    """Ram"""
    def __init__(self, parent):
        """__init__

        :param parent:
        """
        tk.Canvas.__init__(self, parent, bg="white", width=200, height=450)
        self.processes = {}

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
        elif not str(process_size).isdigit():
            messagebox.showerror("Error!",
                                 "Size must only contain numbers")
        elif process_size <= 0:
            messagebox.showerror("Error!",
                                 "Size must be larger than 0")
        elif process_name in self.processes:
            messagebox.showerror("Error!",
                                 "Process Already Exists")
        else:
            # Add entered Process to Processes
            self.processes[process_name] = process_size

    def kill_process(self, process_name):
        """kill_process"""
        self.processes.pop(process_name, None)
