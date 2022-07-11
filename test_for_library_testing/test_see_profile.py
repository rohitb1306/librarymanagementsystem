import sys
from fake_data_lib import readerFactory
sys.path.insert(0, "/home/dell/Desktop/projects/libmanagment") 

import library,unittest,faker
class test_see_profile(unittest.TestCase):
    def test_case1(self):
        reader=readerFactory()
        self.assertEqual(reader.see_profile(),f"name={reader.name}\nid={reader.id}\nbooksissued={reader.booksissued}\nfine={reader.fine}")
unittest.main()