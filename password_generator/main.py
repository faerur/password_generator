from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letters_choice = [random.choice(letters) for char in range(nr_letters)]

    numbers_choice = [random.choice(numbers) for _ in range(nr_symbols)]

    symbols_choice = [random.choice(symbols) for i in range(nr_numbers)]

    password_list = letters_choice + numbers_choice + symbols_choice

    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += char

    password_answer.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = web_answer.get()
    email = user_data_answer.get()
    password = password_answer.get()
    new_data = {
        site: {
            "e-mail": email,
            "password": password
        }
    }

    if len(password) == 0 or len(site) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="You mustn't leave this field empty")

    else:
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)
                web_answer.delete(0, END)

        finally:
            user_data_answer.delete(0, END)
            password_answer.delete(0, END)
# ---------------------------- FINDER ------------------------------- #
def find_password():
    received = web_answer.get()
    try:
        with open(file="data.json", mode="r") as file:
            match = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Not Found", message="No Data File Found")

    else:
        if received in match:
            site = match[received]
            messagebox.showinfo(title="Data", message=f"E-mail: {site['e-mail']}\nPassword: {site['password']}")
            print(match[received])
        else:
            messagebox.showinfo(message="No details for the website found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(width=220, height=220, padx=20, pady=20)

canvas = Canvas(width=200, height=200,)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)


web = Label(text="Website:", anchor="e", justify="right")
web.grid(row=1, column=0)

web_answer = Entry(width=21)
web_answer.grid(row=1, column=1, sticky="EW")

user_data = Label(text="Email/Username: ", justify="right")
user_data.grid(row=2, column=0)

user_data_answer = Entry(width=35)
user_data_answer.grid(row=2, column=1, columnspan=2, sticky="EW")

password_text = Label(text="Password:", anchor="e")
password_text.grid(row=3, column=0, columnspan=1)

password_answer = Entry(width=21)
password_answer.grid(row=3, column=1, sticky="EW")

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()