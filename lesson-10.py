# import re
#
# minyons_1 = "minyonys Bob minyOnys Bob mInyonys Bob"
# minyons_2 = "minyoNys minynyS Bob minYonys"
# minyons_3 = "Bob"
# minyons_4 = "Bob Kevin"
#
# bob = re.compile("Bob")
# print(bob.search(minyons_1))
# print(bob.search(minyons_2))
# for _ in bob.finditer(minyons_1):
#     print(f"match1 - {_}")
# for _ in bob.finditer(minyons_2):
#     print(f"match2 - {_}")
# print("\n", bob.findall(minyons_1))
# print(bob.findall(minyons_2))
# minyons_with_kevin = bob.sub("Kevin", minyons_1)
# print(minyons_1)
# print(minyons_with_kevin)
# print(bob.split(minyons_1))
# print(bob.fullmatch(minyons_3))
# print(bob.fullmatch(minyons_4))

import re
import tkinter as tk

login_pattern = re.compile(r"\w{3,20}@[a-z]{2,10}.[a-z]{2,6}$")
password_pattern = re.compile(r"\w{8,16}$")

root = tk.Tk()
root.geometry("400x300")
root.resizable(False, False)


def logining():
    login = login_entry.get()
    password = password_entry.get()
    if login_pattern.search(login):
        if password_pattern.search(password):
            login_entry.config(bg="green")
            password_entry.config(bg="green")
        else:
            login_entry.config(bg="red")
            password_entry.config(bg="red")
    else:
        login_entry.config(bg="red")
        password_entry.config(bg="red")


login_label = tk.Label(root, text="Login", font=("Arial", 14), padx=50)
password_label = tk.Label(root, text="Password", font=("Arial", 14), padx=50)
login_entry = tk.Entry(root, font=("Arial", 12), width=20)
password_entry = tk.Entry(root, font=("Arial", 12), width=20)

login_button = tk.Button(root, text="LOGIN", font=("Arial", 16), width=12, command=logining)

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=250)
root.grid_rowconfigure(0, minsize=90)
root.grid_rowconfigure(1, minsize=90)
login_button.grid(columnspan=2)
login_label.grid(column=0, row=0, sticky="w")
password_label.grid(column=0, row=1, sticky="w")
login_entry.grid(column=1, row=0, sticky="w")
password_entry.grid(column=1, row=1, sticky="w")
login_button.grid(column=0, row=2)

root.mainloop()
