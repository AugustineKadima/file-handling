import unittest
import readfile

class TestReadFile(unittest.TestCase):
    def test_get_data(self):
        with open("test.txt","r") as handle:
            data = handle.read()
            self.assertEqual(data,readfile.read_file("test.txt"))

    def test_nonfile(self):
            self.assertEqual(None,readfile.read_file("tests.txt"))


if __name__ == "__main__":
    unittest.main()