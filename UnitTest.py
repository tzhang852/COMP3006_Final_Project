"""Unit tests for data frame functionality."""
import unittest
import temperature
import happiness
import analysis
import os
import pandas as pd
import numpy as np

class TestingUnit(unittest.TestCase):
    def test_happiness_filepath(self):
        exists = os.path.exists("data_files/happiness.csv")
        if not exists:
            self.assertRaises(FileNotFoundError)
    
    def test_temperature_filepath(self):
        exists = os.path.exists("data_files/tasmax.csv")
        if not exists:
            self.assertRaises(FileNotFoundError)
    
    def test_happiest(self):
        yay = happiness.Happiness()
        data = {'year':[2008,2020], 'country':['Denmark', 'Finland'], 'happiness':[7.971,7.889]}
        check_yay = pd.DataFrame(data, columns = ['year', 'country', 'happiness'])
        self.assertEqual(yay.top_n_happiest_countries(2)[['year', 'country', 'happiness']].to_string(index=False),
                                                check_yay[['year', 'country', 'happiness']].to_string(index=False))
        
    def test_saddest(self):
        boo = happiness.Happiness()
        data = {'year':[2019,2017], 'country':['Afghanistan', 'Afghanistan'], 'happiness':[2.375,2.662]}
        check_boo = pd.DataFrame(data, columns = ['year', 'country', 'happiness'])
        self.assertEqual(boo.top_n_saddest_countries(2)[['year', 'country', 'happiness']].to_string(index=False),
                                               check_boo[['year', 'country', 'happiness']].to_string(index=False))
                                                
    def test_hottest(self):
        hottest = temperature.Temperature()
        data = {'year':[2010, 2010], 'country':['Mali', 'Niger'], 'max_temp':[36.683333,36.641667]}
        check_hottest = pd.DataFrame(data, columns = ['year', 'country', 'max_temp'])
        self.assertEqual(hottest.top_n_hottest_countries(2)[['year', 'country', 'max_temp']].to_string(index=False),
                                               check_hottest[['year', 'country', 'max_temp']].to_string(index=False))

    def test_coldest(self):
        brr = temperature.Temperature()
        data = {'year':[2013,2018], 'country':['Greenland', 'Greenland'], 'max_temp':[-10.041667,-10.041667]}
        check_brr = pd.DataFrame(data, columns = ['year', 'country', 'max_temp'])
        self.assertEqual(brr.top_n_coldest_countries(2)[['year', 'country', 'max_temp']].to_string(index=False),
                                               check_brr[['year', 'country', 'max_temp']].to_string(index=False))

if __name__ == '__main__':
    unittest.main()

