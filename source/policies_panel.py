#!/usr/bin/env python3
""" Main File """
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


class PoliciesPanel(tk.LabelFrame):
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
        tk.LabelFrame.__init__(self, parent, text="Policies")
        self.compact(ram)
        self.kill(ram)
        self.allocation_policies(ram)

    def allocation_policies(self, ram):
        """ Load Allocation Policies Radio Buttons """
        tk.Label(self, text="Allocation Policies").grid(row=0, column=0)
        self.selected_policie = tk.IntVar()
        self.selected_policie.set(0)
        self.policies = [
            ("First Fit", 0),
            ("Best Fit", 1),
            ("Worst Fit", 2),
        ]
        for name, value in self.policies:
            tk.Radiobutton(self,
                           text=name,
                           variable=self.selected_policie,
                           value=value,
                           command=lambda:
                           ram.selected_policy(self.selected_policie.get())
                           ).grid(row=value, column=1)

    def compact(self, ram):
        """ Load Compact Button """
        tk.Button(self,
                  text="Compact",
                  command=lambda:
                  ram.compact()).grid(row=4, column=0)

    def kill(self, ram):
        """ Load Process List and Kill Button """
        tk.Label(self, text="Process List").grid(row=5, column=0)
        self.var = tk.StringVar(self)
        self.menu = tk.OptionMenu(self,
                                  self.var,
                                  ())
        self.menu.grid(row=5, column=1)
        tk.Button(self,
                  text="Update process list",
                  command=lambda:
                  self.update_list(ram.process_list)).grid(row=6,
                                                           column=0)

        tk.Button(self,
                  text="Kill process",
                  command=lambda:
                  ram.kill(self.var.get())).grid(row=6, column=1)

    def update_list(self, processes):
        """ Update Plist """
        self.var.set('')
        self.menu['menu'].delete(0, 'end')

        for item in processes:
            self.menu['menu'].add_command(label=item,
                                          command=tk._setit(self.var,
                                                            item))
