# coding: utf-8

import pandas as pd
import pandasql

def return_data_frame(filename):

    return pd.read_csv(filename, encoding='ISO-8859-1')

def max_temp_aggregate_by_fog(df):
    q = """
    select fog, maxtempi  from df group by fog ;
    """
    return pandasql.sqldf(q, locals())
	
filename = "turnstile_data_master_with_weather.csv"
df = return_data_frame(filename)
print(max_temp_aggregate_by_fog(df))
