import tkinter as tk
import customtkinter as ctk


root = ctk.CTk()
root.title("Notes App")
root.geometry("1200x800")

def save():
    if title.get() == "":
        title.insert(0, "Untitled")
    with open(title.get() + ".txt", "w") as f:
        f.write(noteInsert.get("1.0", tk.END))

def load():
    fs = tk.filedialog.askopenfilename().split("/")[-1]
    with open(fs, "r") as f:
        noteInsert.delete("1.0", tk.END)
        noteInsert.insert(tk.END, f.read())
        title.delete(0, tk.END)
        if fs.split(".")[0] != "":title.insert(0, fs.split(".")[0])

def clear():
     noteInsert.delete("1.0", tk.END)


def close():
    save()
    root.destroy()

def new():
    noteInsert.delete("1.0", tk.END)
    title.delete(0, tk.END)



title = ctk.CTkEntry(root, width=500)
title.pack()

noteInsert = ctk.CTkTextbox(root, width=500, height=700)
noteInsert.pack()

saveButton = ctk.CTkButton(root, text="Save", command=save)
openButton = ctk.CTkButton(root, text="Open", command=load)
clearButton = ctk.CTkButton(root, text="Clear", command=clear)
closeButton = ctk.CTkButton(root, text="Close", command=close)
newButton = ctk.CTkButton(root, text="New", command=new)
saveButton.pack()
openButton.pack()
clearButton.pack()
closeButton.pack()
newButton.pack()

saveButton.place(x=350, y=700)
openButton.place(x=530, y=700)
clearButton.place(x=200)
closeButton.place(x=860)
newButton.place(x=710, y=700)


root.mainloop()