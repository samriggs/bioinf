'''
Created on Oct 15, 2013

@author: samriggs
CODE CHALLENGE: Solve the Reverse Complement Problem.
'''

from bi_utils.helpers import sane_open

with sane_open("stepic_dataset.txt") as f:
    # [::-1] is a way to use string slicing syntax to reverse strings.
    print (f.readline()[::-1])
    