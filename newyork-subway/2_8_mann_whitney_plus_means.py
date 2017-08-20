# coding: utf-8

import numpy as np
import pandas as pd
import pandasql
import scipy
import scipy.stats

'''
Construa uma função que que retorne:
A média das entradas com chuva
A média das entradas sem chuva
O p-value comparando o numero com chuva e o número sem chuva
'''

def return_data_frame(filename):

    return pd.read_csv(filename, encoding='ISO-8859-1')

def mann_whitney_plus_means(df):
    with_rain = df['ENTRIESn_hourly'][df['rain'] == 1]
    without_rain = df['ENTRIESn_hourly'][df['rain'] == 0]
    
    print(with_rain)
    print(without_rain)

    with_rain_mean = np.mean(with_rain)
    without_rain_mean = np.mean(without_rain)
    U, p = scipy.stats.mannwhitneyu(with_rain, without_rain)
	
    print(U)

    return with_rain_mean, without_rain_mean, p 

filename = "turnstile_data_master_with_weather.csv"
print(mann_whitney_plus_means(return_data_frame(filename)))
