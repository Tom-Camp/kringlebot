"""
Configuration class for Kringle participants.
"""

from file_worker import FileWorker
from helpers import Helpers


class ConfigureParticipants(object):
    """ Update and edit methods. """
    participants = []

    def __init__(self):
        self.participants = FileWorker().readfile('participants.json', 'list')
        self.is_configured()

    def get(self):
        if self.is_configured():
            return self.participants

    def is_configured(self):
        if len(self.participants) > 0:
            return True
        else:
            self.configure()

    def list(self):
        print "\n".join(self.participants)

    def configure(self):
        Helpers().clear()
        Helpers().get_header()
        print ''
        print "It looks like you haven't added any participants."
        print 'Add some participants below.'
        print ''
        print 'Enter "x" to save list.'
        print '-----------------------'
        for p in self.participants:
            print p
        self.add()

    def add(self):
        participant = raw_input('Name? ')
        if participant == 'x':
            FileWorker().writefile('participants.json', self.participants)
            Helpers().restart()
        else:
            self.participants.append(participant)
            self.configure()

    def add_additional(self):
        Helpers().clear()
        Helpers().get_header()
        print 'Add additional participants below.'
        print ''
        print 'Enter "x" to save list.'
        print '-----------------------'
        for p in self.participants:
            print p
        self.add()

    def edit(self):
        Helpers().clear()
        Helpers().get_header()
        for index, kringle in enumerate(self.participants):
            print '%i) %s' % (index + 1, kringle)
        print 'Enter the number to edit or "x" to Save and return to Main Menu'
        participant = raw_input('>> ')
        self.edit_participant(participant)

    def edit_participant(self, participant):
        if participant == 'x':
            FileWorker().writefile('participants.json', self.participants)
            Helpers().restart()
        elif participant.isdigit():
            user = self.participants[int(participant) - 1]
            updated = raw_input('Edit user: %s' % user + chr(8) * len(user))
            del self.participants[int(participant) - 1]
            self.participants.append(updated)
            self.edit()
        else:
            self.edit()
