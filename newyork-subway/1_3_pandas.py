# coding: utf-8

import numpy
import pandas

def filter_by_regular(filename):

    turnstile_data = pandas.read_csv(filename, encoding='ISO-8859-1')
    
    return numpy.mean(turnstile_data['DESCn'])
    #return turnstile_data
	
output_file = 'turnstile_1706.txt'
a = filter_by_regular(output_file)
print(a)