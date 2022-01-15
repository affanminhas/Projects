#== All Imports ==#
from tkinter import *
from tkinter import messagebox
import random
from tkinter import ttk
from tkinter import scrolledtext as tkst
from PIL import Image,ImageTk
from datetime import date
from time import strftime
import string
#---------------------------#

#-- Making Admin login window --#
root = Tk()
root.title("Admin login Area")
root.geometry("1199x600+100+50")

user = StringVar()
password = StringVar()
forgot = StringVar()

def valid_phone(num):
    try:
        if num.strip().isdigit():
            return True
    except:
        return False

def valid_cnic(num):
    try:
        if num.strip().isdigit():
            return True
    except:
        return False



class Login_page:
    def __init__(self,top=None):
        top.geometry("1366x730+1+5")
        top.title("Admin Login Area")
        top.resizable(0,0) #--Ensuring Window can not be resizable

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, height=730, width=1366)

        #=== Background Image ===#
        photo = Image.open("./images/admin login image.jpg")
        photo = photo.resize((1366,730),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image=photo)
        self.label1.configure(image=self.img1)

        #=== Walmart label ===#
        self.label2 = Label(root,bg="light goldenrod")
        self.label2.configure(text="WALMART",font="Times 50 bold")
        self.label2.place(x=800,y=90)

        #=== Login Frame ===#
        self.frame_login = Frame(root, bg="white")
        self.frame_login.place(x=150, y=150, height=400, width=520)

        #== Login Label ==#
        title = Label(self.frame_login, text="Login Here",font="Impact 33 bold",bg="white",
        fg="gray10").place(x=90,y=30)
        desc = Label(self.frame_login, text="Admin Login Area",font="Helvetica 14 bold italic",bg="white",
        fg="gray30").place(x=90,y=90)

        #== Username Label ==#
        labl_user = Label(self.frame_login, text="Username*",font="Goudyoldstyle 14 bold",bg="white",
        fg="gray").place(x=90,y=140)
        #-- Username Entry --#
        self.name_txt = Entry(self.frame_login,font="timesnewroman 14",bg="lightgray",textvariable=user
        ).place(x=90,y=177,width=350,height=35)

        #== Password Label ==#
        labl_password = Label(self.frame_login, text="Password*",font="Goudyoldstyle 14 bold",bg="white",
        fg="gray").place(x=90,y=220)
        #-- Password Entry --#
        self.password_txt = Entry(self.frame_login,font="timesnewroman 14",bg="lightgray",textvariable=password
        ,show="*").place(x=90,y=255,width=350,height=35)

        #== Forget Button ==#
        forget_btn = Button(self.frame_login,text="Forgot password?",bg="white",font="timesnewroman 13",bd=0
        ,cursor="hand2",command=forgot_pass).place(x=180,y=305)
        #== Login Button ==#
        login_btn = Button(top,text="Log In",bg="light goldenrod",fg="black",font="timesnewroman 14",bd=0
        ,cursor="hand2",padx=35,pady=3,command=self.Login).place(x=340,y=530)


    def Login(self, Event=None):
        #-- Getting set variable --#
        username = user.get()
        user_password = password.get()

        if username == "" or password == "": #-- Ensuring both entry should not empty --#
            messagebox.showerror("Error!!","Please provide complete detail")
        
        elif username == "affansultan901" and user_password == "12345":
            messagebox.showinfo("Login Page", "The login is successful.")

            #-- Drawing Admin Window --#
            root.withdraw()
            global adm
            global page2
            adm = Toplevel()  #-- Association
            page2 = Admin_page(adm)   #-- Making object of Admin_page
            adm.protocol("WM_DELETE_WINDOW", Exit) #-- Delete adm window window when click on "X" button on top right corner

            adm.mainloop()
        
        else:
            messagebox.showerror("Error","Incorrect username or password")

def new_password():
    txt_forgot = forgot.get()

    if txt_forgot == "":   #--Ensuring there is any email or phoee
        messagebox.showerror("Error","Please provide email or phone")
    elif txt_forgot == "affansultan901@gmail.com" or txt_forgot == "03152044437":
        messagebox.showinfo("New Password","Username : affansultan901 \nYour password is 12345")
    else:
        messagebox.showerror("Error","This Email or phone dosen't exist") # print if email or page 
        

def forgot_pass():
    password_window = Toplevel()
    pass_lbl = Label(password_window)  #-- widhtdrawing password window anf call
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

    #== Email/Phone Label ==#
    txt_labl = Label(password_window,text="Enter Your Email or Phone",fg="white",bg="gray10",
    font="Times 15 bold")
    txt_labl.place(x=190,y=90)

    #== Email/Phone Entry ==#
    forgot_entry = Entry(password_window,bg="light gray",font="timesnewroman 14",textvariable=forgot)
    forgot_entry.place(x=190, y=140, width=250, height=35)

    #== Submit Button ==#
    forgot_btn = Button(password_window,text="Submit",font="Helvetica 15",padx=30, pady=1, fg="black"
    ,bg="goldenrod",bd=0,cursor="hand2",command=new_password)
    forgot_btn.place(x=250,y=200, height=30)

    password_window.mainloop()

#-- Objects creating inside Exite box
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit", parent = root)
    if sure == True:
        adm.destroy()
        root.destroy()  #-- Distroying mainwindow

def Employee_func():
    adm.withdraw()
    global employee
    global page3
    employee = Toplevel() 
    page3 = Employee(employee) #---page3 class initializing
    page3.time() #---print current time
    employee.protocol("WM_DELETE_WINDOW", Exit)
    employee.mainloop()

def Inventory_func():
    adm.withdraw()
    global inventory
    global page4
    inventory = Toplevel()  #-- New window for inventory 
    page4 = Inventory(inventory)
    page4.time()
    inventory.protocol("WM_DELETE_WINDOW", Exit)
    inventory.mainloop()

