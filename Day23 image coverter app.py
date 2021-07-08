import tkinter as imageConverter
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root = imageConverter.Tk()

canvas1 = imageConverter.Canvas(root, width=600, height=550, bg='grey', relief='raised')
canvas1.pack()

label1 = imageConverter.Label(root, text='Basic Image converter App', bg='#C0C0C0',fg='black')
label1.config(font=('avenir', 20))
canvas1.create_window(300, 80, window=label1)


def getJPEG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browse = imageConverter.Button(text="      Browse   ", command=getJPEG, bg='#C0C0C0', fg='black',
                               font=('avenir', 12, 'bold'))
canvas1.create_window(300, 180, window=browse)


def convertToPNG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)


png = imageConverter.Button(text='Convert JPEG to PNG', command=convertToPNG, bg='#C0C0C0', fg='black',
                            font=('avenir', 12, 'bold'))
canvas1.create_window(300, 260, window=png)

root.mainloop()