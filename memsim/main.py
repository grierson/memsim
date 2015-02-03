""" Main File """
import tkinter as tk
from process_panel import process_panel
from scheduler import ram_canvas

def mainwindow(parent):
    """__init__

    :param parent:
    """
    parent.title("MemSim")
    parent.geometry("800x640")

    # CREATE and PACK
    process_panel(parent)
    ram_canvas(parent)


def main():
    """main"""
    root = tk.Tk()
    mainwindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
