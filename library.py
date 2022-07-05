
from dbm.ndbm import library
from hashlib import algorithms_available
import libmanagment.Book as Book

class Library:
    admin_code=""
    books=[]
    changable_book=[]
    same_book={}
    issued_books={}
    for i in range(5):
        book=Book.books1("the old book of baby names","novel","Anees Salim","2021")
        books.append(book)
        changable_book.append(book)
        if i==0:
            same_book["the old book of baby names"]=[5,"2021","Anees Salim","novel"]
    

    @staticmethod
    def add_book(name,type,writer,year,number_of_books):
        for i in range(number_of_books):
            obj=Book.books1(name,type,writer,year)
            Library.books.append(obj)
            Library.changable_book.append(obj)
            if i==0:
                Library.same_book[name]=[number_of_books,year,writer,type]
    @staticmethod
    def remove_book(id):
        c=0
        for i in Library.changable_book:
            if i.book_number==id:
                Library.books.remove(i)
                Library.changable_book.remove(i)
                Library.same_book[i.name][0]-=1
                c=1
        if c==1:
            return f"book removed by number {id}"
        else:
            return f"could not find the book by number {id}"
    @classmethod
    def show_book(cls,str1):
        if str1=="admin":
            b=[]
            for i in cls.changable_book:
                b.append((i.name,i.type,i.writer,i.year_of_printing,i.book_number))
            return (b)
        elif str1=="Reader":
            b={}
            for i,j in cls.same_book.items():
                b[i]=j
            return (cls.same_book)
        # else:

        #     b=[]
        #     for i in cls.books:
        #         b.append((i.name,i.type,i.writer,i.year_of_printing,i.book_number))
        #     return (b)
    
    @staticmethod
    def seemulti_profile():
        set1=[]
        for i in reader.readers:
            set1.append({"name":i.name,"id":i.id,"booksissued":i.booksissued,"fine":i.fine})
        return set1
class reader(Library):
    idnum=100
    readers=[]
    def __init__(self,name,contact,address,password):
        self.name=name
        self.contact=contact
        self.address=address
        self.password=password
        self.id=reader.idnum
        self.booksissued={}
        self.fine=0.0
        reader.idnum+=1
    
    
    

    def issuebook(self,name,writer,date):
        c=0
        for i in Library.changable_book:
            if name!=i.name  and writer!=i.writer:
                continue
            else:
                self.booksissued[i.book_number]=date
                Library.issued_books[i.book_number]=self.name
                a=Library.changable_book.index(i)
                Library.changable_book.pop(a)
                for j in Library.same_book.keys():
                    if j==i.name:
                        Library.same_book[j][0]-=1
                c=1

                return f"book {i.book_number} issued "
        if c==0:
            return "book not available"

    def returbook(self,id,date):
        c=0
        for i in Library.books:
            if id==i.book_number:
                for j in Library.same_book.keys():
                    if j==i.name:
                        Library.same_book[j][0]+=1
                if Book.date.dat_minus_date(date=date,date1=self.booksissued[id])>15:
                    self.fine=5*(Book.date.dat_minus_date(date1=self.booksissued[id],date=date)-15)
                    self.booksissued.pop(i.book_number)
                    Library.changable_book.append(i)
                    Library.issued_books.pop(i.book_number)
                    return f"one book returned fine={self.fine}"
                elif Book.date.dat_minus_date(date1=self.booksissued[id],date=date)==-1:
                    self.fine=100
                    return f"book returned{self.fine}"
                elif Book.date.dat_minus_date(date1=self.booksissued[id],date=date)==-2:
                    self.fine=1000
                    return f"book returned{self.fine}"
                elif Book.date.dat_minus_date(date1=self.booksissued[id],date=date)==-3:
                    return f"wrong date"
                elif Book.date.dat_minus_date(date1=self.booksissued[id],date=date)==-4:
                    self.fine=1000
                    return f"book returned{self.fine}"
                else:
                    self.booksissued.pop(i.book_number)
                    Library.changable_book.append(i)
                    Library.issued_books.pop(i.book_number)
                    return f"one book returned fine={self.fine}"
                c=1
        if c==0:
            return "wrong book"           


    def see_profile(self):
        return f"name={self.name}\nid={self.id}\nbooksissued={self.booksissued}\nfine={self.fine}"
    
    def searchbooks(self,str1):
        b=[]
        for i in Library.books:
            if i.name==str1:
                b.append((i.name,i.type,i.writer,i.year_of_printing,i.book_number))
        return (b,len(b))
# Library.add_book("let us c","programming","deepak","2022",10)  
# ru=reader("rohit","1234","1234","1234")
# print(ru.issuebook("let us c","deepak","13-06-2022"))     
# print(Library.changable_book)