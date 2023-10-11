from tkinter import *
from tkinter import messagebox
import random as rdm
import tkinter
import sqlite3
import math
import tkinter.messagebox
import random
from tkinter import filedialog


def on_closing():
    if messagebox.askokcancel("hhg"):
        tk.destroy()


tk = Tk()
tk.title("добро пожаловать")
tk.geometry("250x200")

c = Canvas(tk, width=600, height=600, bg="Red", highlightthickness=0)
c.pack
tk.configure(bg='blue')

def start_window_1():
    n = Toplevel(tk)
    n = Tk()
    n.title("METANIT.COM")
    n.geometry("250x200")
    root = tkinter.Tk()
    root.minsize(350, 260)
    root.title(' ')
    root.configure(bg="gray")
    tk.configure(bg='red')
    number = random.randint(1, 20)

    def say_hello():
        print('hello,world!')

    def send_low():
        tkinter.messagebox.showinfo("messagebox", "Your guess is too low.")

    def check_num():
        guess = text_guess.get()
        guess = int(guess)
        if guess > number:
            tkinter.messagebox.showinfo("много", "много")
        if guess < number:
            tkinter.messagebox.showinfo("мало", "мало")
        if guess == number:
            tkinter.messagebox.showinfo("победа", "победа")

    def btn_confirm():
        myName = text_name.get()
        tkinter.messagebox.showinfo(" ", ' ' + myName + ',угадай число от 1 до 20')

    label = tkinter.Label(root, text="игра")
    label.pack()
    label_name = tkinter.Label(root, text="напиши свое имя")
    label_name.place(x=10, y=60)
    text_name = tkinter.Entry(root, width=20)
    text_name.place(x=10, y=90)
    btnOK = tkinter.Button(root, text="OK", command=btn_confirm)
    btnOK.place(x=200, y=90, height=28)

    label_guess = tkinter.Label(root, text='число:')
    label_guess.place(x=10, y=150)
    text_guess = tkinter.Entry(root, width=10)
    text_guess.place(x=90, y=150)
    btnCheck = tkinter.Button(root, text='ответить', command=check_num)
    btnCheck.place(x=200, y=150, width=45, height=28)

    root.mainloop()


btn = Button(tk, text="угадай число", command=start_window_1)
btn.place(x=250, y=200)


def start_window_2():
    class Main(Frame):
        def __init__(self, root):
            super(Main, self).__init__(root)
            self.startUI()

        def startUI(self):
            btn = Button(root, text="Камень", font=("Times New Roman", 15),
                         command=lambda x=1: self.btn_click(x))
            btn2 = Button(root, text="Ножницы", font=("Times New Roman", 15),
                          command=lambda x=2: self.btn_click(x))
            btn3 = Button(root, text="Бумага", font=("Times New Roman", 15),
                          command=lambda x=3: self.btn_click(x))

            btn.place(x=10, y=100, width=120, height=50)
            btn2.place(x=155, y=100, width=120, height=50)
            btn3.place(x=300, y=100, width=120, height=50)

            self.lbl = Label(root, text="Начало игры!", bg="#FFF", font=("Times New Roman", 21, "bold"))
            self.lbl.place(x=150, y=25)

            self.win = self.drow = self.lose = 0

            self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13),
                              text=f"Побед: {self.win}\nПроигрышей:"
                                   f" {self.lose}\nНичей: {self.drow}",
                              bg="#FFF")
            self.lbl2.place(x=5, y=5)

        def btn_click(self, choise):
            comp_choise = rdm.randint(1, 3)

            if choise == comp_choise:
                self.drow += 1
                self.lbl.configure(text="Ничья=")
            elif choise == 1 and comp_choise == 2 \
                    or choise == 2 and comp_choise == 3 \
                    or choise == 3 and comp_choise == 1:
                self.win += 1
                self.lbl.configure(text="Победа+")
            else:
                self.lose += 1
                self.lbl.configure(text="Проигрыш-")

            self.lbl2.configure(text=f"Победа: {self.win}\nПроигрыш:"
                                     f" {self.lose}\nНичья: {self.drow}")

            del comp_choise

    if __name__ == '__main__':
        root = Tk()
        root.geometry("430x160+200+200")
        root.title("Камень, ножницы, бумага")
        root.resizable(False, False)
        root["bg"] = "#FFF"
        app = Main(root)
        app.pack()
        root.configure(bg="purple")
        root.mainloop()
        tk.configure(bg='green')

btn2 = Button(tk, text="камень ножницы бумага", command=start_window_2)
btn2.place(x=250, y=240)


def start_window_3():
    import tkinter as tk

    root = tk.Tk()
    root.title("Простое приложение для заметок")
    root.geometry("400x400")
    root.configure(bg="light blue")

    notes_listbox = tk.Listbox(root)
    notes_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
    note_entry = tk.Entry(root, width=50)
    note_entry.pack(pady=20, padx=20)

    def add_note():
        note = note_entry.get()
        if note:
            notes_listbox.insert(tk.END, note)
            note_entry.delete(0, tk.END)

    def delete_note():
        try:
            notes_listbox.delete(notes_listbox.curselection())
        except:
            pass

    add_button = tk.Button(root, text="Добавить заметку", command=add_note)
    add_button.pack(pady=10, padx=20)
    delete_button = tk.Button(root, text="Удалить заметку", command=delete_note)
    delete_button.pack(pady=10, padx=20)
    root.mainloop()


n = Button(tk, text="заметки", command=start_window_3)
n.place(x=250, y=275)

tk.mainloop()