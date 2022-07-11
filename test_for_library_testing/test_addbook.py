import sys
import fake_data_lib
sys.path.insert(0, "/home/dell/Desktop/projects/libmanagment") 

import library,unittest,faker
class test_add_book(unittest.TestCase):
    def test_case1(self):
        f=faker.Faker()
        self.assertEqual(library.Library.add_book(f.sentence().split(".")[0],type="Novel",writer=f.name(),year=f.year(),number_of_books=10),"book added sucessfully")
unittest.main()