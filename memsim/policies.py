""" ProcessPolicies """
import tkinter as tk

class ProcessPolicies(tk.LabelFrame):
    """ProcessPolicies"""
    def __init__(self, parent):
        """__init__

        :param parent:
        """
        tk.LabelFrame.__init__(self, parent, text="Process Policies")
        tk.Label(self, text="Allocation Policies").pack()

        allocation = [
            ("First Fit", "first"),
            ("Best Fit", "best"),
            ("Worst Fit", "worst"),
        ]
        for policie in allocation:
            tk.Label(self, text=policie).pack()
