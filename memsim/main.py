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
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = Process(container, self)
        self.frames[Process] = frame
        frame.grid(row=0, column=0, sticky="ne")
        self.show_frame(Process)

    def show_frame(self, cont):
        """show_frame"""
        frame = self.frames[cont]
        frame.tkraise()


class Process(tkinter.Frame):
    """Process"""
    def __init__(self, parent, controller):
        """__init__

        :param parent:
        :param controller:
        """
        tkinter.Frame.__init__(self, parent)
        procces_label = tkinter.Label(self, text="Process Name:")
        procces_label.pack(pady=10, padx=10)

        create_process_button = tkinter.Button(self, text="Create Process",
                                               command=lambda:
                                               controller.show_frame(PageOne))
        create_process_button.pack()


def main():
    """main"""
    app = MemSim()
    app.title("MemSim")
    app.geometry("800x640")
    app.mainloop()


main()
