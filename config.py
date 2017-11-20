"""
Check configuration. If it isn't configured correctly, run the configuration.
"""

from participants import ConfigureParticipants
from helpers import Helpers


class KringleConfig(object):
    """ Configuration functions for Kringling. """
    def __init__(self):
        Helpers().clear()
        ConfigureParticipants()

