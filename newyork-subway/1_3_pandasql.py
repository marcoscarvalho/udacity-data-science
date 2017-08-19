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
	
output_file = 'turnstile_1706.txt'
a = filter_by_regular(output_file)
print(a)