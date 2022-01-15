#-- All imports --#
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import os
#------------------#

main = Tk()
main.title("Shopping Store")
main.geometry("1366x768")
main.resizable(0, 0)

def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()

main.protocol("WM_DELETE_WINDOW", Exit)

def login_admin():
    main.withdraw()
    os.system("python admin_login.py")  #-- going into admin_login file
    main.deiconify()

def login_customer():
    main.withdraw()
    os.system("python Customer_login.py") #-- going into customer_login file
    main.deiconify()

#== Main shopping window ==#
label1 = Label(main)
img1 = Image.open("./images/shopping store4.jpg")
img1 = img1.resize((1366, 768), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(img1)
label1.configure(image=photo1)
label1.place(relx=0, rely=0, width=1366, height=768)

#== Frame for labels ==#
F1 = Frame(main, bg="white")
F2 = Frame(main, bg="yellow", padx=30)
Label(F1, text="Login As ?", fg="black",
      font="Impact 35 bold", bg="white").pack(padx=50)
Label(F2, text="WALMART", fg="black",
      font="Impact 40", bg='yellow').pack(padx=50)
F1.place(x=550, y=130)
F2.place(x=515, y=50)

#== Login to customer button ==#
button1 = Button(main)
button1.place(relx=0.326, rely=0.446, width=146, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(borderwidth="0")
img2 = Image.open("./images/Customer2.png")
img2 = img2.resize((146, 90), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(img2)
button1.configure(image=photo2)
button1.configure(command=login_customer)

#== Login to Admin button ==#
button2 = Button(main)
button2.place(relx=0.561, rely=0.448, width=146, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(borderwidth="0")
img3 = Image.open("./images/Admin.png")
img3 = img3.resize((146, 90), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(img3)
button2.configure(image=photo3)
button2.configure(command=login_admin)


main.mainloop()
