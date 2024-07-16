import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("400x400")
im = Image.open('Screenshot_20240716-135727-removebg-preview.png')
photo = ImageTk.PhotoImage(im)
root.wm_iconphoto(True, photo)
root.withdraw()
tkinter.messagebox.showwarning('Knock knock','How deep...?')



