import random
class administrator:

    def login(self):
        correctEmail = False
        correctPassword = False
        print("\n/---- Welcome to admin Area ----/\n--- Please Enter Credential to Login ---\n")
        
        # ---- Checking the input ----- #
        while True:
            print("Continue with email or Phone?\n1: Email\n2: Phone")
            try:
                choose = int(input("Choose Option: "))
                break
            except:
                print("Invalid Input!!")
                continue

        if choose == 1:
            count = 0
            invalid = 0
            while True:
                email = input("\nEnter Your Email: ")
                if invalid == 5:
                    print("You are writing invalid email format\nPlease give correct format")
                    invali
                if count == 5:
                    print("It seems like you forgot Your Email\n please wait!!")
                    count = 0
                    continue

                # ---- Checking correct email ---- #
                if "@" in email and ".com" in email:
                    if email == "affansultan901@gmail.com":
                        print("Email Matched Successfully!!")
                        correctEmail = True
                        break
                    else:
                        print("Email not match\nTry Again!!")
                        count+=1
                        
                else:
                    print("Invalid Format!!")
                    invalid+=1

        elif choose == 2:

            # --- Checking for correct mobile number --- #
            while True:
                phone = input("\nEnter Your Mobile Number: ")
                if len(phone) == 11:
                    if phone == "03152044437":
                        print("Phone Number matched Successfully!!")
                        correctEmail = True 
                        break
                else
                    print("Please Enter valid Mobile Number!!")
                    continue
                
            
        count = 0

        # --- Checking for correct password --- #
        while True
            password = input("\nEnter Your Password: ")
            
            if count == 5:
                print("It seems like you forgot your password\nPlease Wait!!")
                count = 0
                continue
            if password == "CepDsa901":
                print("Password Matched Successfully!!")
                correctPassword 
                break
            else:
                print("Password not match\nTry Again!!")
                count+=1
        
        if correctEmail and correctPassword:
            print("\nLogin Successfull!!\n")

    # --- Main Dashbord --- #
    def dashBoard(self):
        print("\n---- Dashboard ----")
        while True:
            print("Main Menu\n1: Add book\n2: Remove Book\n3: Edit Book\n4: Cancel membership\n5: Exit")
            while True:
                try:
                    choose = int(input("Choose Option: "))
                    break
                except:
                    print("\nInvalid Input!!\n")
                    continue
            
            # --- Exiting --- #
            if choose == 5:
                sure = input("\nAre you sure?\nDo you want to logout: ")
                if sure.lower() == "yes" or sure.lower() == "y":
                    print("Loging Out.......")
                    return

            elif choose == 1:
                books = []
                idpresent = True
                
                # ---- Generating random id ---- #
                def idGenerate():
                    bookid = random.randint10)
                    check = checkId(bookid)
                    if not check:
                        return bookid

                # ---- Checking weather id already present or not ---- #
                def checkId(id):
                    for id in books:
                        if id[0] != id:
                            idpresent = False
                        else:
                            idGenerate()
                        return False
                
                booksinp = int(input("How many books do you want to Enter: "))

                # ---- Taking Input details of Book ---- #
                for book in range(booksinp):
                    savingId = idGenerate()
                    print(f"\nEntering book number {book+1}:")
                    booktitle = input("Enter Title: ")
                    author = input("Enter Author Name: ")
                    subject = input("Enter Subject: ")
                    publisher = input("Enter Publisher: ")
                    books.append([savingId,booktitle,author,subject,publisher])

                # --- Adding book into library --- #    
                with open("Library.txt","a") as f:
                    for each in books:
                        each = str(each)
                        f.write(each + "\n")

                print("\nBook added into library Successfully!!\n")
                    
            elif choose == 2:

                # --- Removing book from library --- #
                found = False
                backBook = []
                with open("Library.txt","r") as f:
                    for data in f:
                        data = eval(data)
                        backBook.append(data)

                rmBook = input("Enter title of the book: ")
                rmbookid = int(input("Enter id of the book: "))
                count = 0

                # --- Checking book is in library or not--- #
                for book in backBook:
                    if book[1].lower() == rmBook.lower() or book[] = rmbookid:
                        backBook.remove(backBook[count])
                        found = True
                    else:
                        count+=1
                
                if not found:
                    print("\nBook not present in the library\n")
                else:
                    # --- Removing --- #
                    print("\nBook removed from library successfully!!\n")
                    with open("Library.txt","w") as f:
                        for book in backBook:
                            f.write(str(book) + "\n")

            elif choose == 3:

                # --- Editing previous Book --- #
                present = False
                ebackBook = []
                with open("Library.txt",r") as f:
                    for data in f:
                        data = eval(data)
                        ebackBook.append(data)

                edBook = input("Enter title of the book: ")
                ebookid = int(input("Enter book id: "))
                for book in ebackBook:

                    # --- For displaying book --- #
                    if book[1].lower() == edBook.lower() or book[0] == ebookid:
                        present = True
                        print("\nBook found!!\n")
                        print("Book Title: "+book[1])
                        print("Author Name: "+book[2])
                        print("Subject of Book: "+book[3])
                        print("Publisher: "+book[4])

                        # --- Editing in the book details --- #
                        while True:
                            print("\nWhat you want to edit?")
                            print("1: Title\n2: Author\n3: Subject\n4: Publisher")
                            try:
                                echoose = int(input("Choose Option: "))
                                break
                            except:
                                print("\nInvalid Input!!\n")
                                continue

                        if echoose == 1:
                            newtitle = input("Enter New tilte: ")
                            book[1] = newtitle

                        elif echoose == 2:
                            newauthor = input("Enter New Author: ")
                            book[2] = newauthor

                        elif echoose == 3:
                            newsubject = input("Enter New Subject: ")
                            book[3] = newsubject

                        elif echoose == 4:
                            newpub = input("Enter New Publisher: ")
                            book[4] = newpub

                if not present:
                    print("Book is not present in the library\n")
                else:
                    # --- saving after editing --- #
                    print("Book is edit successfully!!\n")
                    with open("Library.txt","w") as f:
                        for book in ebackBook:
                            f.write(str(book) + "\n")

            elif choose == 4:

                # --- Cancelling membership of customer --- #
                canceldata = []
                mfound = False
                with open("Customer_data.txt","r") as f:
                    for data in f:
                        data = eval(data)
                        canceldata.append(data)
                cfname = input("Enter his/her first name: ")
                clname = input("Enter his/her last name: ")

                mcount = 0
                for member in canceldata:
                    if member[3].lower() == cfname.lower():
                        if member[3].lower() == clname.lower():
                            canceldata.remove(canceldata[mcount])
                            mfound = True
                            print("Membership cancelled Succesfully!!\n")
                    else:
                        mcount+=1
                if not mfound:
                    print("Member dosen't exist in our database!!\n")


class customer:
    
    def login(self):
        print("\n---- Welcome to the Login Area ----")
        cdata = []
        with open("Customer_data.txt","r") as f:
            for data in f:
                data = eval(data)
                cdata.append(data)

        cinvalid = 0
        ccount = 0
        attempt = False
        ccorrectEmail = False
        foundemail = ""

        # --- Checking validation of email --- #
        while True:
            cemail = input("Enter Your Email address: ")
            if cinvalid == 5:
                print("\nYou are writing invalid email format\nPlease give correct format\n")
                cinvalid = 0
                continue

            if ccount == 5:
                print("It seems like you don't have an account\n Please signUp!!\n")
                attempt=True
                break
            
            # --- Checking email from file --- #
            if "@" in cemail and ".com" in cemail:
                for match in cdata:
                    if cemail == match[0] or cemail == match[5]
                        print("Email Matched Successfully!!\n")
                        ccorrectEmail = True
                        foundemail cemail
                        break
                    
                if ccorrectEmail:
                    break
                else:
                    print("Email not match!\n") 
                    ccount+=1       
            else:
                print("Invalid Format!!\n")
                cinvalid+=1

        if not attempt:
            ccorrectPassword = False
            icount = 0

            # --- Checking Validation of password --- #
            while True:
                cpassword = input("Enter Your Password: ")

                if icount == 5:
                    print("It seems like you are not our user\nKindly signup to be our customer!!\n")
                    break

                if len(cpassword)<8:
                    print("Invalid Password!!\nPassword should be minimum 8 character long\n")
                    continue
                
                else:

                    # --- Matching password from file --- #
                    for match in cdata:
                        if foundemail==match[0] or foundemail==match[1]:
                            if cpassword == match[2]:
                                print("Password Matched!!\n")
                                ccorrectPassword = True
                                break
                            else:
                                continue
                    if ccorrectPassword:
                        break
                    else:
                        print("Password not match!!\n")
                        icount=

        if not attempt and ccorrectEmail and ccorrectPassword:
            print("Login Succesfull!!")


    # --- Signing Up for new acount --- #
    def signUp(self):
        customerData = []
        print("\n---- Welcome to the SignUp Area ----\n")
        fnam = input("Enter your First Name: ")
        lname = input("Enter your Last Name: ")

        while True:
            contact = input("Enter Your Contact Number: ")
            if len(contact) == 11:
                break
            else:
                print("Invalid Contact Number!!\n")
                continue

        while True:
            signemail = input("Enter Your Email: ")
            if "@" in signemail and ".com" in signemail:
                print("Email is valid!!\n")
                break
            else:
                print("Enter Valid Email Address!!\n")
                continue

        while True:
            password = input("Choose Your Password: ")
            if len(password) < 8:
                print("Password is too short!!\n")
                continue
            else:
                print("Password is strong!!\n")
                break
        
        customerData.append([signemail,contact,password,fname,lname])
        print("Your account has been registered!!\n")

        with open("Customer_data.txt","a") as f:
            for data in customerData:
                data = str(data)
                f.write(data + "\n")


    # --- Dashboard for all functions --- #
    def dashBoard(self):
        print("\n---- Welcome to Library Area ----")
        while True:
            print("Main menu\n1: Check-Out Book\n2: Reserve Book\n3: Renew Book\n4: Return Book\n5: Search Book \n6: Exit")
            while True:
                try:
                    choose = int(input("Choose Option: "))
                    break
                except:
                    print("\nInvalid Input!!\n")
                    continue

            # --- Exiting form dashboard --- # 
            if choose == 6:
                sure = input("\nAre you sure?\nDo you want to logout: ")
                if sure.lower() == "yes" or sure.lower) == "y":
                    print("Loging Out.......")
                    break
            
            # --- Checking out form library --- #
            elif choose == 1:
                print("Books Available In Library:\n")
                availBook = []
                with open("Library.txt","r")as f:
                    for book in n
                        book = eval(book)
                        availBook.append(book)

            # ---- Displaying all books from library --- #
                i = 0 
                for book in availBook:
                    print(f"Book Number: {i+1}")
                    print(f"Book Id: {book[0]}")
                    print(f"Title: {book[1]}")
                    print(f"Author: {book[2]}")
                    print(f"Subject: {book[3]}")
                    print(f"Publisher: {book[4]}\n")
                    i+=1

                saveval = ""
                id = 0
                while True:
                    check = False
                    count = 0
                    cchoice = input("Enter book name to check_out: ")
                    cid = int(input("Enter Book Id: "))
                    saveval = cchoice
                    id = cid

                    # --- Checking out book and removing from library --- #
                    for book in availBook:
                        cchoice = cchoice.strip()
                        book[1] = book[1].strip()
                        if book[1].lower() == cchoice.lower() or cid == book[0]:
                            availBook.remove(availBook[count])
                            print("Book is checked-Out successfully!!\n")
                            print("Your book id is {}\n\
                            Remember this id it will help you to renew and return your book".format(cid))
                            check = True
                            with open("CheckedOutBooks.txt","a")as f:
                                f.write(str([book[0],book[1],book[2],book[3],book[4]]))
                            break
                        else:
                            count +=1
                    if check:
                        break
                     
                    # --- If wrong input handling here --- #
                    if not check:
                        print("Please write exact name of the book as shown above\n")
                        seeBook = input("Do you want to see all books?: ")
                        if seeBook=="Y" or seeBook=="y" or seeBook.lower()=="yes":
                            i = 0 
                            for book in availBook:
                                print(f"Book Number: {i+1}")
                                print(f"Book Id: {book[0]}")
                                print(f"Title: {book[1]}")
                                print(f"Author: {book[2]}")
                                print(f"Subject: {book[3]}")
                                print(f"Publisher: {book[]}\n")
                                i+=1
                        else:
                            pass
                
                # --- Updating library -- #
                with open("Library.txt","w")as f:
                    for book in availBook:
                        book = str(book)
                        f.write(book + "\n")


            # --- Reserving book --- #
            elif choose == 2:
                print("\n--- Please enter some details ---")
                name = input("Enter Your Name: "
                reserve = input("Enter the name of the Book: ")
                print(f"Your book '{reserve}' is reserved!!\nThank you very much {name}!!")

            # --- Renewing book --- #
            elif choose == 3:
                issueBook = []
                renewed = False
                with open("CheckedOutBooks.txt","r")as f:
                    for check in f:
                        check = eval(check)
                        issueBook.append(check)

                while True:
                    renew = input("Enter the name of the book: ")
                    bookid = int(input("Enter book id: "))
                    for checkbook in issueBook:
                        if checkbook[0] == bookid:
                            print("Your Book {} is renewed!!\n".format(renew))
                            renewed = True
                            break
                    if renewed:
                        break
                    if not renewed:
                        print("The book {} is not present in our record!!\n".format(renew))

            # --- Returning Book into library --- #
            elif choose == 4:
                rbook = []
                rsaving = []
                rfound = False
                with open("CheckedOutBooks.txt","r")as f:
                    for data in f:
                        data = eval(data)
                        rsaving.appendata)
                
                print("--- Returning Area ---")
                print("Please fill some details to return a book:")
                rid = int(input("Enter Id of the Book: "))
                for checking in rsaving:
                    if rid == checking[0]:
                        rfound = True
                        with open("Library.txt","a")as f:
                            f.write(str(checking)+"\n")
                        print("\nBook Returned into library Successfully!!")
                    
                if not rfound:
                    print("We don't have any record of this book!!")

            # --- Searching book in library --- #
            elif choose == 5:
                storeBooksbyalpha = []
                storeBooksbyid = []
                available = []

                with open("Library.txt","r")as f:
                    for book in f:
                        book = eval(book)
                        storeBooksbyalpha.append(book)
                        storeBooksbyid.append(book)
                        available.append(book)

                # ----- Applying Bubble Sort ------#
                #------Sorting Alphabatically -----#

                for i in range(len(storeBooksbyalpha)-1):
                    for j in range(len(storeBooksbyalpha)-1-i):
                        if storeBooksbyalpha[j][1][0] > storeBooksbyalpha[j+1][1][0]:
                            storeBooksbyalpha[j],storeBooksbyalpha[j+1] = storeooksbyalpha[j+6],storeBooksbyalpha[j]
                
                # ------ Sorting by id --------- #
                for i in range(len(storeBooksbyid)-1):
                    for j in range(len(storeBooksbyid)-1-i):
                        if storeBooksbyid[j][0] > storeBooksbyid[j+1][0]:
                            storeBooksbyid[j],storeBooksbyid[j+1] = storeBooksbyid[j+1],storeBooksbyid[j]

                # ---- Applying Binary Search --- #

                print("Do you want to see all books?")
                see = input("Enter y or n : ")
                if see.lower() == "y":
                    
                    # --- Displaying book --- #
                    i= 0 
                    for book in available:
                        print(f"Book Number: {i+1}")
                        print(f"Book Id: {book[0]}")
                        print(f"Title: {book[1]}")
                        print(f"Author: {book[2]}")
                        print(f"Subject: {book[3]}")
                        print(f"Publisher: {book[4]}\n")
                        i+=1

                else:
                    founddone = 0
                    search = int(input("Enter id of book to search: "))
                    beg = 0
                    end = len(storeBooksbyid)-1
                    found = False
                    while beg<=end and not found:
                        mid = beg + end // 2
                        if search == storeBooksbyid[mid][0]:
                            founddone = search
                            found = True
                        elif search > storeBooksbyid[mid][0]:
                            beg = mid + 1
                        else:
                            end = mid - 1
                    if found:
                        print("Book found Successfully!!\n")
                        for data in storeBooksbyid:
                            if founddone == data[0]:
                                print(f"Book Id: {data[0]}")
                                print(f"Title: {data[1]}")
                                print(f"Author: {data[2]}")
                                print(f"Subject: {data[3]}")
                                print(f"Publisher: {data[4}\n")

# ------- Main Program --------#
if __name__ == '__main__':
    Admin = administrator()
    Customer = customer()

    print("\n----- Library Management system -----")
    print("-----// Engineer Affan Library //-----\n")


    while True:
        print("Who are You??")
        print("1: Administrator\n2: Customer")
        try:
            person = int(input("Choose Option: "))
            break
        except:
            print("\nInvalid Input!!\n")
            continue
    
    # --- Admin Area --- #
    if person == 1:
        Admin.login()
        Admin.dashBoard()
    
    # --- Customer Area --- #
    elif person == 2:
        while True:
            print("\nLogin or SignUp?\n1: Login\n2: SignUp\n3: Exit")
            while True:
                try:
                    choice = int(input("Choose Option: "))
                    break
                except:
                    print("\nInvalid Input!!\n")
                    continue
            if choice == 3:
                print("Library Closing........")
                break
            elif choice == 1:
                Customer.login()
                Customer.dashBoard()
            elif choice == 2:
                CustomerignUp()


















    
    

        
    

