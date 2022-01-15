#=== All Imports ===#

from tkinter import *
from tkinter import messagebox
from typing import Pattern
import random
from PIL import Image,ImageTk
from abc import ABC,abstractmethod
import tkinter as tk
from tkinter import ttk
from time import strftime
from datetime import date
# -------------------------- #

root = Tk()
root.title("Customer login Area")
root.geometry("1199x600+100+50")

username = StringVar()
userpassword = StringVar()
Reg_user_name = StringVar()
Reg_password = StringVar()
Reg_contact = StringVar()
forgot = StringVar()

#-- for checking valid phone number --#
def valid_phone(num):
    try:
        if num.strip().isdigit():
            return True
    except:
        return False

#-- for checking valid cnin number --#
def valid_cnic(num):
    try:
        if num.strip().isdigit():
            return True
    except:
        return False

class Login_page(ABC):
    @abstractmethod
    def login_frame(self):
        pass

    def Login(self):  # Method overriding in Login_customer class
        pass

class Login_customer(Login_page):
    def __init__(self,top=None):
        top.geometry("1299x700+30+20")
        top.title("Customer Login Area")
        top.resizable(0,0)
        self.root = top

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1299, height=700)

        #== Background Image ==#
        photo = Image.open("./images/customer login image.jpg")
        photo =photo.resize((1299,700),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image=photo)
        self.label.configure(image=self.img1)
    
    def login_frame(self):

        #=== Walmart label ===#
        self.label2 = Label(root,bg="dark slate gray")
        self.label2.configure(text="WALMART",font="Times 45 bold",fg="white")
        self.label2.place(x=230,y=65)

        #=== Login Frame ===#
        self.frame_login = Frame(root, bg="white")
        self.frame_login.place(x=150, y=150, height=400, width=520)

        #-- Login Title --#
        title = Label(self.frame_login, text="Login Here",font="Impact 33 bold",bg="white",
        fg="gray10").place(x=90,y=30)
        desc = Label(self.frame_login, text="Customer Login Area",font="Helvetica 14 bold italic",bg="white",
        fg="gray30").place(x=90,y=93)

        #-- Username label/Entry --#
        labl_user = Label(self.frame_login, text="Username*",font="Goudyoldstyle 14 bold",bg="white",
        fg="gray").place(x=90,y=140)
        self.name_txt = Entry(self.frame_login,font="timesnewroman 14",bg="lightgray",textvariable=username
        ).place(x=90,y=177,width=350,height=35)

        #-- Password Label/Entry --#
        labl_password = Label(self.frame_login, text="Password*",font="Goudyoldstyle 14 bold",bg="white",
        fg="gray").place(x=90,y=220)
        self.password_txt = Entry(self.frame_login,font="timesnewroman 14",bg="lightgray",textvariable=userpassword
        ,show="*").place(x=90,y=255,width=350,height=35)

        #-- Forgot password button --#
        forget_btn = Button(self.frame_login,text="Forgot password?",bg="white",font="timesnewroman 13",bd=0
        ,cursor="hand2",command=self.forgot_pass).place(x=180,y=305)

        #-- Register button --#
        register_btn = Button(self.frame_login,text="----Sing Up/Register----",bg="white",font="timesnewroman 13",bd=0
        ,cursor="hand2",command=self.register).place(x=160,y=335)

        #--login button --#
        login_btn = Button(self.root,text="Log In",bg="dark slate gray",fg="white",font="timesnewroman 14",bd=0
        ,cursor="hand2",padx=35,pady=3,command=self.Login).place(x=340,y=530)

    def Login(self, Event=None):
        user_name = username.get()
        user_password = userpassword.get()

        login = []
        with open("Customer login detail.txt","r") as f:
            for line in f:
                line = eval(line)
                login.append(line)

        
        if user_name == "" or user_password == "":
            messagebox.showerror("Error","Please provide complete detail")

        
        elif user_name != "" and user_password != "":
            log = False
            for data in login:
                user = data[0]
                password = data[1]
                
                if user_name == user and user_password == password:
                    messagebox.showinfo("Login Page", "The login is successful.")

                    #== Drawing Shopping  Window ==#
                    root.withdraw()
                    global customer
                    global page3
                    customer = Toplevel()
                    page3 = Shopping_page(customer)
                    page3.time()
                    customer.protocol("WM_DELETE_WINDOW", Exit)
                    log = True  # makes log true after backing from shopping window
                    customer.mainloop()
                else:
                    pass
                    
            if not log:
                messagebox.showerror("Error","Incorrect username or password")


            
    def forgot_pass(self):
        password_window = Toplevel()
        pass_lbl = Label(password_window)
        pass_lbl.place(relx=0, rely=0, width=500, height=300)
        password_window.title("Forgot Password")
        password_window.geometry("500x300+720+270")
        password_window.resizable(0,0)

        #== Forgot password background picture ==#
        pass_photo = Image.open("./images/forgot password.jpg")
        pass_photo = pass_photo.resize((500,300),Image.ANTIALIAS)
        pass_img = ImageTk.PhotoImage(image=pass_photo)
        pass_lbl.configure(image=pass_img)

        #== Walmart Label ==#
        wal_lbl = Label(password_window,text="WALMART",bg="goldenrod",fg="black",padx=30,font="Times 14")
        wal_lbl.place(x=230,y=50)

        #== Username Label ==#
        txt_labl = Label(password_window,text="Enter Username",fg="white",bg="gray10",
        font="Times 15 bold")
        txt_labl.place(x=190,y=100)

        #== Username Entry ==#
        forgot_entry = Entry(password_window,bg="light gray",font="timesnewroman 14",textvariable=forgot)
        forgot_entry.place(x=190, y=140, width=250, height=35)

        #== Submit Button ==#
        forgot_btn = Button(password_window,text="Submit",font="Helvetica 15",padx=30, pady=1, fg="black"
        ,bg="goldenrod",bd=0,cursor="hand2",command=self.new_password)
        forgot_btn.place(x=250,y=200, height=30)

        password_window.mainloop()

    def new_password(self):
        txt_forgot = forgot.get()
        empty = False
        
        if txt_forgot == "":
            messagebox.showerror("Error","Please enter username")
            empty = True
        
        elif empty == False:
            with open("Customer login detail.txt") as f:
                use = False
                for line in f:
                    line = eval(line)
                    #line = line.split(",")  #-- fetchng password and spliting by commas
                    if txt_forgot == line[0]:
                        messagebox.showinfo("Password","Your password is {}".format(line[1]))
                        use = True
                if use == False:    
                    messagebox.showerror("Error","This Username dosen't exist")
                
    def register(self):
        global register_window
        global page2

        #== Creating Register window ==#
        register_window = Toplevel()
        #-- Association --#
        page2 = Register_customer(register_window)
        page2.login_frame()

        register_window.mainloop()

