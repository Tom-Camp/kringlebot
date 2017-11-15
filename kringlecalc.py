"""
Assign a recipient to a Kris Kringle making sure that it isn't the Kringe,
the Kringle's spouse, or the Kringle's recipient from last year.
"""

import datetime
import json
from random import randint

class kriskringle(object):
    """ Assign a recipient to a Kris Kringle"""

    kringle = ''
    kris_kringles = {}
    key = ''
    recipient = ''

    def __init__(self):
        self.set_participants()
        self.set_recipient_list()
        self.set_spouses()
        self.set_previous_recipient_list()

    def assign_recipient_list(self):
        """ Try to assign a recipient to a Kris Kringle. """
        for kringle in self.participants:
            print self.participants
            try:
                self.kris_kringles[kringle] = self.set_recipient_for_kringle(kringle)
            except ValueError as e:
                if kringle == self.participants[-1]:
                    self.__init__()
                else:
                    self.participants.insert(len(self.participants), kringle)

        return self.kris_kringles

    def set_participants(self):
        """ Read the participants from a json file. """
        try:
            with open('participants.json', "r") as json_data:
                self.participants = json.load(json_data)
        except Exception:
            print "Unable to open participants.json."

    def set_recipient_list(self):
        """ Create the recipient_list list. """
        try:
            with open('participants.json', "r") as json_data:
                self.recipient_list = json.load(json_data)
        except Exception:
            print "Unable to open participants.json."

    def set_spouses(self):
        """ Create the spouses dictionary. """
        try:
            with open('spouses.json', "r") as json_data:
                self.spouses = json.load(json_data)
        except Exception:
            print "Unable to open spouses.json."

    def set_previous_recipient_list(self):
        """ Create the previous recipient_list dictionary. """
        last_year = datetime.datetime.now().year - 1
        filename = 'kringles' + str(last_year) + '.json'
        try:
            with open(filename, "r") as json_data:
                self.previousKringles = json.load(json_data)
        except Exception:
            self.previousKringles = {}
            print "Unable to open %s" % filename

    def set_recipient_for_kringle(self, kringle):
        """ Try to assign a recipient to a kringle. """
        self.kringle = kringle
        self.get_recipient()
        if self.check_previous_recipient():
            raise ValueError('Previous Recipient for %s' % self.kringle)
        elif self.check_spouses():
            raise ValueError('Spouse for %s' % self.kringle)
        elif self.check_self():
            raise ValueError('Self for %s' % self.kringle)
        else:
            del self.recipient_list[self.key]
            return self.recipient

    def get_recipient(self):
        """ Get a recipient from the recipient_list list. """
        self.key = randint(0, len(self.recipient_list) - 1)
        self.recipient = self.recipient_list[self.key]

    def check_previous_recipient(self):
        """ Check if the recipient was the kringles recipient last year. """
        if self.recipient == self.previousKringles[self.kringle]:
            print 'Prev error: %s %s' % (self.kringle, self.recipient)
            return True

    def check_spouses(self):
        """ Check if the recipient is the kringles spouse. """
        if self.kringle in self.spouses and self.recipient == self.spouses[self.kringle]:
            print 'Spouse error: %s %s' % (self.kringle, self.recipient)
            return True

    def check_self(self):
        """ Check if the recipient is the kringle. """
        if self.kringle == self.recipient:
            print 'Self error: %s %s' % (self.kringle, self.recipient)
            return True
