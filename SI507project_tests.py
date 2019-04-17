from SI507project_tools import *
import requests
import json
import csv
import sqlite3
import unittest

class PartOne(unittest.TestCase):
    def test_nps_parks(self):
        self.cleaned_file = open('nps_parks.csv','r')
        self.row_reader = self.cleaned_file.readlines()
        #print(self.row_reader) # For debug reasons
        self.assertTrue(self.row_reader[1].split(",")[0], "Testing that there is a Name / first value in the row at index 1, we're skipping the ID number")
        self.assertTrue(self.row_reader[25].split(",")[0], "Testing that there is a Name / first value in the row at index 25, we're skipping the ID number!")
        self.cleaned_file.close()



class FinalProjSQLiteDBTests(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect("allstateparks_info.sqlite") # Connecting to database that should exist in autograder
        self.cur = self.conn.cursor()

    def test_for_States_table(self):
        res = self.cur.execute("select * from States")
        data = res.fetchall()
        self.assertTrue(data, 'Testing that you get a result from making a query to the States table')

    def test_for_Parks_table(self):
        res = self.cur.execute("select * from Parks")
        data = res.fetchall()
        self.assertTrue(data, 'Testing that you get a result from making a query to the Parks table')

    def test_Parks_insert_works(self):
        park = ('Ann Arbor', 'A college town which is home to the wolverines, the harvard of the west, and the beautiful block M. Hail to the Victors! Go Blue!', 'Ann Arbor, MI', "Affiliated Area")
        self.cur.execute("insert into Parks(Name, Descr, Location, Type) values (?, ?, ?, ?)", park)
        self.conn.commit()

    def test_for_Association_table(self):
        res = self.cur.execute("select * from association")
        data = res.fetchall()
        self.assertTrue(data, 'Testing that you get a result from querying the Association table')

    def tearDown(self):
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