def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit", parent = root)
    if sure:
        customer.destroy()
        root.destroy()
        

class Register_customer(Login_page):
    def __init__(self,top=None):
        top.geometry("550x580+720+100")
        top.resizable(0, 0)
        top.title("REGISTER Mode")
        self.reg = top

        #== Register Label ==#
        self.register_label = Label(top)
        self.register_label.place(relx=0, rely=0, width=550, height=580)

        #== Background Image ==#
        reg_photo = Image.open("./images/register.jpg")
        reg_photo = reg_photo.resize((550,580),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image=reg_photo)
        self.register_label.configure(image=self.img1)

    def login_frame(self):

        #-- Walmart Label --#
        self.walm_lbl = Label(self.reg,bg="gold")
        self.walm_lbl.configure(text="WALMART",font="Times 25 bold",fg="gray20")
        self.walm_lbl.place(x=75,y=25)

        #-- Name Label --#
        self.name_lbl = Label(self.reg,text="Enter Your Full Name*",bg="dark slate gray",fg="white"
        ,font="Goudyoldstyle 13")
        self.name_lbl.place(x=20, y=90)
        #-- Name Entry --#
        self.name_entry = Entry(self.reg,bg="light gray",font="timesnewroman 14")
        self.name_entry.place(x=20,y=122,width=200, height=33)

        #-- Username --#
        self.usname_lbl = Label(self.reg,text="Enter Username*",bg="dark slate gray",fg="white"
        ,font="Goudyoldstyle 13")
        self.usname_lbl.place(x=20, y=180)
        #-- userName Entry --#
        self.name_entry = Entry(self.reg,bg="light gray",font="timesnewroman 14",textvariable=Reg_user_name)
        self.name_entry.place(x=20,y=212,width=200, height=33)

        #-- Contact Label--#
        self.contact_lbl = Label(self.reg,text="Contact*",bg="dark slate gray",fg="white"
        ,font="Goudyoldstyle 13")
        self.contact_lbl.place(x=20, y=260)
        #-- Contact Entry --#
        self.contact_entry = Entry(self.reg,bg="light gray",font="timesnewroman 14",textvariable=Reg_contact)
        self.contact_entry.place(x=20,y=292,width=200, height=33)

        #-- Address Label --#
        self.email_lbl = Label(self.reg,text="Address*",bg="dark slate gray",fg="white"
        ,font="Goudyoldstyle 13")
        self.email_lbl.place(x=20, y=340)
        #-- Address Entry --#
        self.email_entry = Entry(self.reg,bg="light gray",font="timesnewroman 14")
        self.email_entry.place(x=20,y=372,width=200, height=33)

        #-- Password label --#
        self.pswd_lbl = Label(self.reg,text="Password*",bg="dark slate gray",fg="white"
        ,font="Goudyoldstyle 13")
        self.pswd_lbl.place(x=20, y=420)
        #-- Password Entry --#
        self.pswd_entry = Entry(self.reg,bg="light gray",font="timesnewroman 14",textvariable=Reg_password)
        self.pswd_entry.place(x=20,y=450,width=200, height=33)

        #-- Submit Button --#
        self.submit_btn = Button(self.reg,text="Submit",bg="gold",fg="gray20"
        ,font="Goudyoldstyle 15",bd=0,cursor="hand2",command=self.Submit)
        self.submit_btn.place(x=130, y=510)
    
    def Submit(self):
        reg_username = Reg_user_name.get()
        reg_password = Reg_password.get()

        if reg_username == "" or reg_password == "":
            messagebox.showerror("Error","Incomplete Information \nPlease fill it again")
        else:
            #-- Writing all details in file --#
            register = [reg_username,reg_password]
            with open("Customer login detail.txt","a") as f:
                f.write(str(register) + "\n")
            messagebox.showinfo("Registertion","Successfully Registered!! \
            \nUsername: {} \nPassword: {}".format(reg_username,reg_password))

            register_window.destroy()

