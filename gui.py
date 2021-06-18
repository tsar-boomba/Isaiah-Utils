import tkinter as tk
import time, sys, os
import mainfunctions

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.guard_number = tk.IntVar()
        self.guard_number.set(1)
        self.start_time = tk.StringVar()
        self.rotations = tk.IntVar()
        self.rotations = self.rotations.get()
        self.am_or_pm = tk.StringVar()
        self.create_widgets()


    def create_widgets(self):

        self.quit = tk.Button(self, text="QUIT", fg="black", bg="red", relief="flat", command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.label1 = tk.Label(self, text="Enter num of guards here (max 10)")
        self.label1.pack()
        self.nog_entry = tk.Entry(self, relief="groove", width="50")
        self.nog_entry.pack()
        self.number_of_guards = tk.StringVar()
        self.nog_entry["textvariable"] = self.number_of_guards
        self.spacer1 = tk.Label(self)
        self.spacer1.pack()

        self.label2 = tk.Label(self, text="Enter time between swaps (max 60)")
        self.label2.pack()
        self.swap_entry = tk.Entry(self, relief="groove", width="50")
        self.swap_entry.pack()
        self.swap = tk.StringVar()
        self.swap_entry["textvariable"] = self.swap
        self.spacer2 = tk.Label(self)
        self.spacer2.pack()

        self.label3 = tk.Label(self, text="Enter the hour the working begins (max 12)")
        self.label3.pack()
        self.hours_entry = tk.Entry(self, relief="groove", width="50")
        self.hours_entry.pack()
        self.hours = tk.StringVar()
        self.hours_entry["textvariable"] = self.hours
        self.spacer3 = tk.Label(self)
        self.spacer3.pack()

        self.label4 = tk.Label(self, text="Enter the minute the working begins (max 59)")
        self.label4.pack()
        self.minutes_entry = tk.Entry(self, relief="groove", width="50")
        self.minutes_entry.pack()
        self.minutes = tk.StringVar()
        self.minutes_entry["textvariable"] = self.minutes
        self.spacer4 = tk.Label(self)
        self.spacer4.pack()

        self.label5 = tk.Label(self, text="Start in AM or PM?")
        self.label5.pack()
        self.am_pm_var = tk.IntVar()
        self.am_radio = tk.Radiobutton(self, text="AM", variable=self.am_pm_var, value=1, command=self.rotations_func())
        self.am_radio.pack()
        self.pm_radio = tk.Radiobutton(self, text="PM", variable=self.am_pm_var, value=2, command=self.rotations_func())
        self.pm_radio.pack()
        self.spacer5 = tk.Label(self)
        self.spacer5.pack()

        self.generate_button = tk.Button(self, text="GO", bg="green")
        self.generate_button["command"] = self.schedule_generator()
        self.generate_button.pack()

    def am_pm_assigner(self):
        self.am_pm_var = self.am_pm_var.get()
        if self.am_pm_var == 1:
            self.am_or_pm.set("AM")
            self.am_or_pm = self.am_or_pm.get()
        elif self.am_pm_var == 2:
            self.am_or_pm.set("PM")
            self.am_or_pm = self.am_or_pm.get()


    def time_formatter(self):
        self.minutes = int(self.minutes.get())
        if self.minutes < 10:
            self.minutes = str(self.minutes)
            self.minutes = "0" + self.minutes
            self.start_time = self.hours + ":" + self.minutes
            return self.start_time
        else:
            self.minutes = str(self.minutes)
            self.start_time = self.hours + ":" + self.minutes
            return self.start_time
    
    def rotations_func(self):
        if self.am_pm_var == 1 and int(self.hours) != 12:
            self.rotations = (21-int(self.hours))*(60/int(self.swap))
        elif self.am_pm_var == 2 and int(self.hours) != 12:
            self.rotations = (21-(12+int(self.hours)))*(60/int(self.swap))
        elif self.am_pm_var == 1 and int(self.hours) == 12:
            self.rotations = 21*(60/int(self.swap))
        elif self.am_pm_var == 2 and int(self.hours) == 12:
            self.rotations = (21-int(self.hours))*(60/int(self.swap))

    def schedule_generator(self):
        try:
            self.number_of_guards = self.number_of_guards.get()
            self.number_of_guards = int(self.number_of_guards)
            self.swap = self.swap.get()
            self.hours = self.hours.get()
            self.minutes = self.minutes.get()
        except:
            print("")
        self.hours = str(self.hours)
        if self.rotations > 0:
            self.shift_time = tk.StringVar()
            self.shift_time = self.time_formatter()
            self.guard_number = str(self.guard_number.get())
            print(f"Guard {self.guard_number}   {self.shift_time}{self.am_or_pm}")
            self.guard_number = int(self.guard_number)
            self.guard_number = self.guard_number + 1
            if self.guard_number > self.number_of_guards:
                self.guard_number = 1
            self.rotations = int(self.rotations.get()) - 1
            self.hours = int(self.hours)
            self.minutes = int(self.minutes)
            self.minutes = self.minutes + int(self.swap.get())
            if self.minutes >= 60:
                if self.hours + 1 == 12:
                    if self.am_or_pm == "AM":
                        self.am_or_pm.set("PM")
                    else:
                        self.am_or_pm.set("AM")
                self.hours = self.hours + 1
                self.minutes = self.minutes - 60
            if self.hours > 12:
                self.hours.set(1)
            return self.schedule_generator()

    def say_hi(self):
        print("hi there, everyone!")
    
    def print_entry(self, event):
        print(self.number_of_guards.get())

root = tk.Tk()
app = Application(master=root)
app.master.title("Lifeguard Swap Scheduler")
app.mainloop()