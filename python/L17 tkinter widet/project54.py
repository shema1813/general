import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def show_message():
    messagebox.showinfo("Photo Album", "Welcome to the Photo Album!")

def show_details():
    details_window = tk.Toplevel(root)
    details_window.title("Photo Details")
    details_window.geometry("300x200")

    tk.Label(details_window,
             text="Photo Information",
             font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(details_window, text="Title: Nature").pack(pady=5)
    tk.Label(details_window, text="Photographer: Your Name").pack(pady=5)
    tk.Label(details_window, text="Location: Local Park").pack(pady=5)

    tk.Button(details_window,
              text="Close",
              command=details_window.destroy).pack(pady=15)

root = tk.Tk()
root.title("Simple Photo Album")
root.geometry("500x500")

# Load Image
image = Image.open("python/L17 tkinter widet/image.png")     
image = image.resize((300, 250))

photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack(pady=20)

message_button = tk.Button(root,
                           text="Show Message",
                           command=show_message)

message_button.pack(pady=5)

details_button = tk.Button(root,
                           text="Photo Details",
                           command=show_details)

details_button.pack(pady=5)

exit_button = tk.Button(root,
                        text="Exit",
                        command=root.destroy)

exit_button.pack(pady=20)

root.mainloop()