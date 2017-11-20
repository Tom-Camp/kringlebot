#!/usr/bin/env python

import sys
from main_menu import MainMenu
from config import KringleConfig


def main():
    KringleConfig()
    MainMenu()

if __name__ == "__main__":
    sys.exit(main())