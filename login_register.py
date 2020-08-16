from tkinter import *
import os

import home_new


def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def login_success():
    screen.destroy()
    # screen2.destroy()
    home_new.main()

def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password error")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error!", fg="green", font=("calibri", 11)).pack()
    Button(screen4, text = "OK", command= delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("user not found")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found!", fg="green", font=("calibri", 11)).pack()
    Button(screen5, text = "OK", command= delete4).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    # filename = os.path.join('/users',username_info+".txt")
    file = open('users/'+username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text="Registration Success!",fg="green",font=("calibri",11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir('/Users/hilabh/Documents/final_project/users')
    if username1 in list_of_files:
        file1 = open('users/'+username1,"r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()
    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1,text="Please enter details below").pack()
    Label(screen1,text="Username * ").pack()
    Label(screen1, text="").pack()
    username_entry = Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password * ").pack()
    password_entry = Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10,height=1,command=register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Registry 1.0")
    Label(text="Registry 1.0",bg="grey", width="300", height="2", font=("calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login", width="30", height="2",command=login).pack()
    Label(text="").pack()
    Button(text="Register", width="30", height="2",command=register).pack()

    screen.mainloop()

main_screen()