import sys
from fake_data_lib import bookFactory,readerFactory
sys.path.insert(0, "/home/dell/Desktop/projects/libmanagment") 

import library,unittest,faker

class testissue_book(unittest.TestCase):

    def test_case1(self):
        f=faker.Faker()
        reader=readerFactory()
        for i in range(5):
            Book=bookFactory()
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==0:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
                self.assertEqual(reader.issuebook(Book.name,Book.type,f.date()),f"book {[i for i in reader.booksissued.keys()][0]} issued ")
    
    def test_case2(self):
        f=faker.Faker()
        reader=readerFactory()
        for i in range(5):
            Book=bookFactory()
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==0:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
        self.assertEqual(reader.issuebook(f.sentence().split(".")[0],Book.type,f.date()),f"book not available")
    
unittest.main()     
