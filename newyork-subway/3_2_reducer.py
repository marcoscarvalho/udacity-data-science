#!/usr/bin/python

import sys

def reducer():

    total = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            continue

        thisKey, value = data_mapped

        if oldKey and oldKey != thisKey:
            print oldKey, "\t", total
            oldKey = thisKey;
            total = 0

        oldKey = thisKey
        total += float(value)

    if oldKey != None:
        print oldKey, "\t", total


reducer()