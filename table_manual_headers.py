import tkinter as tk
from tkinter import ttk
import csv

root = tk.Tk()

tv = ttk.Treeview(columns=(1,2,3), show="headings", height="5")
tv.pack()

tv.heading(1, text="Name")
tv.heading(2, text="Age")
tv.heading(3, text="Email")

root.mainloop()