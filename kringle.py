#!/usr/bin/python
"""Docstring for the kringle"""

import sys
import datetime
import json
from KringleCalc import KrisKringle

PARTICIPANTS = [
    "Sumter",
    "Sherry",
    "Fran",
    "John",
    "Laura Jean",
    "Mary Heather",
    "Rich",
    "Kathryn",
    "Tom",
    "Adriane"
]

def main():
    """docstring"""
    recipients = {}
    kk = KrisKringle()
    print PARTICIPANTS
    for kringle in PARTICIPANTS:
        try:
            recipients[kringle] = kk.setRecipientForKringle(kringle)
        except ValueError as e:
            PARTICIPANTS.append(kringle)
            print PARTICIPANTS

    writeThisYearsFile(recipients)

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
