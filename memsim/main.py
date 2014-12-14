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
        frame.grid(row=0, column=0, sticky="nw")
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

        # Process Name
        procces_name_label = tkinter.Label(self, text="Process Name:").pack()
        self.process_name = tkinter.Entry(self)
        self.process_name.pack()

        # Process Size
        procces_size_label = tkinter.Label(self, text="Process Size:").pack()
        self.process_size = tkinter.Entry(self)
        self.process_size.pack()

        # Create Process Button
        create_process_button = tkinter.Button(self,
                                               text="Create Process",
                                               command=self.get_process)
        create_process_button.pack()

    def get_process(self):
        """get_process"""
        print(self.process_name.get())
        print(self.process_size.get())


def main():
    """main"""
    app = MemSim()
    app.title("MemSim")
    app.geometry("800x640")
    app.mainloop()


main()
