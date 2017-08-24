# coding: utf-8

import pandas as pd
import pandasql

def return_data_frame(filename):

    return pd.read_csv(filename, encoding='ISO-8859-1')

'''
Perceba que no dataset existem várias linhas para o mesmo dia. 
Então é necessário distinguir o número de dias e não o número de linhas que no dataset está igual a 1.
'''
def num_rainy_days(df):
    q = """
    select COUNT(DISTINCT DATEn) num_rainy_days from df where rain = 1 ;
    """
    return pandasql.sqldf(q, locals())
	
filename = "turnstile_data_master_with_weather.csv"
df = return_data_frame(filename)
print(num_rainy_days(df))