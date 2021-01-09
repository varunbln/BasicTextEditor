from tkinter import filedialog, END


def save(editor_window):
    typed_text = editor_window.text.get("1.0", "end-1c")
    if typed_text == "":
        return
    save_loc = editor_window.file_name
    if save_loc is None:
        save_loc = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("All Files (*.*)", '*.*')],
                                                title="Save File")
    if save_loc == "":
        return
    my_file = open(save_loc, "w+")
    my_file.write(typed_text)
    my_file.close()
    editor_window.file_name = save_loc


def open_file(editor_window):
    save(editor_window)
    file = filedialog.askopenfilename()
    my_file = open(file, "r")
    try:
        text = my_file.read()
    except:
        return
    editor_window.text.delete('1.0', END)
    editor_window.text.insert('1.0', text)
    editor_window.file_name = file


def new_and_save(editor_window):
    save(editor_window)
    editor_window.text.delete('1.0', END)
    editor_window.file_name = None
