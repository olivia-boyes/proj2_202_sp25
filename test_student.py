import unittest
from logging import raiseExceptions

from proj2 import *

class TestProject2(unittest.TestCase):

    def test_read_csv_lines(self):
        data = read_csv_lines("sample-csv-data.csv")

        #check if csv file is empty
        self.assertIsNotNone(data)

        #check Row parsing
        self.assertEqual(data.value, Row("Laos",1990,None,None,0.51,0.11820764,0.51,0.11820764))

        data = data.next
        self.assertEqual(data.value, Row("Jordan",2018,9.53,0.9111017,22.99,2.1979253,24.71,2.3623633))

        data = data.next
        self.assertEqual(data.value, Row("Indonesia",1995,74.27,0.37483567,210.37,1.0617232,223.68,1.1288979))

        data = data.next
        self.assertEqual(data.value, Row("Ireland",1990,10.87,3.1187506,30.08,8.630361,30.96,8.882845))

        data = data.next
        self.assertEqual(data.value, Row("Japan",1992,444.89,3.5750017,1073.37,8.6252775,1115.04,8.960125))

        data = data.next
        self.assertEqual(data.value, Row("Japan",1994,470.26,3.758494,1118.46,8.93915,1160.76,9.277229))

        data = data.next
        self.assertEqual(data.value, Row("Japan",2005,519.54,4.0653095,1183.19,9.258254,1215.47,9.51084))

        data = data.next
        self.assertEqual(data.value, Row("Iceland",2005,0.01,0.03366584,2.21,7.4401507,2.26,7.60848))

        self.assertIsNone(data.next)

    def test_listlen(self):
        data = read_csv_lines("sample-csv-data.csv")
        self.assertEqual(listlen(data), 8)

    def test_filter_rows(self):
        data = read_csv_lines("sample-csv-data.csv")

        #Test comparison "equal"
        japan_data = Node(Row("Japan",1992,444.89,3.5750017,1073.37,8.6252775,1115.04,8.960125),
                          Node(Row("Japan",1994,470.26,3.758494,1118.46,8.93915,1160.76,9.277229),
                               Node(Row("Japan",2005,519.54,4.0653095,1183.19,9.258254,1215.47,9.51084))))
        self.assertEqual(filter_rows(data, "country", "equal", "Japan"), japan_data)
        #test ValueError
        with self.assertRaises(ValueError):
            filter_rows(data,"country", "greater_than","Japan")

        #Test "greater than" comparison
        #year
        self.assertEqual(filter_rows(data, "year", "greater_than", 2000), Node(Row("Jordan",2018,9.53,0.9111017,22.99,2.1979253,24.71,2.3623633),
                                                                               Node(Row("Japan",2005,519.54,4.0653095,1183.19,9.258254,1215.47,9.51084),
                                                                                    Node(Row("Iceland",2005,0.01,0.03366584,2.21,7.4401507,2.26,7.60848)))))
        #Test "less than" comparison
        self.assertEqual(filter_rows(data, "energy_co2_emissions", "less_than", 50),
                         Node(Row("Laos",1990,None,None,0.51,0.11820764,0.51,0.11820764),
                              Node(Row("Jordan",2018,9.53,0.9111017,22.99,2.1979253,24.71,2.3623633),
                                   Node(Row("Ireland",1990,10.87,3.1187506,30.08,8.630361,30.96,8.882845),
                                        Node(Row("Iceland",2005,0.01,0.03366584,2.21,7.4401507,2.26,7.60848))))))