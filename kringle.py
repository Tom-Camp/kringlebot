#!/usr/bin/python
"""Docstring for the kringle"""

import sys
import datetime
import json
from kringlecalc import kriskringle

def main():
    """docstring"""
    kk = kriskringle()
    recipients = kk.assign_recipient_list()
    writeThisYearsFile(recipients)
    print recipients

def writeThisYearsFile(recipients):
    print len(recipients)
    year = datetime.datetime.now().year
    filename = 'kringles' + str(year) + '.json'
    try:
        with open(filename, 'w+') as json_data:
            json.dump(recipients, json_data)
    except:
        print 'Error writing file.'

if __name__ == "__main__":
    sys.exit(main())
