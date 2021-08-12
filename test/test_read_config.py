import os
import helper.helper as helper
import unittest
from parameterized import parameterized

class TestReadConfig(unittest.TestCase):
    def setUp(self):
        file = open("text.json", "w")
        file.write('{"FileName" : "./../inputData.xlsx" }')
        file.close()

    @parameterized.expand([("missing file", "missing.json",0),("correct file","./text.json",2)]
                          )
    def test_read_config_file(self, name,input,expected):
        res = helper.read_config_file(input)
        self.assertEqual(len(res), expected)

    def tearDown(self):
        os.remove("text.json")


if __name__ == '__main__':
    unittest.main()