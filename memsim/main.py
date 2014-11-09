""" Main File """
import tkinter


LARGE_FONT = ("Verdana", 12)

class MemSim(tkinter.Tk):
    """MemSim"""
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="ne")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        """show_frame"""
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tkinter.Frame):
    """StartPage"""
    def __init__(self, parent, controller):
        """__init__

        :param parent:
        :param controller:
        """
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


def main():
    """main"""
    app = MemSim()
    app.title("MemSim")
    app.geometry("800x640")
    app.mainloop()


main()
