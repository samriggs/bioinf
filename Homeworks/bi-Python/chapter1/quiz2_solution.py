'''
Created on Oct 15, 2013

@author: samriggs
CODE CHALLENGE: Solve the Reverse Complement Problem.
'''

from bi_utils.helpers import sane_open
from cStringIO import StringIO

def revComp(stringToRC):
        # [::-1] is a way to use string slicing syntax to reverse strings.
    revSeq = stringToRC[::-1]
    # now complement.
    compRevSeq = StringIO()
    for c in revSeq:
        if c is "A": compRevSeq.write("T")
        elif c is "C": compRevSeq.write("G")
        elif c is "G": compRevSeq.write("C")
        elif c is "T": compRevSeq.write("A")
    return compRevSeq.getvalue()

if __name__ ==  "__main__":
    with sane_open("stepic_dataset.txt") as f:
        print revComp(f.readline())