class Shopping_page:
    def __init__(self, top=None):
        top.geometry("1299x700+30+20")
        top.resizable(0, 0)
        top.title("Shopping Area")

        self.label1 = Label(customer)
        self.label1.place(relx=0, rely=0, height=700, width=1299)

        #=== Background Image ===#
        photo = Image.open("./images/Shopping page.png")
        photo = photo.resize((1299,700),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image=photo)
        self.label1.configure(image=self.img1)

        #== Admin Label ==#
        self.message = Label(customer)
        self.message.place(relx=0.079, rely=0.070, width=78, height=25)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="black")
        self.message.configure(background="white")
        self.message.configure(text="""CUSTOMER""")
        self.message.configure(anchor="w")
 
        #== Clock ==#
        self.clock = Label(customer)
        self.clock.place(relx=0.87, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {poppins light} -size 12")
        self.clock.configure(relief="flat")
        self.clock.configure(background="white")

        #== Logout Button ==#
        self.logout_btn = Button(customer)
        self.logout_btn.place(relx=0.067, rely=0.123, width=61, height=18)
        self.logout_btn.configure(relief="flat")
        self.logout_btn.configure(text="LOGOUT")
        self.logout_btn.configure(overrelief="flat")
        self.logout_btn.configure(activebackground="gray20")
        self.logout_btn.configure(cursor="hand2")
        self.logout_btn.configure(bg="dark slate gray")
        self.logout_btn.configure(bd=0)
        self.logout_btn.configure(foreground="white")
        self.logout_btn.configure(font="-family {Poppins SemiBold} -size 10")
        self.logout_btn.configure(command=self.Logout)

        #== Add Product Cart Button ==#
        self.add_emp_btn = Button(customer)
        self.add_emp_btn.place(relx=0.064, rely=0.410, width=275, height=33)
        self.add_emp_btn.configure(relief="flat")
        self.add_emp_btn.configure(text="ADD TO CART")
        self.add_emp_btn.configure(overrelief="flat")
        self.add_emp_btn.configure(activebackground="gray20")
        self.add_emp_btn.configure(cursor="hand2")
        self.add_emp_btn.configure(bg="dark slate gray")
        self.add_emp_btn.configure(bd=0)
        self.add_emp_btn.configure(foreground="#ffffff")
        self.add_emp_btn.configure(font="-family {Poppins SemiBold} -size 14")
        self.add_emp_btn.configure(command=self.add_cart)

        #== View Cart Button ==#
        self.update_emp_btn = Button(customer)
        self.update_emp_btn.place(relx=0.064, rely=0.502, width=275, height=33)
        self.update_emp_btn.configure(relief="flat")
        self.update_emp_btn.configure(text="VIEW CART")
        self.update_emp_btn.configure(overrelief="flat")
        self.update_emp_btn.configure(activebackground="gray20")
        self.update_emp_btn.configure(cursor="hand2")
        self.update_emp_btn.configure(bg="dark slate gray")
        self.update_emp_btn.configure(bd=0)
        self.update_emp_btn.configure(foreground="#ffffff")
        self.update_emp_btn.configure(font="-family {Poppins SemiBold} -size 14")
        self.update_emp_btn.configure(command=self.View_cart)

        #== View shopping history Button ==#
        self.del_emp_btn = Button(customer)
        self.del_emp_btn.place(relx=0.064, rely=0.589, width=275, height=33)
        self.del_emp_btn.configure(relief="flat")
        self.del_emp_btn.configure(text="SHOPPING HISTORY")
        self.del_emp_btn.configure(overrelief="flat")
        self.del_emp_btn.configure(activebackground="gray20")
        self.del_emp_btn.configure(cursor="hand2")
        self.del_emp_btn.configure(bg="dark slate gray")
        self.del_emp_btn.configure(bd=0)
        self.del_emp_btn.configure(foreground="#ffffff")
        self.del_emp_btn.configure(font="-family {Poppins SemiBold} -size 14")
        self.del_emp_btn.configure(command=self.shopping_history)

        #== Scroll bar ==#
        self.scrollbary = Scrollbar(customer, orient=VERTICAL)

        #== Treeview Widget ==#
        self.tree = ttk.Treeview(customer)
        self.tree.place(relx=0.288, rely=0.245, width=859, height=473)
        self.tree.configure(
            yscrollcommand = self.scrollbary.set
        )
        self.tree.configure(selectmode="extended")
        self.tree.bind("<<TreeviewSelect>>", self.Tree_Select)

        #== Setting scrollbar to tree ==#
        self.scrollbary.configure(command=self.tree.yview)

        #== Placing scrollbar ==#
        self.scrollbary.place(relx=0.950, rely=0.244, width=22, height=473)

        #== Configuring Headings ==#
        self.tree.configure(
            columns=(
                "Product ID",
                "Name",
                "Category",
                "Sub-Category",
                "In Stock",
                "Price"
            )
        )

        style = ttk.Style()
        style.configure("Treeview.Heading", foreground = "dark slate gray", font="Times 12")

        #==  Setting Heading  ==#
        self.tree.heading("Product ID", text="Product ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Category", text="Category", anchor=W)
        self.tree.heading("Sub-Category", text="Sub-Category", anchor=W)
        self.tree.heading("In Stock", text="In Stock", anchor=W)
        self.tree.heading("Price", text="Price", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=95)
        self.tree.column("#2", stretch=NO, minwidth=0, width=230)
        self.tree.column("#3", stretch=NO, minwidth=0, width=145)
        self.tree.column("#4", stretch=NO, minwidth=0, width=145)
        self.tree.column("#5", stretch=NO, minwidth=0, width=120)
        self.tree.column("#6", stretch=NO, minwidth=0, width=120)

        self.Displaydata()

    def Displaydata(self):
        data = []
        with open("Product data.txt","r") as f:
            for line in f:
                line = eval(line)
                data.append(line)

        for record in data:
            #-- Inserting records in treeview --#
            self.tree.insert("","end", values=(
                record[0],record[1],record[2],record[3],record[4],record[5]))

    select = []
    def Tree_Select(self, Event):
        self.select.clear()
        for i in self.tree.selection():
            if i not in self.select:
                self.select.append(i)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            customer.destroy()
            root.deiconify()

    def add_cart(self):
        select = self.tree.selection()  #-- give id of selected item
        index = self.tree.focus()
        index = index[3:]

        if len(select) != 0:
            data = []
            with open("Product data.txt","r") as f:
                for line in f:
                    line = eval(line)
                    data.append(line)
            
            data_dic = {
                    
                    "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,
                    "N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35
                } 

            try:
                lst = data[int(index) - 1]  #-- deleting from file

            except:
                del data[data_dic[index]-1]   #-- deleting from file if index>9

            select_item_lst = [userpassword.get(),lst[0],lst[1],lst[2],lst[3],lst[5]]
            with open("Cart data.txt","a") as f:
                f.write(str(select_item_lst) + "\n")
            
            messagebox.showinfo("confirmation","Product added in cart successfully!!", parent = customer)

        else:
            messagebox.showerror("Error","Please select product to add in cart", parent = customer)



    def View_cart(self):
        global cart
        cart = Toplevel()
        page6 = Cart(cart)
        page6.time()
        cart.protocol("WM_DELETE_WINDOW", self.exit_cart)
        cart.mainloop()

    def exit_cart(self):
        cart.destroy()

    def shopping_history(self):
        global history
        history = Toplevel()
        shop_history = Shopping_History(history)
        history.mainloop()


class Shopping_History:
    def __init__(self, top=None):
        top.geometry("790x450")
        top.resizable(0, 0)
        top.title("Shopping History")

        #== Label for BG ==#
        self.lbl = Label(history)
        self.lbl.place(relx=0, rely=0, width=790, height=450)

        #=== Background Image ===#
        photo1 = Image.open("./images/Shopping History.png")
        photo1 = photo1.resize((790,450),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(image=photo1)
        self.lbl.configure(image=self.img)

        #== Scroll bar ==#
        self.scrollbary = Scrollbar(history, orient=VERTICAL)

        #== Treeview Widget ==#
        self.tree = ttk.Treeview(history)
        self.tree.place(relx=0.004, rely=0.270, width=765, height=325)
        self.tree.configure(
            yscrollcommand = self.scrollbary.set
        )
        self.tree.configure(selectmode="extended")

        #== Setting scrollbar to tree ==#
        self.scrollbary.configure(command=self.tree.yview)

        #== Placing scrollbar ==#
        self.scrollbary.place(relx=0.975, rely=0.270, width=22, height=325)

        #== Configuring Headings ==#
        self.tree.configure(
            columns=(
                "Product Name",
                "Category",
                "Price",
                "Date"
            )
        )

        #==  Setting Heading  ==#
        self.tree.heading("Product Name", text="Product Name", anchor=W)
        self.tree.heading("Category", text="Category", anchor=W)
        self.tree.heading("Price", text="Price", anchor=W)
        self.tree.heading("Date", text="Date", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=230)
        self.tree.column("#2", stretch=NO, minwidth=0, width=230)
        self.tree.column("#3", stretch=NO, minwidth=0, width=150)
        self.tree.column("#4", stretch=NO, minwidth=0, width=150)

        self.Display_data()

    def Display_data(self):
        try:
            data = []
            with open("Shopping history data.txt","r") as f:
                for line in f:
                    line = eval(line)
                    data.append(line)
            #print(data)
            
            for record in data:
                if record[0] == userpassword.get():
                    #-- inserting data in treeview --#
                    self.tree.insert("","end", values=(
                        record[1],record[2],record[3],record[4]))
        except:
            messagebox.showinfo("Empty","Your cart is empty...!! \nPlease add items in cart first")


class Cart(Shopping_page):
    def __init__(self, top=None):
        top.geometry("899x500+190+150")
        top.resizable(0, 0)
        top.title("Cart")

        #=== Background Image ===#
        self.label1 = Label(cart)
        self.label1.place(relx=0, rely=0, height=500, width=899)
        photo = Image.open("./images/cart.png")
        photo = photo.resize((899,500),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image=photo)
        self.label1.configure(image=self.img1)

        #== Back Button ==#
        self.logout_btn = Button(cart)
        self.logout_btn.place(relx=0.059, rely=0.146, width=50, height=18)
        self.logout_btn.configure(relief="flat")
        self.logout_btn.configure(text="BACK")
        self.logout_btn.configure(overrelief="flat")
        self.logout_btn.configure(activebackground="gray20")
        self.logout_btn.configure(cursor="hand2")
        self.logout_btn.configure(bg="dark slate gray")
        self.logout_btn.configure(bd=0)
        self.logout_btn.configure(foreground="white")
        self.logout_btn.configure(font="-family {Poppins SemiBold} -size 10")
        self.logout_btn.configure(command=self.Back)

        #== Delete product Button ==#
        self.add_emp_btn = Button(cart)
        self.add_emp_btn.place(relx=0.075, rely=0.410, width=160, height=28)
        self.add_emp_btn.configure(relief="flat")
        self.add_emp_btn.configure(text="DELETE PRODUCT")
        self.add_emp_btn.configure(overrelief="flat")
        self.add_emp_btn.configure(activebackground="gray20")
        self.add_emp_btn.configure(cursor="hand2")
        self.add_emp_btn.configure(bg="dark slate gray")
        self.add_emp_btn.configure(bd=0)
        self.add_emp_btn.configure(foreground="#ffffff")
        self.add_emp_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.add_emp_btn.configure(command=self.delete_item)

        #== Checkout Button ==#
        self.add_emp_btn = Button(cart)
        self.add_emp_btn.place(relx=0.075, rely=0.510, width=160, height=28)
        self.add_emp_btn.configure(relief="flat")
        self.add_emp_btn.configure(text="CHECK OUT")
        self.add_emp_btn.configure(overrelief="flat")
        self.add_emp_btn.configure(activebackground="gray20")
        self.add_emp_btn.configure(cursor="hand2")
        self.add_emp_btn.configure(bg="dark slate gray")
        self.add_emp_btn.configure(bd=0)
        self.add_emp_btn.configure(foreground="#ffffff")
        self.add_emp_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.add_emp_btn.configure(command=self.check_out)

        #== Clock ==#
        self.clock = Label(cart)
        self.clock.place(relx=0.82, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {poppins light} -size 12")
        self.clock.configure(relief="flat")
        self.clock.configure(background="white")

        #== Scroll bar ==#
        self.scrollbary = Scrollbar(cart, orient=VERTICAL)

        #== Treeview Widget ==#
        self.tree = ttk.Treeview(cart)
        self.tree.place(relx=0.267, rely=0.274, width=600, height=292)
        self.tree.configure(
            yscrollcommand = self.scrollbary.set
        )
        self.tree.configure(selectmode="extended")
        self.tree.bind("<<TreeviewSelect>>", self.tree_select)

        #== Setting scrollbar to tree ==#
        self.scrollbary.configure(command=self.tree.yview)

        #== Placing scrollbar ==#
        self.scrollbary.place(relx=0.935, rely=0.274, width=21, height=292)

        #== Configuring Headings ==#
        self.tree.configure(
            columns=(
                "Product ID",
                "Name",
                "Category",
                "Sub-Category",
                "Price"
            )
        )

        #==  Setting Heading  ==#
        self.tree.heading("Product ID", text="Product ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Category", text="Category", anchor=W)
        self.tree.heading("Sub-Category", text="Sub-Category", anchor=W)
        self.tree.heading("Price", text="Price", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=95)
        self.tree.column("#2", stretch=NO, minwidth=0, width=210)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=100)
        self.tree.column("#5", stretch=NO, minwidth=0, width=90)

        self.Display_data()

    def Display_data(self):
        try:
            data = []
            with open("Cart data.txt","r") as f:
                for line in f:
                    line = eval(line)
                    data.append(line)
            
            for record in data:
                if record[0] == userpassword.get():
                    self.tree.insert("","end", values=(
                        record[1],record[2],record[3],record[4],record[5]))
        except:
            messagebox.showinfo("Empty","Your cart is empty...!! \nPlease add items in cart first")
            
    select = []
    def tree_select(self, Event):
        self.select.clear()
        for i in self.tree.selection():
            if i not in self.select:
                self.select.append(i)
            
    def Back(self):
        cart.destroy()
    
    def delete_item(self):
        select = self.tree.selection()
        index = self.tree.focus()  # give number like I001, where 1 belongs natural number
        # print(index)
        index = index[3:]

        if len(select)!=0:   #== Ensuring user select any line 
            sure = messagebox.askyesno("Confirm","Are you sure you want to delete selected product?", parent = cart)
            if sure:
                for record in select:
                    self.tree.delete(record)  #-- Deleting selected line
                
                data = []
                with open("Cart data.txt","r") as f:
                    for line in f:
                        line = eval(line)
                        if line[0] == userpassword.get():
                            data.append(line)

                data_dic = {
                    
                    "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,
                    "N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35
                } 
                
                try:
                    del data[int(index) - 1]   #--deleting selected line from file

                except:
                    del data[data_dic[index]-1]   #-- deleting from file if index>9

                with open("Cart data.txt","w") as f:
                    for lst in data:
                        f.write(str(lst) + "\n")
                
        else:
            messagebox.showerror("Error!!","Please select product!!", parent = cart)
    

    def check_out(self):
        cart.withdraw()
        global check
        check = Toplevel()
        page4 = Check_Out(check)
        check.protocol("WM_DELETE_WINDOW", self.exit)
        check.mainloop()

    def exit(self):
        check.destroy()


class Check_Out:
    def __init__(self, top=None):
        top.geometry("1299x700")
        top.resizable(0, 0)
        top.title("Payment Process")

        #=== Background Image ===#
        self.label1 = Label(check)
        self.label1.place(relx=0, rely=0, height=700, width=1299)
        photo = Image.open("./images/check out.png")
        photo = photo.resize((1299,700),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image=photo)
        self.label1.configure(image=self.img1)

        #== Check out Button ==#
        self.logout_btn = Button(check)
        self.logout_btn.place(relx=0.690,rely=0.865, width=80, height=37)
        self.logout_btn.configure(relief="flat")
        self.logout_btn.configure(text="Pay")
        self.logout_btn.configure(overrelief="flat")
        self.logout_btn.configure(activebackground="gray20")
        self.logout_btn.configure(cursor="hand2")
        self.logout_btn.configure(bg="dark slate gray")
        self.logout_btn.configure(bd=0)
        self.logout_btn.configure(foreground="white")
        self.logout_btn.configure(font="-family {Poppins SemiBold} -size 16")
        self.logout_btn.configure(command=self.Pay)

        #== Walmart Label ==#
        self.wal_lbl = Label(check)
        self.wal_lbl.place(x=150, y=10)
        self.wal_lbl.configure(text="WALMART")
        self.wal_lbl.configure(font="Impact 35")
        self.wal_lbl.configure(bg="dark slate gray",padx=60)
        self.wal_lbl.configure(foreground="white")

        #== Payment Area ==#
        self.wal_lbl = Label(check)
        self.wal_lbl.place(x=780, y=15)
        self.wal_lbl.configure(text="Payment Area")
        self.wal_lbl.configure(font="Impact 25")
        self.wal_lbl.configure(bg="dark slate gray",padx=60)
        self.wal_lbl.configure(foreground="white")

        #== Customer name Entry ==#
        self.entry = Entry(check)
        self.entry.place(relx=0.190, rely=0.258, width=300, height=43)
        self.entry.configure(font="-family {Poppins} -size 17")
        self.entry.configure(relief="flat")

        #== Customer Phone Entry ==#
        self.entry1 = Entry(check)
        self.entry1.place(relx=0.190, rely=0.395, width=305, height=43)
        self.entry1.configure(font="-family {Poppins} -size 17")
        self.entry1.configure(relief="flat")

        #== Customer Addrress Entry ==#
        self.entry2 = Entry(check)
        self.entry2.place(relx=0.130, rely=0.530, width=320, height=43)
        self.entry2.configure(font="-family {Poppins} -size 17")
        self.entry2.configure(relief="flat")

        #== Customer CNIC Entry ==#
        self.entry3 = Entry(check)
        self.entry3.place(relx=0.130, rely=0.660, width=320, height=43)
        self.entry3.configure(font="-family {Poppins} -size 17")
        self.entry3.configure(relief="flat")

        #== Product Quantity display ==#
        prod_data = []
        with open("Cart data.txt","r") as f:
            quantity = 0
            for line in f:
                line = eval(line)
                if line[0] == userpassword.get():
                    prod_data.append(line)
                    quantity += 1
        self.label = Label(check)
        self.label.place(relx=0.130, rely=0.870, width=315, height=43)
        self.label.configure(font="-family {Poppins} -size 17")
        self.label.configure(bg="white")
        self.label.configure(fg="black")
        self.label.configure(text=quantity)

        #== Account title Entry ==#
        self.entry5 = Entry(check)
        self.entry5.place(relx=0.515, rely=0.277, width=340, height=40)
        self.entry5.configure(font="-family {Poppins} -size 17")
        self.entry5.configure(relief="flat")

        #== Account No.Entry ==#
        self.entry6 = Entry(check)
        self.entry6.place(relx=0.520, rely=0.437, width=340, height=40)
        self.entry6.configure(font="-family {Poppins} -size 17")
        self.entry6.configure(relief="flat")

        #== Bank name Entry ==#
        self.entry7 = Entry(check)
        self.entry7.place(relx=0.520, rely=0.610, width=340, height=40)
        self.entry7.configure(font="-family {Poppins} -size 17")
        self.entry7.configure(relief="flat")

        #== Passcode Entry ==#
        self.entry8 = Entry(check)
        self.entry8.place(relx=0.530, rely=0.770, width=300, height=40)
        self.entry8.configure(font="-family {Poppins} -size 17")
        self.entry8.configure(relief="flat")
        self.entry8.configure(show="*")

    def Pay(self):
        cus_nam = self.entry.get()
        cus_phone = self.entry1.get()
        cus_address = self.entry2.get()
        cus_cnic = self.entry3.get()
        acc_title = self.entry5.get()
        acc_no = self.entry6.get()
        bank_nam = self.entry7.get()
        passcode = self.entry8.get()

        if cus_nam.strip():
            if cus_phone:
                if cus_address:
                    if cus_cnic:
                        if acc_title:
                            if acc_no:
                                if bank_nam:
                                    if valid_phone(self.entry1.get()):
                                        if valid_cnic(self.entry3.get()):
                                            if passcode:
                                                self.Pay_final()
                                        
                                            else:
                                                messagebox.showerror("Error!","Please Enter Your Passcode",parent = check)
                                       
                                        else:
                                            messagebox.showerror("Oops!", "Please enter valid CNIC no..", parent=check)
                                            #-- Raising Exception --#
                                            raise ValueError("CNIC number can't be alphabets")

                                    else:
                                        messagebox.showerror("Oops!", "Please enter valid Phone no..", parent=check)
                                         #-- Raising Exception --#
                                        raise ValueError("Phone number can't be alphabets")
        
                                else:
                                    messagebox.showerror("Error!","Please Enter Bank name",parent = check)
                            else:
                                messagebox.showerror("Error!","Please Enter Account No.",parent = check)
                        else:
                            messagebox.showerror("Error!","Please Enter Account title",parent = check)
                    else:
                        messagebox.showerror("Error!","Please Enter Your CNIC No.",parent = check)
                else:
                    messagebox.showerror("Error!","Please Enter Your Address",parent = check)
            else:
                messagebox.showerror("Error!","Please Enter Your phone No.",parent = check)
        else:
            messagebox.showerror("Error!","Please Enter Your Name",parent = check)


    def Pay_final(self):
        bill_num = "WMB" + str(random.randint(100,999))  #-- Creating random bill number
        customer_name = self.entry.get()
        customer_phone = self.entry1.get()
        today = date.today()
        Date = today.strftime("%B %d, %Y")

        data = []
        with open("Cart data.txt","r") as f:
            quantity = 0
            for line in f:
                line = eval(line)
                if line[0] == userpassword.get():
                    data.append(line)
                    quantity += 1
        
        product_names =[]  #-- all products appending in this list
        for product in data:
            product_names.append(product[2])

        product_category =[]  #-- All category appending in this list
        for product in data:
            product_category.append(product[3])

        product_prices = []  # -- All prices appending in this file
        for price in data:
            product_prices.append(price[5])

        check.withdraw()
        bill = Toplevel()
        bill.geometry("800x400")
        bill.title("Bill")

        #=== Background Image ===#
        self.label1 = Label(bill)
        self.label1.place(relx=0, rely=0, height=400, width=800)
        photo = Image.open("./images/Bill window2.png")
        photo = photo.resize((800,400),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image=photo)
        self.label1.configure(image=self.img1)

        product_nam = ""
        for item in product_names:
            product_nam += item + "\n"

        product_categ = ""
        for item in product_category:
            product_categ += item + "\n"

        product_price = ""
        for item in product_prices:
            product_price += item + "\n"
    
    
        #== Product name label ==#
        self.label2 = Label(bill)
        self.label2.place(relx=0.040, rely=0.490)
        self.label2.configure(text=product_nam)
        self.label2.configure(bg="white")
        self.label2.configure(fg="black")

        #== Product category label ==#
        self.label2 = Label(bill)
        self.label2.place(relx=0.450, rely=0.490)
        self.label2.configure(text=product_categ)
        self.label2.configure(bg="white")
        self.label2.configure(fg="black")

        #== Price label ==#
        self.label3 = Label(bill)
        self.label3.place(relx=0.860, rely=0.490)
        self.label3.configure(text=product_price)
        self.label3.configure(bg="white")
        self.label3.configure(fg="black")

        #== Customer name label ==#
        self.label4 = Label(bill)
        self.label4.place(relx=0.190, rely=0.230)
        self.label4.configure(text=customer_name)
        self.label4.configure(bg="white")
        self.label4.configure(fg="black")

        #== Bill no. label ==#
        self.label4 = Label(bill)
        self.label4.place(relx=0.150, rely=0.275)
        self.label4.configure(text=bill_num)
        self.label4.configure(bg="white")
        self.label4.configure(fg="black")

        #== Phone no. label ==#
        self.label4 = Label(bill)
        self.label4.place(relx=0.870, rely=0.230)
        self.label4.configure(text=customer_phone)
        self.label4.configure(bg="white")
        self.label4.configure(fg="black")

        #== Date label ==#
        self.label4 = Label(bill)
        self.label4.place(relx=0.801, rely=0.277)
        self.label4.configure(text=Date)
        self.label4.configure(bg="white")
        self.label4.configure(fg="black")

        #== Invoice Data ==#
        invoice = [bill_num,Date,customer_name,customer_phone]
        with open("Invoice data.txt", "a") as f:
            f.write(str(invoice) + "\n")

        #== Shopping History ==#
        data_cart = []
        with open("Cart data.txt","r") as f:
            for line in f:
                line = eval(line)
                if line[0] == userpassword.get():
                    data_cart.append(line)


        with open("Shopping history data.txt","a") as f:
            for product in data_cart:
                sh_history = [userpassword.get(),product[2],product[3],product[5],Date]
                f.write(str(sh_history) + "\n")
                
#=== Driver Code ===#
page1 = Login_customer(root)
page1.login_frame()
root.mainloop()