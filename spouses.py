"""
Configuration class for Kringle spouses.
If a user has a spouse listed the spouse will not be assigned to that user.
"""

from file_worker import FileWorker
from participants import ConfigureParticipants


class ConfigureSpouses(object):
    """ Add and edit methods for spouses. """
    participants = []
    unassigned = []

    def __init__(self):
        self.spouses = FileWorker().readfile('spouses.json', 'dictionary')

    def is_configured(self):
        if self.spouses:
            return True
        else:
            return False

    def prepare_to_add_spouses(self):
        self.participants = ConfigureParticipants.get_participants()
        self.unassigned = self.participants
        self.unassigned.append('None')
        self.configure_spouses()

    def configure_spouses(self):
        self.clear()
        self.get_header()
        print ''
        print 'Associate spouse with participant'
        for index, participant in enumerate(self.unassigned):
            print "{0:3} {1}".format(index, participant)
        for name in self.unassigned:
            spouse = int(raw_input('%s spouse: ') % name)
            self.add_spouse(spouse, name)

    def add_spouse(self, spouse, name):
        self.spouses[spouse] = name
        self.spouses[name] = spouse
        del self.unassigned[spouse]
        del self.unassigned[name]
        self.configure_spouses()

    @staticmethod
    def get_header():
        print "                                      `}-'       `}-"
        print " ___                    `}-' `}-'  ____/`-,  _____/`-,"
        print "\"-_/}__             `}-'_/`-, /`-,( _,,.{-,_(__,,,.("
        print "  [(_.-'`--,__   ____/`-,.(,-`}-'_,>___\/`-, >|`---\\"
        print "  [(__\___\  _`-(--...(..-'_`./`-,/(--,,.(  //    / >"
        print "  |_______/-'    >`---\ / (   `{    >`---\    tc"
        print "                         /  \/  \\"
