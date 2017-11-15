#KringleCalc.py

import datetime
import json
from random import randint

class kriskringle(object):
    """ Assign a recipient to a Kris Kringle"""

    def __init__(self):
        self.setRecipients()
        self.setParticipants()
        self.setSpouses()
        self.setPreviousKringles()

    def assignRecipients(self):
        for kringle in self.participants:
            try:
                self.setRecipientForKringle(kringle)
            except ValueError as e:
                self.participants.append(kringle)

    def setRecipients(self):
        try:
            with open('recipients.json', "r") as json_data:
                self.participants = json.load(json_data)
        except Exception:
            print "Unable to open recipients.json."

    def setParticipants(self):
        self.recipients = self.participants

    def setSpouses(self):
        try:
            with open('spouse.json', "r") as json_data:
                self.spouses = json.load(json_data)
        except Exception:
            print "Unable to open spouses.json."

    def setPreviousKringles(self):
        lastYear = datetime.datetime.now().year - 1
        filename = 'kringles' + str(lastYear) + '.json'
        try:
            with open(filename, "r") as json_data:
                self.previousKringles = json.load(json_data)
        except Exception:
            self.previousKringles = {}
            print "Unable to open %s" % filename

    def setRecipientForKringle(self, kringle):
        self.kringle = kringle
        self.getRecipient()
        if self.checkPreviousYear() == True:
            raise ValueError('Previous Recipient for %s' % self.kringle)
        elif self.checkSpouses() == True:
            raise ValueError('Spouse for %s' % self.kringle)
        elif self.checkSelf() == True:
            raise ValueError('Self for %s' % self.kringle)
        else:
            del(self.recipients[self.key])
            return self.recipient

    def getRecipient(self):
        self.key = randint(0,len(self.recipients) - 1)
        self.recipient = self.recipients[self.key]

    def checkSpouses(self):
        if self.kringle in self.spouses and self.recipient == self.spouses[self.kringle]:
            print 'Spouse error: %s %s' % (self.kringle, self.recipient)
            return True

    def checkSelf(self):
        if self.kringle == self.recipient:
            print 'Self error: %s %s' % (self.kringle, self.recipient)
            return True

    def checkPreviousYear(self):
        if self.recipient == self.previousKringles[self.kringle]:
            print 'Prev error: %s %s' % (self.kringle, self.recipient)
            return True
