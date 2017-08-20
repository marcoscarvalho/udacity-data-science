#!/usr/bin/python

import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(",")

        if data[0] == '':
            continue

        if len(data) == 22:
            a1,UNIT,DATEn,TIMEn,Hour,DESCn,ENTRIESn_hourly,EXITSn_hourly = data[:8]
            maxpressurei,maxdewpti,mindewpti,minpressurei,meandewpti,meanpressurei = data[8:14]
            fog,rain,meanwindspdi,mintempi,meantempi,maxtempi,precipi,thunder = data[14:]

            #print "{0}\t{1}".format(UNIT, ENTRIESn_hourly)

mapper()