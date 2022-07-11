
import library
print("starting the library")
adm=input("make admin user\n")
security_code=input("enter new security code\n")
library.Library.admin_code=security_code
while(True):
    print("WHO ARE YOU\ntype Reader for Reader \ntype admin for admin \ntype exit to exit")
    str1=input()
    c=0
    if str1=="Reader":
        name1=input("enter your username that has not been taken by anyone else\n")
        for i in library.reader.readers:
            if i.name==name1:
                print("username already exist")
                pas1=input("enter password")
                if pas1==i.password:
                    obj=i
                else:
                    print("wrong password")
                c=1
                break
        if c==0:
            contact=input("enter your contact\n")
            password=input("enter your password\n")
            address=input("enter your address\n")
            obj=library.reader(name1,contact,address,password)
            library.reader.readers.append(obj)

#"the old book of baby names"
        
        while True:
            print("""pick a choice
1. See available book on the shop
2. issue books by providing its name,type
3. return books
4. see profile
5. search for book by name
6. go backto login menu\n""")
            number=int(input("enter your choce from above\n"))
            if number==1:
                print(library.Library.show_book(str1))
            elif number==2:
                name=input("enter full name of the book\n")
                type=input("enter type of the book\n")
                date=input("date of book issuing in dd-mm-yyyy format\n")
                print(obj.issuebook(name,type,date))
            elif number==3:
                id=int(input("enter the id of the book that you issued\n"))
                date=input("date of book returning in yyyy-mm-dd format\n")
                print(obj.returbook(id,date))
            elif number==4:
                print(obj.see_profile())
            elif number==5:
                name=input("enter the name of book you want to search\n")
                print(obj.searchbooks(name))
            elif number==6:
                break
            else:
                print("could not found your request please try again\n")
                continue
    elif str1=="admin":
        sec_code=input("enter the security code for admin access\n")
        if library.Library.admin_code!=sec_code:
            pass
        else:         
            while True:
                print("""pick a choice
1. display the books 
2. add books
3. remove books
4. list of readers
5. list of issued books
6. go backto last menu""")
                number=int(input("enter your choice from above\n"))
                if number==1:
                    print(library.Library.show_book(str1))
                elif number==2:
                    name=input("enter name of the book")
                    type=input("type of the new book")
                    writer=input("writer of the book")
                    year=input("year of release of the book")
                    no_of_books=int(input("number of books"))
                    library.Library.add_book(name,type,writer,year,no_of_books)

                elif number==3:
                    id=int(input("enter the id of the book you want to remove"))
                    library.Library.remove_book(id)
                    
                elif number==4:
                    print(library.reader.seemulti_profile())
                elif number==5:
                    print(library.Library.issued_books)
                elif number==6:
                    break
                else:
                    print("could not found your request try again")
                    continue
            
    elif str1=="exit":
        break
    else:
        print("wrong command entered")
        continue