"""Docstring for the kringle"""

import datetime
import sys
from file_worker import FileWorker
from kringlecalc import kriskringle


def main():
    """ Try to assign Kris Kringles. """
    kris_kringle = kriskringle()
    recipients = kris_kringle.assign_recipient_list()

    write_this_years_file(recipients)
    display_kringles(recipients)


def display_kringles(recipients):
    """ Show the results. """
    print '{0:14} {1}'.format('Kringle', 'Recipient')
    print '=========================='
    for kringle, recip in recipients.iteritems():
        print '{0:14} {1}'.format(kringle, recip)


def write_this_years_file(recipients):
    """ Write the recipients to this year's file. """
    year = datetime.datetime.now().year
    filename = 'kringles' + str(year) + '.json'
    FileWorker().writefile(filename, recipients)


if __name__ == "__main__":
    sys.exit(main())
