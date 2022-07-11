import sys
sys.path.insert(0, "/home/dell/Desktop/projects/libmanagment") 

import Book,library,unittest,faker

from faker import Faker
import factory

f = Faker("en_IN")
class bookFactory(factory.Factory):

    class Meta:
        model = Book.books1
    name = f.sentence().split(".")[0]
    type = "unique"
    writer = f.profile()['name']
    year = f.year()


class readerFactory(factory.Factory):

    class Meta:
        model = library.reader

    name=Faker("en_IN").name()
    mail = factory.LazyAttribute(lambda n : "%s@webllisto.com"%n.name.split(" ")[0])
    address = Faker("en_IN").address()
    password = Faker("en_IN").profile()["ssn"]
  