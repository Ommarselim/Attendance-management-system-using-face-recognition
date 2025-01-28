import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np

class App:
    def __init__(self, master):
        self.master = master
        master.title("FCFS Disk Scheduling Algorithm")

        self.label = tk.Label(master, text="Enter the disk queue:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Run FCFS", command=self.run_fcfs)
        self.button.pack()

    def run_fcfs(self):
        disk_queue = self.entry.get()
        if disk_queue:
            disk_queue = pd.Series(map(int, disk_queue.split()))
            head = disk_queue[0]
            moves = np.abs(disk_queue - head).sum()
            messagebox.showinfo("FCFS Result", f"Total head movements: {moves}")
        else:
            messagebox.showwarning("Error", "Please enter a valid disk queue")

root = tk.Tk()
app = App(root)
root.mainloop()
