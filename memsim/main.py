""" Main File """
import tkinter as tk
from process import Process

class MemSim:
    """MemSim"""
    def __init__(self, parent):
        """__init__

        :param parent:
        """
        parent.title("MemSim")
        parent.geometry("800x640")

        # CREATE and PACK
        Process(parent)

def main():
    """main"""
    root = tk.Tk()
    MemSim(root)
    root.mainloop()

if __name__ == "__main__":
    main()
