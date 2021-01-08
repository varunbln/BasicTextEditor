import ctypes
from editor_window.EditorWindow import EditorWindow

# Sets the tkinter window to render in high res
ctypes.windll.shcore.SetProcessDpiAwareness(True)

editor_window = EditorWindow()
