""" Main File """
import tkinter as tk
from process_panel import ProcessPanel

class MainWindow:
    """ MemSim
    Main Window
    """
    def __init__(self, parent):
        """__init__

        :param parent:
        """
        self.parent = parent
        parent.title("MemSim")
        parent.geometry("800x640")

        # CREATE and PACK
        self.process_panel = ProcessPanel(parent)

def main():
    """main"""
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
