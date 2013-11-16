'''
Created on Nov 12, 2013

@author: samriggs

EXERCISE BREAK: Give all values of Skew(Prefix_i (GAGCCACCGCGATA)) for i ranging from 0 to 14.
https://beta.stepic.org/Bioinformatics-Algorithms-2/Peculiar-Statistics-of-the-Forward-and-Reverse-Half-Strands-7/#step-4
'''

from bi_utils.helpers import sane_open
from cStringIO import StringIO

def skew_list(dataset=''):
    if (not dataset):
        dataset = 'stepic_dataset.txt'
        
    with sane_open(dataset) as f:
        i = 0
        file_str = StringIO()
        for c in f.readline():
            file_str.write(str(i))
            file_str.write(' ')
            if (c == "C"):
                i -= 1
            elif (c == "G"):
                i += 1
    # print final skew status
    file_str.write(str(i))
                
    print file_str.getvalue()

if (__name__ == "__main__"):
    skew_list("")