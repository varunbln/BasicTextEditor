from tkinter import filedialog


def save(editor_window):
    typed_text = editor_window.text.get("1.0", "end-1c")
    if typed_text == "":
        return
    save_loc = editor_window.file_name
    if save_loc is None:
        save_loc = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("All Files (*.*)", '*.*')], title="Save File")
    if save_loc == "":
        return
    my_file = open(save_loc, "w+")
    my_file.write(typed_text)
    my_file.close()