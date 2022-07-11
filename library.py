import Book


class Library:
    admin_code = ""
    books = []
    changable_book = []
    same_book = {}
    issued_books = {}
    ls1 = []
    b = []
    num = 1001

    @staticmethod
    def add_book(name, type, writer, year, number_of_books):
        for i in range(number_of_books):
            obj = Book.books1(name, type, writer, year)
            Library.books.append(obj)
            Library.changable_book.append(obj)
            if i == 0:
                Library.same_book[name] = [number_of_books, year, writer, type]
        return "book added sucessfully"

    @staticmethod
    def remove_book(id, name):
        c = 0

        for i in Library.changable_book:
            
            if i.book_number == id:
                Library.books.remove(i)
                Library.changable_book.remove(i)
                Library.same_book[name][0] -= 1

                c = 1
        if c == 1:
            return f"book number={id} removed"
        else:
            return f"could not find the book by number {id}"

    @classmethod
    def show_book(cls, str1):
        if str1 == "admin":
            cls.b = []
            for i in cls.changable_book:
                cls.b.append((i.name, i.type, i.writer,
                             i.year_of_printing, i.book_number))
            return (cls.b)
        elif str1 == "Reader":
            return (cls.same_book)

    @staticmethod
    def seemulti_profile():
        Library.ls1 = []
        for i in reader.readers:
            Library.ls1.append({"name": i.name, "id": i.id,"booksissued": i.booksissued, "fine": i.fine})
        return Library.ls1


class reader(Library):
    idnum = 101
    readers = []
    b = []

    def __init__(self, name, mail, address, password):
        self.name = name
        self.mail = mail
        self.address = address
        self.password = password
        self.id = reader.idnum
        self.booksissued = {}
        self.fine = 0.0
        reader.idnum += 1

    def issuebook(self, name, type, date):
        c = 0
        for i in Library.changable_book:
            if name == i.name and type == i.type:
                self.booksissued[i.book_number] = date
                Library.issued_books[i.book_number] = self.name
                a = Library.changable_book.index(i)
                Library.changable_book.pop(a)
                for j in Library.same_book.keys():
                    if j == i.name:
                        Library.same_book[j][0] -= 1
                c = 1
                return f"book {i.book_number} issued "
        if c == 0:
            return "book not available"

    def returbook(self, id1, date):
        c = 0
        for i in Library.books:
            if id1 in Library.issued_books.keys() and id1 == i.book_number:
                for j in Library.same_book.keys():
                    if j == i.name:
                        Library.same_book[j][0] += 1
                if Book.date.dat_minus_date(date=date, date1=self.booksissued[id1]) > 15:
                    self.fine = 5 * \
                        (Book.date.dat_minus_date(
                            date1=self.booksissued[id1], date=date)-15)
                    temp = self.booksissued[id1]
                    self.booksissued.pop(id1)
                    Library.changable_book.append(i)
                    Library.issued_books.pop(i.book_number)
                    return f"book returned fine={self.fine} return={date} issuing={temp}"
                elif Book.date.dat_minus_date(date1=self.booksissued[id1], date=date) == -1:
                    self.fine = 100
                    temp = self.booksissued[id1]
                    self.booksissued.pop(id1)
                    Library.changable_book.append(i)
                    Library.issued_books.pop(i.book_number)
                    return f"book returned fine={self.fine} return={date} issuing={self.booksissued[id1]}"
                elif Book.date.dat_minus_date(date1=self.booksissued[id1], date=date) == -2:
                    self.fine = 1000
                    temp = self.booksissued[id1]
                    self.booksissued.pop(id1)
                    Library.changable_book.append(i)
                    Library.issued_books.pop(i.book_number)
                    return f"book returned fine={self.fine} return={date} issuing={temp}"
                elif Book.date.dat_minus_date(date1=self.booksissued[id1], date=date) == -3:
                    return f"wrong date return={date} issuing={self.booksissued[id1]}"
                else:
                    temp = self.booksissued[id1]
                    self.booksissued.pop(id1)
                    Library.changable_book.append(i)
                    Library.issued_books.pop(i.book_number)

                    return f"book returned fine={self.fine} return={date} issuing={temp}"
                c = 1
        if c == 0:
            return f"book number ={id1} not found"

    def see_profile(self):
        return f"name={self.name}\nid={self.id}\nbooksissued={self.booksissued}\nfine={self.fine}"

    def searchbooks(self, str1):
        reader.b = []
        c=0
        for i in Library.books:
            if i.name == str1:
                reader.b.append((i.name, i.type, i.writer,i.year_of_printing, i.book_number))
                c=1
        if c==1:
            return (reader.b, len(reader.b))
        else:
            return "no result found"