import tkinter as tk
import time, sys, os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack()

        self.quit = tk.Button(self, text="QUIT", fg="black", bg="red", relief="flat", command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.entry_thing = tk.Entry(self)
        self.entry_thing.pack(side="top")

        self.my_var = tk.StringVar()
        self.my_var.set("Type into me")

        self.entry_thing["textvariable"] = self.my_var
        self.entry_thing.bind('<Key-Return>',
                             self.print_entry)

    def say_hi(self):
        print("hi there, everyone!")
    
    def print_entry(self, event):
        print(self.my_var.get())

root = tk.Tk()
app = Application(master=root)
app.master.title("Lifeguard Swap Scheduler")
app.mainloop()