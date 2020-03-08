import unittest
import CsvtoJson
import re
import csv

# class for providing test capabilities by inheriting unittest
makeNoteOfRecords = {}


class testCsvJson(unittest.TestCase):
    def setUp(self):
        self.data = '\sample10.csv'

    def test_chkValidLicense_0(self):
        # invalid String from "RemovedRecords.json"
        result = CsvtoJson.chkValidLicense("1094548341")
        self.assertEqual(result, False)

    def test_chkValidLicense_1(self):
        # Empty String from
        result = CsvtoJson.chkValidLicense("")
        self.assertEqual(result, False)

    def test_chkValidLicense_3(self):
        # Valid String from "RemovedRecords.json"
        result = CsvtoJson.chkValidLicense("7068085734")
        self.assertEqual(result, True)

    def test_chkValidLicense_4(self):
        # Test when no. of digits are not 10
        result = CsvtoJson.chkValidLicense("12")
        self.assertEqual(result, False)

    def test_convert_date_5(self):
        result = CsvtoJson.convert_date("7/4/18")
        self.assertIsNotNone(result)

    def test_convert_date_6(self):
        result = CsvtoJson.convert_date("2019-07-29")
        self.assertIsNotNone(result)

    def test_convert_date_7(self):
        result = CsvtoJson.convert_date("2020/7/4")
        self.assertIsNone(result)

    def test_convert_date_8(self):
        result = CsvtoJson.convert_date("07-29-2019")
        self.assertIsNone(result)

    # def test_cleanDataRecord_9(self):
    #     CsvtoJson.csvFile = self.data
    #     CsvtoJson.cleanDataRecord()
    #     result = True
    #     self.assertEqual(result, True)
