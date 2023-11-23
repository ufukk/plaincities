import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plaincities import Globe

class GeneratedFilesTestCase(unittest.TestCase):

    def test_load_generated_files(self):
        globe = Globe('ko', path='tests/generated')
        usa = globe['US']
        self.assertEqual(usa.name, '미국')

if __name__ == '__main__':
    unittest.main()
