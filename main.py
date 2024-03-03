from PIL import Image, ImageDraw, ImageFont
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter import IntVar



def open_file():
    global i
    file_path = askopenfile(mode='r', filetypes=[('Image Files', ['*jpeg', '*png'])])
    if file_path is not None:
        i = Image.open(file_path.name)

def place_text():
    global xy
    try:
        x, y = i.size[0], i.size[1]
    except NameError:
        messagebox.showerror(title="Error", message="Choose file before!")
    else:
        if var.get() == 1:
            xy = (70, 70)
        elif var.get() == 2:
            xy = (x-70, 70)
        elif var.get() == 3:
            xy = (70, y-70)
        elif var.get() == 4:
            xy = (x-70, y-70)
        else:
            messagebox.showerror(title="Error", message="Choose the place of text!")

def convert():
    try:
        im = ImageDraw.Draw(i)
    except NameError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        font_name = combo.get()
        font = ImageFont.truetype(f"{font_name.lower()}.ttf", 35)
        im.text(xy=xy, text=get_text.get(), font=font)
        i.show()


window = Tk()
var = IntVar()

title = ttk.Label(text="WATERMARK", font=("", 61), padding=50)
title.grid(column=0, row=0, columnspan=10)


file_button = ttk.Button(
    window,
    text='Choose File',
    command=open_file
    )
file_button.grid(row=2, column=3)

text = ttk.Label(text="Text: ", font=("", 15))
text.grid(row=3, column=0)

get_text = ttk.Entry(width=70)
get_text.grid(row=3, column=0, columnspan=10,padx=20,pady=20)
get_text.focus()

convert_button = ttk.Button(text="Convert",command=convert)
convert_button.grid(row=9, column=3)

radio_button1 = ttk.Radiobutton(text="TopLeft", variable=var, value=1, command=place_text)
radio_button1.grid(row=5,column=1)

radio_button2 = ttk.Radiobutton(text="TopRight", variable=var, value=2, command=place_text)
radio_button2.grid(row=5,column=3)

radio_button3 = ttk.Radiobutton(text="BottomLeft", variable=var, value=3, command=place_text)
radio_button3.grid(row=5,column=5)

radio_button4 = ttk.Radiobutton(text="BottomRight", variable=var, value=4, command=place_text)
radio_button4.grid(row=5,column=7)


combo = ttk.Combobox(values=["Arial", "Verdana", "Corbel", "Tahoma", "Cour"])
combo.grid(row=6,column=3,padx=20,pady=20)
combo.insert(0, "Arial")




window.mainloop()
