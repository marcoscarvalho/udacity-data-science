# coding: utf-8

import pandas as pd
import pandasql

def return_data_frame(filename):

    return pd.read_csv(filename, encoding='ISO-8859-1')

def num_rainy_days(df):
    q = """
    select * from df where rain >= 1 ;
    """
    return pandasql.sqldf(q, locals())
	
filename = "turnstile_data_master_with_weather.csv"
df = return_data_frame(filename)
print(num_rainy_days(df))
