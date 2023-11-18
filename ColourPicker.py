from tkinter import *

RGB = [0, 0, 0]

def rgb_to_hex(r, g, b):
    r = int(r)
    g = int(g)
    b = int(b)
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_color

def RGBList(red_value, green_value, blue_value):
    global RGB
    RGB = [red_value, green_value, blue_value]
    hex_code = rgb_to_hex(RGB[0], RGB[1], RGB[2])
    colour.config(bg=hex_code, text="Hex Code: " + rgb_to_hex(RGB[0], RGB[1], RGB[2]))

window = Tk()
window.geometry("200x300")
window.title("Colour Picker")

title = Label(text="Colour Picker", font="Helvetica 12 underline")
title.pack()

redLabel = Label(text="RED", font="Helvetica 12 underline", fg='#ff1100')
redLabel.pack()
red = Scale(window, from_=0, to=255, orient=HORIZONTAL, command=lambda value: RGBList(value, green.get(), blue.get()))
red.pack()

greenLabel = Label(text="Green", font="Helvetica 12 underline", fg='#25cc46')
greenLabel.pack()
green = Scale(window, from_=0, to=255, orient=HORIZONTAL, command=lambda value: RGBList(red.get(), value, blue.get()))
green.pack()

blueLabel = Label(text="BLUE", font="Helvetica 12 underline", fg='#0080ff')
blueLabel.pack()
blue = Scale(window, from_=0, to=255, orient=HORIZONTAL, command=lambda value: RGBList(red.get(), green.get(), value))
blue.pack()

colour = Label(window, font="Helvetica 9 bold",text="Hex Code: " + rgb_to_hex(RGB[0], RGB[1], RGB[2]),fg="#ffffff", width=17, height=3, relief="groove")
colour.pack(pady=10)


window.mainloop()