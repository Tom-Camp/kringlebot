"""
Configuration class for Kringle participants.
"""

from file_worker import FileWorker
import os


class ConfigureParticipants(object):
    """ Update and edit methods. """
    participants = []

    def __init__(self):
        self.participants = FileWorker().readfile('participants.json', 'list')
        self.is_configured()

    def get_participants(self):
        return self.participants

    def is_configured(self):
        if len(self.participants) > 0:
            return True
        else:
            self.configure_participants()

    def list_participants(self):
        for participant in self.participants:
            print participant

    def configure_participants(self):
        self.clear()
        self.get_header()
        print ''
        print "It looks like you haven't added any participants."
        print 'Add some names below.'
        print ''
        print 'Enter "x" to save list.'
        print '-----------------------'
        for p in self.participants:
            print p
        self.add_participants()

    def add_participants(self):
        participant = raw_input('Name? ')
        if participant == 'x':
            FileWorker().writefile('participants.json', self.participants)
        else:
            self.participants.append(participant)
            self.configure_participants()

    def edit_participants(self):
        pass

    @staticmethod
    def get_header():
        print " {_} {_}        {_} {_}        {_} {_}        {_} {_}  |-|() |-|() |-|()"
        print "'-=\'-=\       '-=\'-=\       '-=\'-=\       '-=\'-=\          #  &"
        print "   \\__\\____(    \\__\\____(    \\__\\____(    \\__\\____(   [_]@(x)<="
        print "  _|/-_|/---\\_  _|/-_|/---\\_  _|/-_|/---\\_  _|/-_|/---\\_   \[_]____"
        print "  \   \        \ \   \        \ \   \       \ \   \        \    __|___'"

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
