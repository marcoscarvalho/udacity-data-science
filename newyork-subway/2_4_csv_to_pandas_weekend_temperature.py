# coding: utf-8

import pandas as pd
import pandasql

def return_data_frame(filename):

    return pd.read_csv(filename, encoding='ISO-8859-1')

def avg_weekend_temperature(df):
    q = """
    select avg(meantempi) from df where cast (strftime('%w', daten) as integer) in (0,6);
    """
    return pandasql.sqldf(q, locals())
	
filename = "turnstile_data_master_with_weather.csv"
df = return_data_frame(filename)
print(avg_weekend_temperature(df))
