import sys
from fake_data_lib import readerFactory,bookFactory
sys.path.insert(0, "/home/dell/Desktop/projects/libmanagment") 

import library,unittest,faker
class testreturn_book(unittest.TestCase):
    
    # def test_case1(self):
    #     f=faker.Faker("en_IN")
    #     user=readerFactory(name=f.profile()["name"],address=f.profile()["address"],password=f.profile()["ssn"])
        
    #     for i in range(5):
    #         Book=bookFactory(name=f.sentence().split(".")[0],writer=f.profile()["name"],year=f.year())
    #         library.Library.books.append(Book)
    #         library.Library.changable_book.append(Book)
    #         if i==0:
    #             library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
    #     user.issuebook(Book.name,Book.type,str(f.date()))
    #     lst=[i for i in user.booksissued.keys()]
    #     self.assertEqual(user.returbook(lst[0],str(f.date())),f"book retuned fine={user.fine}")
    
    def test_case2(self):
        f=faker.Faker("en_IN")
        user=readerFactory(name=f.profile()["name"],address=f.profile()["address"],password=f.profile()["ssn"])
        for i in range(5):
            Book=bookFactory(name=f.sentence().split(".")[0],writer=f.profile()["name"],year=f.year())
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==0:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
        user.issuebook(Book.name,Book.type,"2022-06-13")
        lst=[int(i) for i in user.booksissued.keys()]
        temp=user.booksissued[lst[0]]        
        self.assertEqual(user.returbook(lst[0],"2022-07-10"),f"book returned fine={user.fine} return=2022-07-10 issuing={temp}")
    def test_case3(self):
        f=faker.Faker("en_IN")
        user=readerFactory(name=f.profile()["name"],address=f.profile()["address"],password=f.profile()["ssn"])
        for i in range(5):
            Book=bookFactory(name=f.sentence().split(".")[0],writer=f.profile()["name"],year=f.year())
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==0:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
        user.issuebook(Book.name,Book.type,"2022-06-13")
        lst=[int(i) for i in user.booksissued.keys()]
        temp=user.booksissued[lst[0]]        
        self.assertEqual(user.returbook(1006,"2022-07-10"),"book number =1006 not found")

    def test_case4(self):
        f=faker.Faker("en_IN")
        user=readerFactory(name=f.profile()["name"],address=f.profile()["address"],password=f.profile()["ssn"])
        for i in range(5):
            Book=bookFactory(name=f.sentence().split(".")[0],writer=f.profile()["name"],year=f.year())
            library.Library.books.append(Book)
            library.Library.changable_book.append(Book)
            if i==0:
                library.Library.same_book[Book.name]=[5,Book.year_of_printing,Book.writer,Book.type]
        user.issuebook(Book.name,Book.type,"2022-06-13")
        lst=[int(i) for i in user.booksissued.keys()]
        temp=user.booksissued[lst[0]]        
        self.assertEqual(user.returbook(lst[0],"2019-07-10"),f"wrong date return=2019-07-10 issuing={temp}")
    
unittest.main()