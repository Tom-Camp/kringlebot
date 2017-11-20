"""
Class for creating and handling the main menu.
"""

from participants import ConfigureParticipants
from spouses import ConfigureSpouses
from pick_kringle import pickKringle
from helpers import Helpers
import sys


class MainMenu(object):
    """ Create and manage main menu. """
    participants = False
    spouses = False
    menu_items = []
    error_message = ''

    def __init__(self):
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
            self.menu_items.append('Add spouses')

        self.show_menu()

    def show_menu(self):
        self.menu_items.append('Exit')
        Helpers().clear()
        Helpers().get_header()
        print self.error_message
        for index, item in enumerate(self.menu_items):
            print '%i) %s' % (index + 1, item)
        option = int(input('Enter the item number: '))
        self.confirm_selection(option)

    def confirm_selection(self, option):
        item_count = len(self.menu_items)
        if option > item_count:
            self.error_message = 'Invalid menu option'
        else:
            self.action(option - 1)

    def action(self, option):
        action = self.menu_items[option]
        if action == 'List participants':
            Helpers().clear()
            Helpers().get_header()
            ConfigureParticipants().list()
            raw_input('Press "Enter" to continue.')
            Helpers().restart()
        elif action == 'Add participants':
            ConfigureParticipants().add_additional()
        elif action == 'Edit participants':
            ConfigureParticipants().edit()
        elif action == 'Edit spouses':
            ConfigureSpouses().edit()
        elif action == 'Add spouses':
            ConfigureSpouses().prepare_to_add()
        else:
            sys.exit(0)
