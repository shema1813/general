from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title('my photo album')
window.geometry('400x420')

#Part 2
title = Label(window, text='My Photo Album', fg='white', bg='purple', width=40)
title.pack(pady=10)
img_file = Image.open('python/L17 tkinter widet/image.png')
img_file = img_file.resize((300,180))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=5)

#part3
def show_message():
    messagebox.askretrycancel('Great!', 'You clicked the photo!')
msg_btn = Button(window, text='click to react', bg='blue', fg='white', command=show_message)
msg_btn.pack(pady=5)

#part4
def show_details():
    top = Toplevel()
    top.title('Photo Details')
    top.geometry('200x120')
    info = Label(top, text='Taken on: 1 June 2025')
    info.pack(pady=10)
    place = Label(top, text='Location: My Garden')
    place.pack()
    top.mainloop()
details_btn = Button(window, text='See details', bg='green', fg='white', command=show_details)
details_btn.pack(pady=5)

#part5
window.mainloop()