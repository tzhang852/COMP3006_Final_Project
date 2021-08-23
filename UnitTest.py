"""Unit tests for data frame functionality."""
import unittest
import temperature
import happiness
import analysis
import os

class TestingUnit(unittest.TestCase):
    def test_happiness_filepath(self):
        exists = os.path.exists("data_files/happiness.csv")
        if not exists:
            self.assertRaises(FileNotFoundError)
    
    def test_temperature_filepath(self):
        exists = os.path.exists("data_files/tasmax.csv")
        if not exists:
            self.assertRaises(FileNotFoundError)
    
    def 
        

# class TestHappiness(unittest.TestCase):
#     def test_dataframe(self):

# class TestAnalysis(unittest.TestCase):
#     def test_dataframe(self): 

if __name__ == '__main__':
    unittest.main()

