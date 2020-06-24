import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello World")
label.config(fg='#333333', bg='#eeeeee',
             font=("monospace", 30, "bold"))
label.config(height=5, width=10)
label.pack(fill=tk.BOTH, expand=tk.YES)

root.mainloop()