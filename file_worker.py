"""
Read and write files.
"""

import json


class FileWorker(object):
    """ A class to read and write files. """

    def __init__(self):
        pass

    def readfile(self, filename):
        try:
            with open('files/' + filename, "r+") as json_data:
                return json.load(json_data)
        except Exception:
            print "Unable to open %s" % filename

    def writefile(self, filename, data):
        try:
            with open('files/' + filename, 'w+') as json_data:
                json.dump(data, json_data)
        except Exception:
            print 'Error writing file.'
            return {}
