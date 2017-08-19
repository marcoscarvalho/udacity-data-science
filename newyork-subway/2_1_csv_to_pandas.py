# coding: utf-8

import pandas as pd

def return_data_frame(filename):

    return pd.read_csv(filename, encoding='ISO-8859-1')

def num_rainy_days(df):
    
    
    
    
    #your code here
    return
	
filename = "turnstile_data_master_with_weather.csv"
print(return_data_frame(filename))