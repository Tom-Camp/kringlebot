"""
Configuration class for Kringle spouses.
If a user has a spouse listed the spouse will not be assigned to that user.
"""

from file_worker import FileWorker
from participants import ConfigureParticipants
from helpers import Helpers


class ConfigureSpouses(object):
    """ Add and edit methods for spouses. """
    participants = []
    unassigned = []

    def __init__(self):
        self.spouses = FileWorker().readfile('spouses.json', 'dictionary')

    def get(self):
        if self.is_configured():
            return self.spouses

    def is_configured(self):
        if self.spouses:
            return True
        else:
            return False

    def prepare_to_add(self):
        self.participants = ConfigureParticipants.get()
        self.unassigned = self.participants
        self.unassigned.append('None')
        self.configure()

    def configure(self):
        Helpers().clear()
        Helpers().get_header()
        print ''
        print 'Associate spouse with participant'
        for index, participant in enumerate(self.unassigned):
            print "{0:3} {1}".format(index, participant)
        spouse = int(raw_input('%s spouse: ') % self.unassigned[0])
        self.add(spouse, self.unassigned[0])

    def add(self, spouse, kringle):
        if spouse == 'None':
            del self.unassigned[kringle]
        else:
            self.spouses[spouse] = kringle
            self.spouses[kringle] = spouse
            del self.unassigned[spouse]
            del self.unassigned[kringle]
        self.configure()

    def edit(self):
        Helpers.clear()
        Helpers.get_header()
