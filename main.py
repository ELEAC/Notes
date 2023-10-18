import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

# Create the main application window
root = tk.Tk()
root.title("Notepad")

# Text widget for editing
text = tk.Text(root, wrap=tk.WORD)
text.pack(expand=True, fill="both")

# Functions for file menu
def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete("1.0", tk.END)
            text.insert("1.0", file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get("1.0", tk.END))

# Functions for edit menu
def undo():
    text.edit_undo()

def redo():
    text.edit_redo()

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def delete():
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)

def select_all():
    text.tag_add(tk.SEL, "1.0", tk.END)
    text.mark_set(tk.INSERT, "1.0")
    text.see(tk.INSERT)

def find():
    find_text = simpledialog.askstring("Find", "Find what:")
    if find_text:
        start = text.search(find_text, tk.INSERT, stopindex=tk.END)
        if start:
            text.tag_remove(tk.SEL, "1.0", tk.END)
            end = f"{start}+{len(find_text)}c"
            text.tag_add(tk.SEL, start, end)
            text.mark_set(tk.INSERT, end)
            text.see(tk.INSERT)
        else:
            messagebox.showinfo("Notepad", "Text not found")

# Functions for view menu
def zoom_in():
    text.zoom(True)

def zoom_out():
    text.zoom(False)

# Functions for setting menu
def set_font_family():
    font_family = simpledialog.askstring("Font Family", "Enter font family:")
    if font_family:
        text.configure(font=(font_family, text.cget("font")[1]))

def set_font_style():
    font_style = simpledialog.askstring("Font Style", "Enter font style:")
    if font_style:
        text.configure(font=(text.cget("font")[0], font_style))

def set_font_size():
    font_size = simpledialog.askinteger("Font Size", "Enter font size:")
    if font_size:
        text.configure(font=(text.cget("font")[0], font_size))

# Create menus
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Delete", command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)
edit_menu.add_command(label="Find", command=find)

view_menu = tk.Menu(menu)
menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom In", command=zoom_in)
view_menu.add_command(label="Zoom Out", command=zoom_out)

setting_menu = tk.Menu(menu)
menu.add_cascade(label="Settings", menu=setting_menu)
setting_menu.add_command(label="Set Font Family", command=set_font_family)
setting_menu.add_command(label="Set Font Style", command=set_font_style)
setting_menu.add_command(label="Set Font Size", command=set_font_size)

root.mainloop()
