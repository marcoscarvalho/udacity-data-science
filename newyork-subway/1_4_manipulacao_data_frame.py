# coding: utf-8

import numpy
import pandas
import pandasql

def filter_by_regular(filename):

    turnstile_data = pandas.read_csv(filename, encoding='ISO-8859-1')
    q = """
    select * from turnstile_data where DESCn = 'REGULAR';
    """
    return pandasql.sqldf(q, locals())
	
def get_hourly_entries(df):
    #Responsável por pegar o atual - o anterior com shift(1)
    df['ENTRIESn_hourly'] = pandas.Series(df['ENTRIESn'] - df['ENTRIESn'].shift(1))
    # Função que tira NaN e modifica para 1
    df['ENTRIESn_hourly'] = df['ENTRIESn_hourly'].fillna(1) 
    return df

output_file = 'turnstile_1706.txt'
print(get_hourly_entries(filter_by_regular(output_file)))