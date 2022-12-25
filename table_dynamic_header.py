import tkinter as tk
from tkinter import ttk
import csv

root = tk.Tk()

file = open('data.csv')

csvreader = csv.reader(file)
columns = []
columns = next(csvreader) # column headers
row_set = [row for row in csvreader] # list of rows of data

tree_view = ttk.Treeview(root)
tree_view.grid(row=1, column=1,padx=30, pady=20)
tree_view["columns"] = columns

for i in columns:
    tree_view.column(i, width=150, anchor="c")
    tree_view.heading(i, text = i)

for dt in row_set:
    value = [r for r in dt]
    tree_view.insert("", "end", iid=value[0], values=value)

tree_view.pack()
root.mainloop()