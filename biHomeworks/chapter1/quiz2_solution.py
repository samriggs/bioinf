'''
Created on Oct 15, 2013

@author: samriggs
CODE CHALLENGE: Solve the Reverse Complement Problem.
'''

from bi_utils.helpers import sane_open
from cStringIO import StringIO

with sane_open("stepic_dataset.txt") as f:
    # [::-1] is a way to use string slicing syntax to reverse strings.
    rev_seq = f.readline()[::-1]
    # now complement.
    comp_rev_seq = StringIO()
    for i in range(1, len(rev_seq)):
        if rev_seq[i] is "A": comp_rev_seq.write("T")
        elif rev_seq[i] is "C": comp_rev_seq.write("G")
        elif rev_seq[i] is "G": comp_rev_seq.write("C")
        elif rev_seq[i] is "T": comp_rev_seq.write("A")
    print comp_rev_seq.getvalue()
    