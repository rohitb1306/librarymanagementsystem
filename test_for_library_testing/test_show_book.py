import sys
sys.path.insert(0, "/home/dell/Desktop/projects/libmanagment") 

import library,unittest
class test_add_book(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(library.Library.show_book("admin"),library.Library.b)
    
    def test_case2(self):
        self.assertEqual(library.Library.show_book("Reader"),library.Library.same_book)
unittest.main()