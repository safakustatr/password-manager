from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_list + number_list + symbol_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the information you entered: \n"
                                                              f"Email/Username: {username}\n"
                                                              f"Password: {password}\nWould you like to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_label.config(padx=10, pady=5)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_label.config(padx=10, pady=5)

username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, "example@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_label.config(padx=10, pady=5)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, sticky="W")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="E")

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()