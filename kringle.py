#!/usr/bin/python
"""Docstring for the kringle"""

import sys
import datetime
import json
from kringlecalc import kriskringle

def main():
    """ Try to assign Kris Kringles. """
    kris_kringle = kriskringle()
    recipients = kris_kringle.assign_recipient_list()

    write_this_years_file(recipients)
    display_kringles(recipients)

def display_kringles(recipients):
    """ Show the results. """
    for kringle, recip in recipients.iteritems():
        print '%s giving to %s' % (kringle, recip)

def write_this_years_file(recipients):
    """ Write the recipients to this year's file. """
    year = datetime.datetime.now().year
    filename = 'kringles' + str(year) + '.json'
    try:
        with open(filename, 'w+') as json_data:
            json.dump(recipients, json_data)
    except Exception:
        print 'Error writing file.'

if __name__ == "__main__":
    sys.exit(main())
