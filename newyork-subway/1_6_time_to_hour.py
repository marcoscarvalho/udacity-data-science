# coding: utf-8

from datetime import datetime

def time_to_hour(time):
    return datetime.strptime(time, '%H:%M:%S').time().hour
	
print(time_to_hour('21:35:00'))