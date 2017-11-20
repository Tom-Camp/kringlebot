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
        if self.participants:
            print '-----------------------'
            prompt = 'another '
        else:
            prompt = ''
        participant = raw_input('Add %sparticipant >> ' % prompt)
        if participant == 's':
            FileWorker().writefile('participants.json', self.participants)
            Helpers().restart()
        elif participant == 'x':
            Helpers().restart()
        else:
            self.participants.append(participant)
            self.configure()

    def add_additional(self):
        Helpers().clear()
        Helpers().get_header()
        print 'Add additional participants below.'
        print ''
        print 'Enter "s" to save list or "x" to cancel.'
        print '-----------------------'
        print ''
        for p in self.participants:
            print p
        self.add()

    def edit(self):
        Helpers().clear()
        Helpers().get_header()
        for index, kringle in enumerate(self.participants):
            print '%i) %s' % (index + 1, kringle)
        print ''
        print 'Enter the number to edit or "x" to Save and return to Main Menu'
        participant = raw_input('>> ')
        self.edit_participant(participant)

    def edit_participant(self, participant):
        if participant == 'x':
            FileWorker().writefile('participants.json', self.participants)
            Helpers().restart()
        elif participant.isdigit():
            print 'Enter "u" to update or "d" to delete user %s' % self.participants[int(participant) - 1]
            print 'Enter "x" to return to the Edit menu.'
            print ''
            option = raw_input('>> ')
            self.update_delete_participant(int(participant) - 1, option)
        else:
            self.edit()

    def update_delete_participant(self, participant, option):
        if option == 'x' or option == 'X':
            self.edit()
        elif option == 'u' or option == 'U':
            user = self.participants[participant]
            updated = raw_input('Edit user: %s' % user + chr(8) * len(user))
            del self.participants[participant]
            self.participants.append(updated)
            self.edit()
        elif option == 'd' or option == 'D':
            del self.participants[participant]
            self.edit()
        else:
            self.edit()

