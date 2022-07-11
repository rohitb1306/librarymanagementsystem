import sys
from fake_data_lib import readerFactory,bookFactory
sys.path.insert(0, "/home/dell/Desktop/projects/libmanagment") 

import library,unittest,faker
class test_search_book(unittest.TestCase):
    
    def test_case1(self):
        f=faker.Faker()
        reader=readerFactory()
        for i in range(5):
            Book=bookFactory()
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==0:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
        f=faker.Faker()
        self.assertEqual(reader.searchbooks(Book.name),(reader.b, len(reader.b)))
    def test_case2(self):
        f=faker.Faker()
        reader=readerFactory()
        for i in range(5):
            Book=bookFactory()
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==0:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
        f=faker.Faker()
        self.assertEqual(reader.searchbooks(f.sentence().split(".")[0]),"no result found")
    
unittest.main()