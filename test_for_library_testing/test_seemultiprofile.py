import sys
from fake_data_lib import readerFactory
sys.path.insert(0, "/home/dell/Desktop/projects/libmanagment") 

import library,unittest,faker
class test_see_multipleprofile(unittest.TestCase):
    
    def test_case1(self):
        reader=readerFactory()
        library.reader.readers.append(reader)
        self.assertEqual(library.Library.seemulti_profile(),library.Library.ls1)

    def test_case2(self):
        reader=readerFactory()
        library.reader.readers.append(reader)
        reader1=readerFactory()
        library.reader.readers.append(reader1)
        self.assertEqual(library.Library.seemulti_profile(),library.Library.ls1)
unittest.main()