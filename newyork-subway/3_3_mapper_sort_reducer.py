#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader('turnstile_data_master_with_weather.csv', delimiter=',')
    #writer = csv.writer('t_mapper.csv', delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        print(line)
        

        if len(line) == 22:
            a1,UNIT,DATEn,TIMEn,Hour,DESCn,ENTRIESn_hourly,EXITSn_hourly = line[:8]
            maxpressurei,maxdewpti,mindewpti,minpressurei,meandewpti,meanpressurei = line[8:14]
            fog,rain,meanwindspdi,mintempi,meantempi,maxtempi,precipi,thunder = line[14:]
            
            line_str = UNIT, '\t', ENTRIESn_hourly
            print(line_str)
            #writer.writerow("{0}\t{1}".format(UNIT, ENTRIESn_hourly))

def sort_list():
    for line in sorted(sys.stdin):
        print(line)

def reducer():

    total = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            continue

        thisKey, value = data_mapped

        if oldKey and oldKey != thisKey:
            print(oldKey, "\t", total)
            oldKey = thisKey;
            total = 0

        oldKey = thisKey
        total += float(value)

    if oldKey != None:
        print(oldKey, "\t", total)

def main():
    mapper()
    #sort_list()
    #reducer()
	
main()