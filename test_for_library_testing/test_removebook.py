import sys
from fake_data_lib import readerFactory,bookFactory
sys.path.insert(0, "/home/dell/Desktop/projects/libmanagment") 

import library,unittest,faker
class test_remove_book(unittest.TestCase):
    def test_case1(self):
        f=faker.Faker()
        user=readerFactory()
        for i in range(5):
            Book=bookFactory(name="the old book of baby names",type="novel")
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==4:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
        user.issuebook(Book.name,Book.type,"2022-06-13")
        self.assertEqual(library.Library.remove_book(1004,Book.name),"book number=1004 removed")
    
    def test_case2(self):
        f=faker.Faker()
        user=readerFactory()
        for i in range(0,5):
            Book=bookFactory(name="let us c",type="programing")
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==0:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
        # user.issuebook(Book.name,Book.type,"2022-06-13")
        self.assertEqual(library.Library.remove_book(1006,Book.name),"book number=1006 removed")
    
    def test_case3(self):
        f=faker.Faker()
        user=readerFactory()
        for i in range(0,5):
            Book=bookFactory()
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==0:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
        user.issuebook(Book.name,Book.type,"2022-06-13")
        self.assertEqual(library.Library.remove_book(1011,Book.name),"could not find the book by number 1011")
    
unittest.main()