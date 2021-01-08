import ctypes
from tkinter import Tk, Text, filedialog, Button, Menubutton, Menu, IntVar

# Sets the tkinter window to render in high res
ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = Tk("Basic Text Editor")
root.wm_title("Basic Text Editor")

text = Text(root)
text.grid()


def save_as(event=None):
    global text
    typed_text = text.get("1.0", "end-1c")
    if typed_text == "":
        return
    save_loc = filedialog.asksaveasfilename()
    if save_loc == "":
        return
    my_file = open(save_loc, "w+")
    my_file.write(typed_text)
    my_file.close()


button = Button(root, text="Save", command=save_as)
button.grid()
root.bind('<Control-s>', save_as)

root.mainloop()
