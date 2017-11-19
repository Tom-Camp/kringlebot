"""Docstring for the kringle"""

import datetime
from file_worker import FileWorker
from kringlecalc import kriskringle


class pickKringle(object):
    """ Try to assign Kris Kringles. """
    def __init__(self):
        kris_kringle = kriskringle()
        recipients = kris_kringle.assign_recipient_list()

        self.write_this_years_file(recipients)
        self.display_kringles(recipients)

    def display_kringles(self, recipients):
        """ Show the results. """
        print '{0:14} {1}'.format('Kringle', 'Recipient')
        print '=========================='
        for kringle, recip in recipients.iteritems():
            print '{0:14} {1}'.format(kringle, recip)

    def write_this_years_file(self, recipients):
        """ Write the recipients to this year's file. """
        year = datetime.datetime.now().year
        filename = 'kringles' + str(year) + '.json'
        FileWorker().writefile(filename, recipients)
