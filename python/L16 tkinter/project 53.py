from tkinter import *
from tkinter import messagebox

def show_bio():
    name = name_entry.get()
    age = age_entry.get()
    hobby = hobby_entry.get()
    about = about_text.get("1.0", END).strip()

    bio = f"""Personal Bio

Name: {name}
Age: {age}
Hobby: {hobby}

About Me:
{about}
"""

    messagebox.showinfo("My Personal Bio", bio)

window = Tk()
window.title("Personal Bio Form")
window.geometry("400x430")
window.configure(bg="lightblue")

title = Label(window, text="Personal Bio Form",
              fg="white", bg="navy", width=40)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

name_label = Label(window, text="Name", bg="lightblue", fg="navy")
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(window, bg="white", fg="darkblue", width=25)
name_entry.grid(row=1, column=1, padx=10, pady=5)

age_label = Label(window, text="Age", bg="lightblue", fg="navy")
age_label.grid(row=2, column=0, padx=10, pady=5)

age_entry = Entry(window, bg="white", fg="darkblue", width=25)
age_entry.grid(row=2, column=1, padx=10, pady=5)

hobby_label = Label(window, text="Hobby", bg="lightblue", fg="navy")
hobby_label.grid(row=3, column=0, padx=10, pady=5)

hobby_entry = Entry(window, bg="white", fg="darkblue", width=25)
hobby_entry.grid(row=3, column=1, padx=10, pady=5)

about_frame = Frame(window, relief=RAISED, borderwidth=3, bg="lightblue")
about_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

about_label = Label(about_frame, text="About Me:", bg="lightblue", fg="navy")
about_label.pack()

about_text = Text(about_frame, bg="white", fg="darkblue",
                  width=40, height=5)
about_text.pack()

submit = Button(window, text="Show My Bio",
                bg="navy", fg="white",
                width=20, command=show_bio)
submit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()


