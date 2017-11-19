"""
Check configuration. If it isn't configured correctly, run the configuration.
"""

from participants import ConfigureParticipants
from spouses import ConfigureSpouses
import os


class KringleConfig(object):
    """ Configuration functions for Kringling. """
    participants = False
    spouses = False
    menu_items = []

    def __init__(self):
        self.clear()
        self.check_participants()
        self.check_spouses()
        self.create_menu()

    def check_participants(self):
        participants = ConfigureParticipants()
        if participants:
            self.participants = True;

    def check_spouses(self):
        self.spouses = ConfigureSpouses().is_configured()

    def create_menu(self):
        if self.participants:
            self.menu_items.append('List participants')
            self.menu_items.append('Add participants')
            self.menu_items.append('Edit participants')

        if self.spouses:
            self.menu_items.append('Edit spouses')
        else:
            self.menu_items.append('Edit spouses')

        self.show_menu()

    def show_menu(self):
        for index, item in enumerate(self.menu_items):
            print '%i) %s' % (index + 1, item)

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

