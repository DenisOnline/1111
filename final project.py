import tkinter as tk

def fun1():
    new_windows = tk.Tk()
    new_windows.geometry("500x350")
    new_windows.resizable(False, False)

def fun2():
    new_windows = tk.Tk()
    new_windows.geometry("500x350")
    new_windows.resizable(False, False)

def fun3():
    new_windows = tk.Tk()
    new_windows.geometry("500x350")
    new_windows.resizable(False, False)
def file_exit():
    root.destroy()

root = tk.Tk()
root.geometry("600x400+500+400")
root.title("Magician's diary")
root.iconbitmap("Note.ico")
root.minsize(200, 100)
root.maxsize(1920, 1080)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label='Ваша функция 1', command=fun1)
file_menu.add_command(label='Ваша функция 2', command=fun2)
file_menu.add_command(label='Ваша функция 3', command=fun3)
file_menu.add_command(label='Выход', command=file_exit)
menu.add_cascade(label='File', menu=file_menu)

root.mainloop()