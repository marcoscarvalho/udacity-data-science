# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''Antes de realizar qualquer análise, pode ser útil olhar para os dados que esperamos analisar. 
Mais especificamente, vamos examinar as entradas por hora em nossos dados do metrô de Nova York 
para determinar a distribuição dos dados. Estes dados são armazenados na coluna ['ENTRIESn_hourly'].

Trace dois histogramas nos mesmos eixos para mostrar as entradas quando esta chovendo vs quando não 
está chovendo. Abaixo está um exemplo sobre como traçar histogramas com pandas e matplotlib:
Turnstile_weather ['column_to_graph']. Hist ()

http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
'''

def return_data_frame(filename):

    return pd.read_csv(filename, encoding='ISO-8859-1')

def entries_histogram(df):
    print(df.groupby('rain')['ENTRIESn_hourly'].size())
	
    bins30 = np.linspace(0, df['ENTRIESn_hourly'].max(), num=30)
    print(bins30)

    bins = 150
    alpha = 0.5
    xmin = ymin = 0
    xmax = 6000
    ymax = 45000
    
    plt.figure()
    # your code here to plot a historgram for hourly entries when it is raining
    df['ENTRIESn_hourly'][df['rain']==1].hist(bins=bins, alpha=alpha, label = 'Rain') 

    # your code here to plot a historgram for hourly entries when it is not raining
    df['ENTRIESn_hourly'][df['rain']==0].hist(bins=bins, alpha=alpha, label = 'No rain') 
    
    plt.axis([xmin, xmax, ymin, ymax])
    plt.suptitle('Histogram of ENTRIESn_hourly')
    plt.title("bin of 150")
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')
    plt.legend()

    plt.figure()
    # your code here to plot a historgram for hourly entries when it is raining
    df['ENTRIESn_hourly'][df['rain']==1].hist(bins=30, alpha=alpha, label = 'Rain') 
    
    # your code here to plot a historgram for hourly entries when it is not raining
    df['ENTRIESn_hourly'][df['rain']==0].hist(bins=30, alpha=alpha, label = 'No rain') 
    
    #plt.xticks(bins30)
    plt.suptitle("Histogram of ENTRIESn_hourly")
    plt.title("bin of 30")
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')
    plt.legend()
    
    return plt

filename = "turnstile_data_master_with_weather.csv"
entries_histogram(return_data_frame(filename)).show()