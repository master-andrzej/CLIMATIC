import tkinter as tk

def handle_focus(event):
    if event.widget == root:
        print("I have gained the focus")
        root.geometry("1000x1000")

root = tk.Tk()
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
print(entry2.winfo_rgb("red"))


entry1.pack()
entry2.pack()

root.bind("<FocusOut>", handle_focus)

#root.mainloop()
exit(9)