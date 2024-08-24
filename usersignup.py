from tkinter import *
from tkinter import messagebox
from linklist import *
from functools import partial
from cutomerclass import *
import os
from booking_win2 import run2


# Paths change according to system
path = os.path.join(".", "Front end\\data", "id_data.txt")
path1 = os.path.join(".", "Front end\\data", "data.txt")
path2 = os.path.join(".", "Front end\\data", "id_data.txt")

with open(path, "r") as file:
    for id in file:
        if id != "\n":
            identity = int(id)


def run1():
    global path1, path2
    # Data Storage!
    data = LinkedList()

    def signup(name, phno, mail, pwd):
        global identity
        ph_no_data = phno.get()
        mail_data = mail.get()
        name_data = name.get()
        password = pwd.get()
        if (check_qty(ph_no_data, mail_data, name_data, password)):
            customer = Customer(name_data, ph_no_data,
                                mail_data, password, identity)
            check_user(customer)
            identity += 1

            details = add_data(customer)

            with open(path1, "a") as file:
                file.write(details)

            with open(path2, "a") as file:
                file.write("\n")
                file.write(str(identity))

            win1.destroy()
            run2(customer)

    def add_data(customer):
        data.append(customer)
        string = ""
        cust = data._head
        while cust is not None:
            string += cust._item.attributes() + "\n"
            cust = cust._next
        return string

    # Main Code!
    win1 = Tk()
    win1.title("User Signup Portal")
    win1.geometry("700x400")

    namelabel = Label(win1, text="Username :", font=(
        "Segoe UI bold", 14)).grid(row=0, column=0, padx=5, pady=10)
    name = StringVar()
    nameentry = Entry(win1, textvariable=name, font=("Verdana", 13)).grid(
        row=0, column=1, padx=5, pady=10)

    phnolabel = Label(win1, text="Phone Number :", font=("Segoe UI bold", 14)).grid(
        row=1, column=0, padx=5, pady=10
    )
    phno = StringVar()
    phnoentry = Entry(win1, textvariable=phno, font=("Verdana", 13)).grid(
        row=1, column=1, padx=5, pady=10)

    maillabel = Label(win1, text="Email :", font=("Segoe UI bold", 14)).grid(
        row=2, column=0, padx=5, pady=10)
    mail_id = StringVar()
    mailentry = Entry(win1, textvariable=mail_id, font=("Verdana", 13)).grid(
        row=2, column=1, padx=5, pady=10)

    passlabel = Label(win1, text="Password :", font=(
        "Segoe UI bold", 14)).grid(row=3, column=0, padx=5, pady=10)
    pwd = StringVar()
    pwdentry = Entry(win1, textvariable=pwd, font=("Verdana", 13)).grid(
        row=3, column=1, padx=5, pady=10)

    signup = partial(signup, name, phno, mail_id, pwd)
    logbutton = Button(win1, text="Signup", command=signup,
                       font=("Segoe UI bold", 14), fg="white", bg="green")
    logbutton.grid(row=5, column=1, padx=5, pady=10)

    win1.mainloop()

    # Running of second window!
