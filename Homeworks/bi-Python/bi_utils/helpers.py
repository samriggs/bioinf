'''
Created on Oct 14, 2013

@author: samriggs
'''

import os

"""
patially sourced from
http://stackoverflow.com/questions/2507808/python-how-to-check-file-empty-or-not

Returns true if and only if the file exists and is non-empty. Returns false
otherwise.
@param path the path of the file
"""
def sane_open(path):
    if ( os.path.exists(path) is False ):
        print ("The file " + path + " does not exist")
        exit(1)
    elif ( os.stat(path).st_size == 0 ):
        print (path + " is an empty file.")
        exit(1)
    return open(path, 'r')