def Invoice_func():
    adm.withdraw()
    global invoice
    global page5
    invoice = Toplevel() #-- New window for invoice
    page5 = Invoice(invoice)
    page5.time()
    invoice.protocol("WM_DELETE_WINDOW", Exit)
    invoice.mainloop()

def About_func():
    about = Toplevel()
    about.geometry("800x500")
    about.title("About")
    about.resizable(0,0)

    #== Background Image ==#
    label_pic = Label(about)
    label_pic.place(relx=0, rely=0, width=800, height=500)
    photo = Image.open("./images/About admin.png")
    photo = photo.resize((800,500),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(photo)
    label_pic.configure(image=img)

    about.mainloop()



class Admin_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Admin Mode")

        #== Background Image ==#
        self.label_pic = Label(top)
        self.label_pic.place(relx=0, rely=0, width=1366, height=768)
        photo = Image.open("./images/admin mode.png")
        photo = photo.resize((1366,768),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(photo)
        self.label_pic.configure(image=self.img)

        #== Admin Label ==#
        self.message = Label(adm)
        self.message.place(relx=0.046, rely=0.056, width=62, height=30)
        self.message.configure(font="-family {Poppins} -size 12")
        self.message.configure(foreground="black")
        self.message.configure(background="gray95")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        #== Admin Logo ==#
        self.admin_logo = Label(adm)
        self.admin_logo.place(relx=0.029, rely=0.056, width=25, height=30)
        adm_logo = Image.open("./images/admin logo.png")
        adm_logo = adm_logo.resize((20,15),Image.ANTIALIAS)
        self.adm_img = ImageTk.PhotoImage(adm_logo)
        self.admin_logo.configure(image=self.adm_img)

        #== Logout Button ==#
        self.logout_btn = Button(adm)
        self.logout_btn.place(relx=0.032, rely=0.106, width=76, height=23)
        self.logout_btn.configure(relief="flat")
        self.logout_btn.configure(overrelief="flat")
        self.logout_btn.configure(activebackground="DarkGoldenrod1")
        self.logout_btn.configure(font="-family {poppins SemiBold} -size 12")
        self.logout_btn.configure(cursor="hand2")
        self.logout_btn.configure(borderwidth="0")
        self.logout_btn.configure(text="Logout")
        self.logout_btn.configure(command=self.Logout)

        #== Walmart Label ==#
        self.wal_lbl = Label(adm)
        self.wal_lbl.place(x=610, y=20)
        self.wal_lbl.configure(text="WALMART")
        self.wal_lbl.configure(font="Impact 35")
        self.wal_lbl.configure(bg="DarkGoldenrod1",padx=60)

        #== Admin Mode Label ==#
        self.adm_lbl = Label(adm)
        self.adm_lbl.place(x=638,y=90)
        self.adm_lbl.configure(text="ADMIN MODE")
        self.adm_lbl.configure(font="Times 25 bold")
        self.adm_lbl.configure(bg="RoyalBlue4",padx=10)
        self.adm_lbl.configure(fg="white")

        #== Employee button ==#
        self.emp_btn = Button(adm)
        self.emp_btn.place(x=390, y=410, width=125, height=85)
        self.emp_btn.configure(relief="flat")
        self.emp_btn.configure(overrelief="flat")
        self.emp_btn.configure(activebackground="DarkGoldenrod1")
        self.emp_btn.configure(cursor="hand2")
        empp_btn = Image.open("./images/Employee.png")
        empp_btn = empp_btn.resize((130,90),Image.ANTIALIAS)
        self.emppic = ImageTk.PhotoImage(empp_btn)
        self.emp_btn.configure(image=self.emppic)
        self.emp_btn.configure(command=Employee_func)
        
        #== Inventory Button ==#
        self.inventory_btn = Button(adm)
        self.inventory_btn.place(x=545, y=410, width=120, height=90)
        self.inventory_btn.configure(relief="flat")
        self.inventory_btn.configure(overrelief="flat")
        self.inventory_btn.configure(activebackground="DarkGoldenrod1")
        self.inventory_btn.configure(cursor="hand2")
        inven_btn = Image.open("./images/Inventory.png")
        inven_btn = inven_btn.resize((120,90),Image.ANTIALIAS)
        self.invenbtn = ImageTk.PhotoImage(inven_btn)
        self.inventory_btn.configure(image=self.invenbtn)
        self.inventory_btn.configure(command=Inventory_func)

        #== Invoice Button ==#
        self.invoice_btn = Button(adm)
        self.invoice_btn.place(x=695, y=410, width=115, height=90)
        self.invoice_btn.configure(relief="flat")
        self.invoice_btn.configure(overrelief="flat")
        self.invoice_btn.configure(activebackground="DarkGoldenrod1")
        self.invoice_btn.configure(cursor="hand2")
        invo_btn = Image.open("./images/Invoice.png")
        invo_btn = invo_btn.resize((115,90),Image.ANTIALIAS)
        self.invobtn = ImageTk.PhotoImage(invo_btn)
        self.invoice_btn.configure(image=self.invobtn)
        self.invoice_btn.configure(command=Invoice_func)

        #== About Button ==#
        self.about_btn = Button(adm)
        self.about_btn.place(x=840, y=410, width=115, height=90)
        self.about_btn.configure(relief="flat")
        self.about_btn.configure(overrelief="flat")
        self.about_btn.configure(activebackground="DarkGoldenrod1")
        self.about_btn.configure(cursor="hand2")
        about_btn = Image.open("./images/About.png")
        about_btn = about_btn.resize((115,90),Image.ANTIALIAS)
        self.aboutbtn = ImageTk.PhotoImage(about_btn)
        self.about_btn.configure(image=self.aboutbtn)
        self.about_btn.configure(command=About_func)

    def Logout(self):
        sure = messagebox.askyesno("Logout","Are you sure you want to logout?",parent = adm)
        if sure:
            adm.destroy()
            root.deiconify()  #-- return back to root window
        

class Employee:
    def __init__(self, top=None):
        top.geometry("1299x700+30+20")
        top.resizable(0, 0)
        top.title("Employee Management")

        #== Background Image ==#
        self.label1 = Label(employee)
        self.label1.place(relx=0, rely=0, width=1299, height=700)
        photo = Image.open("images/employee management4.png")
        photo = photo.resize((1299,700),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(photo)
        self.label1.configure(image=self.img1)

        #== Admin text ==#
        self.admin = Label(employee)
        self.admin.place(relx=0.066, rely=0.057, width=136, height=30)
        self.admin.configure(font="-family {poppins} -size 10")
        self.admin.configure(background="#ffffff")
        self.admin.configure(foreground="#000000")
        self.admin.configure(text="""ADMIN""")
        self.admin.configure(anchor="w")

        #== Clock ==#
        self.clock = Label(employee)
        self.clock.place(relx=0.87, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {poppins light} -size 12")
        self.clock.configure(relief="flat")
        self.clock.configure(background="white")

        #== Employee ID Entry ==#
        self.entry1 = Entry(employee)
        self.entry1.place(relx=0.060, rely=0.274, width=218, height=18)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        #== Search Button ==#
        self.search_btn = Button(employee)
        self.search_btn.place(relx=0.232, rely=0.260, width=68, height=20)
        self.search_btn.configure(relief="flat")
        self.search_btn.configure(text="Search")
        self.search_btn.configure(overrelief="flat")
        self.search_btn.configure(activebackground="gold")
        self.search_btn.configure(cursor="hand2")
        self.search_btn.configure(bg="DarkGoldenrod1")
        self.search_btn.configure(bd=0)
        self.search_btn.configure(foreground="black")
        self.search_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.search_btn.configure(command=self.search_emp)

        #== Add Employee Button ==#
        self.add_emp_btn = Button(employee)
        self.add_emp_btn.place(relx=0.068, rely=0.410, width=275, height=33)
        self.add_emp_btn.configure(relief="flat")
        self.add_emp_btn.configure(text="ADD EMPLOYEE")
        self.add_emp_btn.configure(overrelief="flat")
        self.add_emp_btn.configure(activebackground="gold")
        self.add_emp_btn.configure(cursor="hand2")
        self.add_emp_btn.configure(bg="DarkGoldenrod1")
        self.add_emp_btn.configure(bd=0)
        self.add_emp_btn.configure(foreground="#ffffff")
        self.add_emp_btn.configure(font="-family {Poppins SemiBold} -size 14")
        self.add_emp_btn.configure(command=self.add_employee)

        #== Delete Employee Button ==#
        self.del_emp_btn = Button(employee)
        self.del_emp_btn.place(relx=0.068, rely=0.502, width=275, height=33)
        self.del_emp_btn.configure(relief="flat")
        self.del_emp_btn.configure(text="DELETE EMPLOYEE")
        self.del_emp_btn.configure(overrelief="flat")
        self.del_emp_btn.configure(activebackground="gold")
        self.del_emp_btn.configure(cursor="hand2")
        self.del_emp_btn.configure(bg="DarkGoldenrod1")
        self.del_emp_btn.configure(bd=0)
        self.del_emp_btn.configure(foreground="#ffffff")
        self.del_emp_btn.configure(font="-family {Poppins SemiBold} -size 14")
        self.del_emp_btn.configure(command=self.del_emp)

        #== Exit Button ==#
        self.exit_emp_btn = Button(employee)
        self.exit_emp_btn.place(relx=0.148, rely=0.863, width=68, height=20)
        self.exit_emp_btn.configure(relief="flat")
        self.exit_emp_btn.configure(text="EXIT")
        self.exit_emp_btn.configure(overrelief="flat")
        self.exit_emp_btn.configure(activebackground="gold")
        self.exit_emp_btn.configure(cursor="hand2")
        self.exit_emp_btn.configure(bg="DarkGoldenrod1")
        self.exit_emp_btn.configure(bd=0)
        self.exit_emp_btn.configure(foreground="black")
        self.exit_emp_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.exit_emp_btn.configure(command=self.Exit)

        #== Logout Button ==#
        self.logout_btn = Button(employee)
        self.logout_btn.place(relx=0.046, rely=0.102, width=61, height=18)
        self.logout_btn.configure(relief="flat")
        self.logout_btn.configure(text="LOGOUT")
        self.logout_btn.configure(overrelief="flat")
        self.logout_btn.configure(activebackground="gold")
        self.logout_btn.configure(cursor="hand2")
        self.logout_btn.configure(bg="DarkGoldenrod1")
        self.logout_btn.configure(bd=0)
        self.logout_btn.configure(foreground="black")
        self.logout_btn.configure(font="-family {Poppins SemiBold} -size 10")
        self.logout_btn.configure(command=self.Logout)

        #== Scroll bar ==#
        self.scrollbarx = Scrollbar(employee, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(employee, orient=VERTICAL)

        #== Treeview Widget ==#
        self.tree = ttk.Treeview(employee)
        self.tree.place(relx=0.312, rely=0.203, width=845, height=483)
        self.tree.configure(
            xscrollcommand = self.scrollbarx.set,
            yscrollcommand = self.scrollbary.set
        )
        self.tree.configure(selectmode="extended")
        self.tree.bind("<<TreeviewSelect>>", self.Tree_Select)

        #== Setting scrollbar to tree ==#
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        #== Placing scrollbar ==#
        self.scrollbarx.place(relx=0.312, rely=0.894, width=865, height=22)
        self.scrollbary.place(relx=0.963, rely=0.203, width=22, height=483)

        #== Tree Headings ==#
        self.tree.configure(
            columns=(
                "Employee ID",
                "Employee Name",
                "Contact No",
                "Address",
                "CNIC No",
                "Password",
                "Designation"            
            )
        )

        style = ttk.Style()
        style.configure("Treeview.Heading", foreground = "dark slate gray", font="Times 12")

        #-- Configuring Headings of tree view --#
        self.tree.heading("Employee ID", text="Employee ID", anchor = W)
        self.tree.heading("Employee Name", text="Employee Name", anchor = W)
        self.tree.heading("Contact No", text="Contact No", anchor =W)
        self.tree.heading("Address", text="Address", anchor = W)
        self.tree.heading("CNIC No", text="CNIC No", anchor = W)
        self.tree.heading("Password", text="Password", anchor = W)
        self.tree.heading("Designation", text="Designation", anchor = W)

        #-- Setting collumn width settings --#
        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=100)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=198)
        self.tree.column("#5", stretch=NO, minwidth=0, width=110)
        self.tree.column("#6", stretch=NO, minwidth=0, width=110)
        self.tree.column("#7", stretch=NO, minwidth=0, width=120)

        self.Displaydata()

    def Displaydata(self):
        data = []
        with open("Employee data.txt","r") as f:
            for line in f:
                line = eval(line)   #-- Evaluate line back to list
                data.append(line)

        for record in data:
            #-- Inserting data in treeview --#
            self.tree.insert("","end", values=(
                record[0],record[1],record[2],record[3],record[4],record[5],record[6]))
    

    def search_emp(self):
        emp_id = self.entry1.get()
        data_emp = []
        with open("Employee data.txt", "r") as f:
            for line in f:
                line = eval(line)
                data_emp.append(line)

        index = 0
        found = False
        for lst in data_emp:
            if emp_id == str(lst[0]):
                #-- Get all data from treeview --#
                child_id = self.tree.get_children()[index]
                self.tree.focus(child_id)    #-- focus on selected id
                self.tree.selection_set(child_id)  #-- give address of selected line
                messagebox.showinfo("Success!!", "Employee ID: {} found.".format(self.entry1.get()), parent=employee)
                found = True
            else:
                index += 1
        if not found:
            messagebox.showerror("Oops!!", "Employee ID: {} not found.".format(self.entry1.get()), parent=employee)


    # # global select
    select = []
    def Tree_Select(self, Event):
        self.select.clear()  
        for i in self.tree.selection():   #-- Give address of selected line id
            if i not in self.select:
                self.select.append(i)

    def del_emp(self):
        select = self.tree.selection()
        index = self.tree.focus()  # give number like I001, where 1 belongs natural number
        index = index[3:]

        if len(select)!=0:   #== Ensuring user select any line 
            sure = messagebox.askyesno("Confirm","Are you sure you want to delete selected employee?", parent = employee)
            if sure:
                for record in select:
                    self.tree.delete(record)  #-- Deleting selected line
                
                data = []
                with open("Employee data.txt","r") as f:
                    for line in f:
                        line = eval(line)
                        data.append(line)

                data_dic = {
                    
                    "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,
                    "N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35
                } 
                
                try:
                    del data[int(index) - 1]   #--deleting selected line from file

                except:
                    del data[data_dic[index]-1]   #-- deleting from file if index>9

                with open("Employee data.txt","w") as f:
                    for lst in data:
                        f.write(str(lst) + "\n")
        else:
            messagebox.showerror("Error!!","Please select an employee!!", parent = employee)



    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent = employee)
        if sure:
            employee.destroy()
            adm.deiconify()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            employee.destroy()
            root.deiconify()

    def add_employee(self):
        global emp_add
        emp_add = Toplevel()
        page6 = Add_Employee(emp_add)
        page6.time()
        emp_add.protocol("WM_DELETE_WINDOW", self.exit_emp)
        emp_add.mainloop()
    
    def exit_emp(self):
        emp_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.Displaydata()

class Add_Employee(Employee):
    def __init__(self, top=None):
        top.geometry("1299x700")
        top.title("Add Employee")
        top.resizable(0, 0)

        #== Background Image ==#
        self.label1 = Label(emp_add)
        self.label1.place(relx=0, rely=0, width=1299, height=700)
        photo = Image.open("images/Add Employee.png")
        photo = photo.resize((1299,700),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(photo)
        self.label1.configure(image=self.img1)
        
        #== clock ==#
        self.clock = Label(emp_add)
        self.clock.place(relx=0.80, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {poppins light} -size 12")
        self.clock.configure(relief="flat")
        self.clock.configure(foreground="black")
        self.clock.configure(background="white")

        #== Employee Name label ==#
        self.entry1 = Entry(emp_add)
        self.entry1.place(relx=0.10, rely=0.320, width=325, height=40)
        self.entry1.configure(font="-family {Poppins} -size 16")
        self.entry1.configure(relief="flat")

        #== Employee Contact label ==#
        self.entry2 = Entry(emp_add)
        self.entry2.place(relx=0.10, rely=0.512, width=325, height=40)
        self.entry2.configure(font="-family {Poppins} -size 16")
        self.entry2.configure(relief="flat")

        #== Employee CNIC label ==#
        self.entry3 = Entry(emp_add)
        self.entry3.place(relx=0.10, rely=0.694, width=325, height=40)
        self.entry3.configure(font="-family {Poppins} -size 16")
        self.entry3.configure(relief="flat")

        #== Employee designation label ==#
        self.entry4 = Entry(emp_add)
        self.entry4.place(relx=0.567, rely=0.320, width=325, height=40)
        self.entry4.configure(font="-family {Poppins} -size 16")
        self.entry4.configure(relief="flat")

        #== Employee address label ==#
        self.entry5 = Entry(emp_add)
        self.entry5.place(relx=0.567, rely=0.512, width=325, height=40)
        self.entry5.configure(font="-family {Poppins} -size 16")
        self.entry5.configure(relief="flat")

        #== Employee password label ==#
        self.entry6 = Entry(emp_add)
        self.entry6.place(relx=0.567, rely=0.692, width=325, height=40)
        self.entry6.configure(font="-family {Poppins} -size 16")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

        #== Add Button ==#
        self.add_btn = Button(emp_add)
        self.add_btn.place(relx=0.461, rely=0.834, width=105, height=40)
        self.add_btn.configure(relief="flat")
        self.add_btn.configure(text="Add")
        self.add_btn.configure(overrelief="flat")
        self.add_btn.configure(activebackground="gold")
        self.add_btn.configure(cursor="hand2")
        self.add_btn.configure(bg="DarkGoldenrod1")
        self.add_btn.configure(bd=0)
        self.add_btn.configure(foreground="black")
        self.add_btn.configure(font="-family {Poppins SemiBold} -size 20")
        self.add_btn.configure(command=self.add)

    def add(self):
        e_name = self.entry1.get()
       
        e_contact = self.entry2.get()
        e_cnic = self.entry3.get()
        e_designation = self.entry4.get()
        e_address = self.entry5.get()
        e_password = self.entry6.get()

        if e_name.strip():
            if e_contact:
                if e_cnic:
                    if e_designation:
                        if e_address:
                            if e_password:
                                if valid_phone(self.entry2.get()):
                                    if valid_cnic(self.entry3.get()):
                                        emp_id = "WME" + str(random.randint(100,999))  #-- generating random id
                                        insert = [emp_id,e_name,e_contact,e_address,e_cnic,e_password,e_designation]
                                        with open("Employee data.txt","a") as f:
                                            f.write(str(insert) + "\n")
                                        
                                        self.clear()
                                    else:
                                        messagebox.showerror("Oops!", "Please enter valid Cnic no..", parent=emp_add)
                                         #-- Raising Exception --#
                                        raise ValueError("CNIC number can't be alphabets")
                                else:
                                    messagebox.showerror("Oops!", "Please enter valid phone.", parent=emp_add)

                                    #-- Raising Exception --#
                                    raise ValueError("Phone number can't be alphabets")
                            else:
                                messagebox.showerror("Oops!", "Please enter a password.", parent=emp_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter address.", parent=emp_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter designation.", parent=emp_add)
                else:
                    messagebox.showerror("Oops!", "Please enter CNIC No..", parent=emp_add)
            else:
                messagebox.showerror("Oops!", "Please enter Contact.", parent=emp_add)
        else:
            messagebox.showerror("Oops!", "Please enter name.", parent=emp_add)

    def clear(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)


class Inventory:
    def __init__(self, top = None):
        top.geometry("1299x700+30+20")
        top.resizable(0, 0)
        top.title("Inventory")

        #== Background Image ==#
        self.label2 = Label(inventory)
        self.label2.place(relx=0, rely=0, width=1299, height=700)
        photo2 = Image.open("images/Inventory Management.png")
        photo2 = photo2.resize((1299,700),Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(photo2)
        self.label2.configure(image=self.img2)

        #== Clock ==#
        self.clock = Label(inventory)
        self.clock.place(relx=0.87, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {poppins light} -size 12")
        self.clock.configure(relief="flat")
        self.clock.configure(background="white")

        #== Admin Label ==#
        self.message = Label(inventory)
        self.message.place(relx=0.063, rely=0.056, width=62, height=30)
        self.message.configure(font="-family {Poppins} -size 12")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        #== Inventory ID Entry ==#
        self.entry1 = Entry(inventory)
        self.entry1.place(relx=0.060, rely=0.273, width=218, height=18)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        #== Search Button ==#
        self.search_btn = Button(inventory)
        self.search_btn.place(relx=0.232, rely=0.260, width=68, height=20)
        self.search_btn.configure(relief="flat")
        self.search_btn.configure(text="Search")
        self.search_btn.configure(overrelief="flat")
        self.search_btn.configure(activebackground="gold")
        self.search_btn.configure(cursor="hand2")
        self.search_btn.configure(bg="DarkGoldenrod1")
        self.search_btn.configure(bd=0)
        self.search_btn.configure(foreground="black")
        self.search_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.search_btn.configure(command=self.search_prod)

        #== Add Inventory Button ==#
        self.add_inven_btn = Button(inventory)
        self.add_inven_btn.place(relx=0.068, rely=0.410, width=275, height=33)
        self.add_inven_btn.configure(relief="flat")
        self.add_inven_btn.configure(text="ADD PRODUCT")
        self.add_inven_btn.configure(overrelief="flat")
        self.add_inven_btn.configure(activebackground="gold")
        self.add_inven_btn.configure(cursor="hand2")
        self.add_inven_btn.configure(bg="DarkGoldenrod1")
        self.add_inven_btn.configure(bd=0)
        self.add_inven_btn.configure(foreground="#ffffff")
        self.add_inven_btn.configure(font="-family {Poppins SemiBold} -size 14")
        self.add_inven_btn.configure(command=self.add_product)

        #== Delete Inventory Button ==#
        self.del_inven_btn = Button(inventory)
        self.del_inven_btn.place(relx=0.068, rely=0.502, width=275, height=33)
        self.del_inven_btn.configure(relief="flat")
        self.del_inven_btn.configure(text="DELETE PRODUCT")
        self.del_inven_btn.configure(overrelief="flat")
        self.del_inven_btn.configure(activebackground="gold")
        self.del_inven_btn.configure(cursor="hand2")
        self.del_inven_btn.configure(bg="DarkGoldenrod1")
        self.del_inven_btn.configure(bd=0)
        self.del_inven_btn.configure(foreground="#ffffff")
        self.del_inven_btn.configure(font="-family {Poppins SemiBold} -size 14")
        self.del_inven_btn.configure(command=self.del_prod)

        #== Exit Button ==#
        self.exit_inven_btn = Button(inventory)
        self.exit_inven_btn.place(relx=0.148, rely=0.863, width=68, height=20)
        self.exit_inven_btn.configure(relief="flat")
        self.exit_inven_btn.configure(text="EXIT")
        self.exit_inven_btn.configure(overrelief="flat")
        self.exit_inven_btn.configure(activebackground="gold")
        self.exit_inven_btn.configure(cursor="hand2")
        self.exit_inven_btn.configure(bg="DarkGoldenrod1")
        self.exit_inven_btn.configure(bd=0)
        self.exit_inven_btn.configure(foreground="black")
        self.exit_inven_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.exit_inven_btn.configure(command=self.Exit)

        #== Logout Button ==#
        self.logout_btn = Button(inventory)
        self.logout_btn.place(relx=0.046, rely=0.102, width=61, height=18)
        self.logout_btn.configure(relief="flat")
        self.logout_btn.configure(text="LOGOUT")
        self.logout_btn.configure(overrelief="flat")
        self.logout_btn.configure(activebackground="gold")
        self.logout_btn.configure(cursor="hand2")
        self.logout_btn.configure(bg="DarkGoldenrod1")
        self.logout_btn.configure(bd=0)
        self.logout_btn.configure(foreground="black")
        self.logout_btn.configure(font="-family {Poppins SemiBold} -size 10")
        self.logout_btn.configure(command=self.Logout)

        #== Scrollbar slider ==#
        self.scrollbarx = Scrollbar(inventory, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(inventory, orient=VERTICAL)

        #== Tree View Widget ==#
        self.tree = ttk.Treeview(inventory)
        self.tree.place(relx=0.310, rely=0.203, width=848, height=483)
        self.tree.configure(
            xscrollcommand = self.scrollbarx.set,
            yscrollcommand = self.scrollbary.set
        )
        self.tree.configure(selectmode="extended")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        #== Configuring scrollbar to treeview ==#
        self.scrollbarx.configure(command = self.tree.xview)
        self.scrollbary.configure(command = self.tree.yview)

        #== Placing scrollbar ==#
        self.scrollbarx.place(relx=0.312, rely=0.894, width=865, height=22)
        self.scrollbary.place(relx=0.963, rely=0.203, width=22, height=483)

        #== Configuring Headings ==#
        self.tree.configure(
            columns=(
                "Product ID",
                "Name",
                "Category",
                "Sub-Category",
                "In Stock",
                "MRP",
                "Cost Price",
                "Vendor No."
            )
        )

        #==  Setting Heading  ==#
        self.tree.heading("Product ID", text="Product ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Category", text="Category", anchor=W)
        self.tree.heading("Sub-Category", text="Sub-Category", anchor=W)
        self.tree.heading("In Stock", text="In Stock", anchor=W)
        self.tree.heading("MRP", text="MRP", anchor=W)
        self.tree.heading("Cost Price", text="Cost Price", anchor=W)
        self.tree.heading("Vendor No.", text="Vendor No.", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=230)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)
        self.tree.column("#8", stretch=NO, minwidth=0, width=100)

        self.Displaydata()

    def Displaydata(self):
        data = []
        with open("Product data.txt","r") as f:
            for line in f:
                line = eval(line)
                data.append(line)

        for record in data:
            #-- inserting ddata in treeview --#
            self.tree.insert("","end", values=(
                record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))


    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def del_prod(self):
        select = self.tree.selection()
        index = self.tree.focus()  # give number like I001, where 1 belongs natural number
        index = index[3:]
    
        if len(select)!=0:   #== Ensuring user select any line 
            sure = messagebox.askyesno("Confirm","Are you sure you want to delete selected product?", parent = inventory)
            if sure:
                for record in select:
                    self.tree.delete(record)  #-- Deleting selected line
                
                data = []
                with open("Product data.txt","r") as f:
                    for line in f:
                        line = eval(line)
                        data.append(line)

                data_dic_prod = {
                    
                    "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,
                    "N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35
                } 
                
                try:
                    del data[int(index) - 1]  #-- deleting selected line from file
                   
                except:
                    del data[data_dic_prod[index]-1]   #-- deleting if index > 9
 
                with open("Product data.txt","w") as f:
                    for lst in data:
                        f.write(str(lst) + "\n")
            
        else:
            messagebox.showerror("Error!!","Please select product!!", parent = inventory)


    def search_prod(self):
        prod_id = self.entry1.get()
        data_prod = []
        with open("Product data.txt", "r") as f:
            for line in f:
                line = eval(line)
                data_prod.append(line)

        index = 0
        found = False
        for lst in data_prod:
            if prod_id == lst[0]:
                child_id = self.tree.get_children()[index]  #-- give id of selected line
                self.tree.focus(child_id)  #-- focus on selected line 
                self.tree.selection_set(child_id)
                messagebox.showinfo("Success!!", "Product ID: {} found.".format(self.entry1.get()), parent=inventory)
                found = True
            else:
                index += 1
        if not found:
            messagebox.showerror("Oops!!", "Employee ID: {} does not found.".format(self.entry1.get()), parent=inventory)

    select = []
    def on_tree_select(self, Event):
        self.select.clear()
        for i in self.tree.selection():
            if i not in self.select:
                self.select.append(i)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent = inventory)
        if sure:
            inventory.destroy()
            adm.deiconify()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            inventory.destroy()
            root.deiconify()

    def add_product(self):
        global prod_add
        prod_add = Toplevel()
        page8 = Add_Product(prod_add)
        page8.time()
        prod_add.protocol("WM_DELETE_WINDOW", self.exit_prod)
        prod_add.mainloop()

    def exit_prod(self):
        prod_add.destroy()
        self.tree.delete(*self.tree.get_children())  #-- deleting all data of tree view
        self.Displaydata()   #-- again showing with updated data


class Add_Product(Inventory):
    def __init__(self, top=None):
        top.geometry("1299x700")
        top.resizable(0, 0)
        top.title("Add Product")

        #== Background Image ==#
        self.label1 = Label(prod_add)
        self.label1.place(relx=0, rely=0, width=1299, height=700)
        photo = Image.open("images/Add Product.png")
        photo = photo.resize((1299,700),Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(photo)
        self.label1.configure(image=self.img1)
        
        #== clock ==#
        self.clock = Label(prod_add)
        self.clock.place(relx=0.80, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {poppins light} -size 12")
        self.clock.configure(relief="flat")
        self.clock.configure(foreground="black")
        self.clock.configure(background="white")

        #== Product name Entry ==#
        self.entry = Entry(prod_add)
        self.entry.place(relx=0.099, rely=0.283, width=325, height=38)
        self.entry.configure(font="-family {Poppins} -size 16")
        self.entry.configure(relief="flat")

        #== Category Name Entry ==#
        self.entry1 = Entry(prod_add)
        self.entry1.place(relx=0.10, rely=0.438, width=325, height=38)
        self.entry1.configure(font="-family {Poppins} -size 16")
        self.entry1.configure(relief="flat")

        #==  Qauntity Entry ==#
        self.entry2 = Entry(prod_add)
        self.entry2.place(relx=0.10, rely=0.585, width=325, height=38)
        self.entry2.configure(font="-family {Poppins} -size 16")
        self.entry2.configure(relief="flat")

        #== Selling Price Entry ==#
        self.entry3 = Entry(prod_add)
        self.entry3.place(relx=0.10, rely=0.732, width=325, height=38)
        self.entry3.configure(font="-family {Poppins} -size 16")
        self.entry3.configure(relief="flat")

        #== Sub Category Entry ==#
        self.entry4 = Entry(prod_add)
        self.entry4.place(relx=0.569, rely=0.435, width=325, height=38)
        self.entry4.configure(font="-family {Poppins} -size 16")
        self.entry4.configure(relief="flat")

        #== Cost Price Entry ==#
        self.entry5 = Entry(prod_add)
        self.entry5.place(relx=0.569, rely=0.577, width=325, height=40)
        self.entry5.configure(font="-family {Poppins} -size 16")
        self.entry5.configure(relief="flat")

        #== vendor Phone No. Entry ==#
        self.entry6 = Entry(prod_add)
        self.entry6.place(relx=0.569, rely=0.727, width=325, height=40)
        self.entry6.configure(font="-family {Poppins} -size 16")
        self.entry6.configure(relief="flat")

        #== Add Button ==#
        self.add_btn = Button(prod_add)
        self.add_btn.place(relx=0.461, rely=0.834, width=105, height=40)
        self.add_btn.configure(relief="flat")
        self.add_btn.configure(text="Add")
        self.add_btn.configure(overrelief="flat")
        self.add_btn.configure(activebackground="gold")
        self.add_btn.configure(cursor="hand2")
        self.add_btn.configure(bg="DarkGoldenrod1")
        self.add_btn.configure(bd=0)
        self.add_btn.configure(foreground="black")
        self.add_btn.configure(font="-family {Poppins SemiBold} -size 20")
        self.add_btn.configure(command=self.add)

    
    def add(self):
        prod_name = self.entry.get()
        prod_category = self.entry1.get()
        prod_quantity = self.entry2.get()
        prodd_sell_price = self.entry3.get()
        prod_sub_cat = self.entry4.get()
        prod_cost_price = self.entry5.get()
        prod_vendor = self.entry6.get()

        if prod_name.strip():
            if prod_category:
                if prod_quantity:
                    if prodd_sell_price:
                        if prod_sub_cat:
                            if prod_cost_price:
                                if prod_vendor:
                                    if valid_phone(self.entry6.get()):
                                        prod_id = "WMP" + str(random.randint(100,999)) #-- generating random id
                                        insert = [prod_id,prod_name,prod_category,prod_sub_cat,prod_quantity,prodd_sell_price,prod_cost_price,prod_vendor]
                                        with open("Product data.txt","a") as f:
                                            f.write(str(insert) + "\n")
                                        self.clear()
                                    else:
                                        messagebox.showerror("Oops!", "Enter valid phone no..", parent=prod_add)
                                        #-- raising exception --#
                                        raise ValueError("Phone number should be digit")
                                else:
                                    messagebox.showerror("Oops!", "Please vendor No.", parent=prod_add)
                            else:
                                messagebox.showerror("Oops!", "Please enter cost price", parent=prod_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter product sub-category", parent=prod_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter selling price.", parent=prod_add)
                else:
                    messagebox.showerror("Oops!", "Please enter product quantity..", parent=prod_add)
            else:
                messagebox.showerror("Oops!", "Please enter product category.", parent=prod_add)
        else:
            messagebox.showerror("Oops!", "Please enter product name.", parent=prod_add)

    def clear(self):
        self.entry.delete(0, END)
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)



class Invoice:
    def __init__(self, top=None):
        top.geometry("1299x700+30+20")
        top.resizable(0, 0)
        top.title("Invoice")

        #== Background Image ==#
        self.label3 = Label(invoice)
        self.label3.place(relx=0, rely=0, width=1299, height=700)
        photo3 = Image.open("images/Invoices.png")
        photo3 = photo3.resize((1299,700),Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(photo3)
        self.label3.configure(image=self.img3)

        #== Clock ==#
        self.clock = Label(invoice)
        self.clock.place(relx=0.87, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {poppins light} -size 12")
        self.clock.configure(relief="flat")
        self.clock.configure(background="white")

        #== Admin Label ==#
        self.message = Label(invoice)
        self.message.place(relx=0.063, rely=0.056, width=62, height=30)
        self.message.configure(font="-family {Poppins} -size 12")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        #== Invoice ID Entry ==#
        self.entry1 = Entry(invoice)
        self.entry1.place(relx=0.060, rely=0.273, width=218, height=18)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        #== Search Button ==#
        self.search_btn = Button(invoice)
        self.search_btn.place(relx=0.232, rely=0.260, width=68, height=20)
        self.search_btn.configure(relief="flat")
        self.search_btn.configure(text="Search")
        self.search_btn.configure(overrelief="flat")
        self.search_btn.configure(activebackground="gold")
        self.search_btn.configure(cursor="hand2")
        self.search_btn.configure(bg="DarkGoldenrod1")
        self.search_btn.configure(bd=0)
        self.search_btn.configure(foreground="black")
        self.search_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.search_btn.configure(command=self.search_invoice)

        #== Delete Invoice Button ==#
        self.add_emp_btn = Button(invoice)
        self.add_emp_btn.place(relx=0.068, rely=0.410, width=275, height=33)
        self.add_emp_btn.configure(relief="flat")
        self.add_emp_btn.configure(text="DELETE INVOICE")
        self.add_emp_btn.configure(overrelief="flat")
        self.add_emp_btn.configure(activebackground="gold")
        self.add_emp_btn.configure(cursor="hand2")
        self.add_emp_btn.configure(bg="DarkGoldenrod1")
        self.add_emp_btn.configure(bd=0)
        self.add_emp_btn.configure(foreground="#ffffff")
        self.add_emp_btn.configure(font="-family {Poppins SemiBold} -size 14")
        self.add_emp_btn.configure(command=self.del_invoice)

        #== Exit Button ==#
        self.exit_emp_btn = Button(invoice)
        self.exit_emp_btn.place(relx=0.148, rely=0.863, width=68, height=20)
        self.exit_emp_btn.configure(relief="flat")
        self.exit_emp_btn.configure(text="EXIT")
        self.exit_emp_btn.configure(overrelief="flat")
        self.exit_emp_btn.configure(activebackground="gold")
        self.exit_emp_btn.configure(cursor="hand2")
        self.exit_emp_btn.configure(bg="DarkGoldenrod1")
        self.exit_emp_btn.configure(bd=0)
        self.exit_emp_btn.configure(foreground="black")
        self.exit_emp_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.exit_emp_btn.configure(command=self.Exit)

        #== Logout Button ==#
        self.logout_btn = Button(invoice)
        self.logout_btn.place(relx=0.046, rely=0.102, width=61, height=18)
        self.logout_btn.configure(relief="flat")
        self.logout_btn.configure(text="LOGOUT")
        self.logout_btn.configure(overrelief="flat")
        self.logout_btn.configure(activebackground="gold")
        self.logout_btn.configure(cursor="hand2")
        self.logout_btn.configure(bg="DarkGoldenrod1")
        self.logout_btn.configure(bd=0)
        self.logout_btn.configure(foreground="black")
        self.logout_btn.configure(font="-family {Poppins SemiBold} -size 10")
        self.logout_btn.configure(command=self.Logout)

        #==  Making Scrollbar  ==# 
        self.scrollbarx = Scrollbar(invoice, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(invoice, orient=VERTICAL)

        #== Tree View Widget ==#
        self.tree = ttk.Treeview(invoice)
        self.tree.place(relx=0.310, rely=0.203, width=848, height=483)
        self.tree.configure(
            yscrollcommand= self.scrollbary.set,
            xscrollcommand= self.scrollbarx.set)
        self.tree.configure(selectmode= "extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)  #-- binding what select on treeview

        #== configuring tree with scrollbar ==#
        self.scrollbarx.configure(command= self.tree.xview)
        self.scrollbary.configure(command= self.tree.yview)

        #== Placing Scrollbar ==#
        self.scrollbarx.place(relx=0.312, rely=0.894, width=865, height=22)
        self.scrollbary.place(relx=0.963, rely=0.203, width=22, height=483)

        #== Setting heading of columns ==#
        self.tree.configure(
            columns=(
                "Bill Number",
                "Date",
                "Customer Name",
                "Customer Phone No."
            )
        )

        #== Setting All headings ==#
        self.tree.heading("Bill Number", text="Bill Number", anchor = W)
        self.tree.heading("Date", text="Date", anchor = W)
        self.tree.heading("Customer Name", text="Customer Name", anchor = W)
        self.tree.heading("Customer Phone No.", text="Customer Phone No.", anchor = W)

        #== Setting column width ==#
        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=219)
        self.tree.column("#2", stretch=NO, minwidth=0, width=219)
        self.tree.column("#3", stretch=NO, minwidth=0, width=219)
        self.tree.column("#4", stretch=NO, minwidth=0, width=219)

        self.Displaydata()

    def Displaydata(self):
        data = []
        with open("Invoice data.txt","r") as f:
            for line in f:
                line = eval(line)
                data.append(line)

        for record in data:
            self.tree.insert("","end", values=(
                record[0],record[1],record[2],record[3]))
    

    def del_invoice(self):
        select = self.tree.selection()
        index = self.tree.focus()  # give number like I001, where 1 belongs natural number
        # print(index)
        index = index[3:]
    
        if len(select)!=0:   #== Ensuring user select any line 
            sure = messagebox.askyesno("Confirm","Are you sure you want to delete selected invoice?", parent = invoice)
            if sure:
                for record in select:
                    self.tree.delete(record)  #-- Deleting selected line
                
                data = []
                with open("Invoice data.txt","r") as f:
                    for line in f:
                        line = eval(line)
                        data.append(line)

                data_dic = {
                    
                    "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,
                    "N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35
                } 
                
                try:
                    del data[int(index) - 1]

                except:
                    del data[data_dic[index]-1]

                with open("Invoice data.txt","w") as f:
                    for lst in data:
                        f.write(str(lst) + "\n")
        else:
            messagebox.showerror("Error!!","Please select Invoice!!", parent = invoice)
    
    def search_invoice(self):
        invoice_id = self.entry1.get()
        data_invoice = []
        with open("Invoice data.txt", "r") as f:
            for line in f:
                line = eval(line)
                data_invoice.append(line)

        index = 0
        found = False
        for lst in data_invoice:
            if invoice_id == lst[0]:
                child_id = self.tree.get_children()[index]
                self.tree.focus(child_id)
                self.tree.selection_set(child_id)
                messagebox.showinfo("Success!!", "Invoice ID: {} found.".format(self.entry1.get()), parent=invoice)
                found = True
            else:
                index += 1
        if not found:
            messagebox.showerror("Oops!!", "Invoice ID: {} does not found.".format(self.entry1.get()), parent=invoice)

    select = []
    def on_tree_select(self, Event):
        self.select.clear()
        for i in self.tree.selection():
            if i not in self.select:
                self.select.append(i)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent = invoice)
        if sure:
            invoice.destroy()
            adm.deiconify()

    def Logout(self):
        sure = messagebox.askyesno("Logout","Are you sure you want to logout?")
        if sure:
            invoice.destroy()
            root.deiconify()

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


#--- Driver code ---#
page1 = Login_page(root)
root.bind("<Return>", Login_page.Login)
root.mainloop()