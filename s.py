from tkinter import *

def btn2Click():
    username = txtUsername.get()
    password = txtPassword.get()

    myfile = open("username.txt", "a")
    str1 = "\n" + username + "-" + password + "-end"
    myfile.write(str1)

def show_menu():
    menu_window = Tk()
    menu_window.title("choose your meal")

    with open("restaurants.txt", "r") as menu_file:
        menu_data = menu_file.readlines()

    def show_prices(item):
        menu_window.destroy()

        order_window = Tk()
        order_window.title("total price")

        for line in menu_data:
            if item in line:
                price = line.split("-")[1].strip()
                Label(order_window, text=f" total: {price}").pack()



        order_window.mainloop()

    for line in menu_data:
        item = line.split("-")[0].strip()
        Button(menu_window, text=item, command=lambda i=item: show_prices(i)).pack()

    menu_window.mainloop()

def btn1Click():
    username = txtUsername.get()
    password = txtPassword.get()

    myfile = open("username.txt", "r")
    alldata = myfile.readlines()

    for x in alldata:
        linedata = x.split("-")
        if username == linedata[0] and password == linedata[1]:
            lblOutput.config(text="Pass")
            show_menu()
            break
        else:
            lblOutput.config(text="Fail")


soso = Tk()

lblUsername = Label(soso, text="Username")
lblPassword = Label(soso, text="Password")
lblOutput = Label(soso, text="......")

txtUsername = Entry(soso)
txtPassword = Entry(soso, show="*")

btnLogin = Button(soso, text="Login", command=btn1Click)
btnSignup = Button(soso, text="Signup", command=btn2Click)

lblUsername.pack()
txtUsername.pack()

lblPassword.pack()
txtPassword.pack()

btnLogin.pack()
lblOutput.pack()
btnSignup.pack()

soso.mainloop()
