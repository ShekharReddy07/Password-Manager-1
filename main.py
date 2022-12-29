from tkinter import *
from tkinter import messagebox 
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_symbols)]
    password_list += [random.choice(symbols) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += str(char)

    print(f"Your password is: {password}")
    pass_entry.insert(0, f"{password}")

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_text():
    if len(web_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.askretrycancel(title="title", message="All fields are not entered")
        return
    is_okay = messagebox.askokcancel(title="Title", message=f"are u okay with the entered data:\nEmail: {email_entry.get()}\nPassword: {pass_entry.get()}")
    if is_okay:
        with open("doc.txt", "a") as file:
            file.write(web_entry.get() + " | ")
            file.write(email_entry.get() + " | ")
            file.write(pass_entry.get() + "\n")
        web_entry.delete(0, END)
        pass_entry.delete(0, END)
    web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(220, 220)
window.config(padx=50, pady=50)

image_file = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image_file)
canvas.grid(column=1, row=0)

website_label = Label(window, text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(window, text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(window, text="Password:")
pass_label.grid(column=0, row=3)

web_entry = Entry(width=52)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "shekharreddy1888@gmail.com")

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)

gen_pass_button = Button(window, text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button = Button(window, text="Add", width=45, command=add_text)
add_button.grid(column=1, row=4, columnspan=2)















window.mainloop()