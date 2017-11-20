"""
Helper and reused methods.
"""

import os


class Helpers(object):
    """ Helper methods. """
    @staticmethod
    def return_to_menu():
        try:
            os.system('pause')
        except WindowsError:
            os.system('read -p "Press any key to continue"')

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def restart():
        os.execl('./startup.py', 'startup.py')

    @staticmethod
    def get_header():
        print """
         __.----.
      _.'        `-.
     /    _____     `-.
    /_.-""     ""-._   \\
    ."   _......._   ".  \\
    ; .-' _ ))) _ `-. ;   |
    `/  ." _   _ ".  \\'.  /
    _|  .-.^ ) ^.-.  |_ \/-.
    \ `"==-.(_).-=="' //    \\
     `.____.-^-.____.' \    /
     |     \`-'/    |   `--'
      \     `       /
       `.         .'
         `-.....-'"""

