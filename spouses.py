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
        self.participants = ConfigureParticipants().get()
        self.unassigned = self.participants
        self.unassigned.append('None')
        self.configure()

    def configure(self):
        Helpers().clear()
        Helpers().get_header()
        print ''
        print 'Associate spouse with participant'
        print 'Enter "x" to save and return to Main Menu.'

        if len(self.unassigned) == 1:
            FileWorker().writefile('spouses.json', self.spouses)
            Helpers().restart()

        for index, participant in enumerate(self.unassigned):
            if index > 0:
                print "{0:3} {1}".format(index, participant)
        spouse = raw_input('Spouse for %s: ' % self.unassigned[0])
        self.add(spouse)

    def add(self, spouse):
        if self.unassigned[int(spouse)] == 'None':
            del self.unassigned[0]
        elif spouse == 'x':
            FileWorker().writefile('spouses.json', self.spouses)
            Helpers().restart()
        else:
            self.spouses[self.unassigned[int(spouse)]] = self.unassigned[0]
            self.spouses[self.unassigned[0]] = self.unassigned[int(spouse)]
            del self.unassigned[int(spouse)]
            del self.unassigned[0]
        self.configure()

    def edit(self):
        Helpers.clear()
        Helpers.get_header()
