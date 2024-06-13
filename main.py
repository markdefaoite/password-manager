from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it OK to save? ')
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.config(justify="right")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry()
website_entry.config(width=40)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry()
email_entry.config(width=40)
email_entry.insert(0, "Jane.Doe@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry()
password_entry.config(width=22)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", justify="left")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.config(width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
