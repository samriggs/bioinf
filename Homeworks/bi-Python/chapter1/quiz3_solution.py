'''
Created on Oct 16, 2013

@author: samriggs

CODE CHALLENGE: Solve the Pattern Matching Problem (restated below).
https://beta.stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Surprising-than-Others-3/#step-5
'''

from bi_utils.helpers import sane_open
import sys

def p_match(filename="stepic_dataset.txt", pat=''):
    with sane_open(filename) as f:
        # Python WILL match newlines. so get rid of them.
        if (pat is ''):
            pattern = f.readline().rstrip('\n')
        else:
            pattern = pat
        seq = f.readline().rstrip('\n')
        start = 1
        index = 0 
        last_index = 0
        
        while (start + len(pattern) < len(seq)):
            # get the index of the first match
            index = seq.find(pattern, start)
            # exit if no matches found at all
            if index < 0:
                break
            # update last_index if a new one found, and print it out.
            if (last_index < index):
                # preceding space only if it's not the first match
                if (last_index is not 0): sys.stdout.write(" ")
                sys.stdout.write(str(index))
                last_index = index
            
            if start < last_index:
                start = last_index
            else:
                start += 1

if (__name__ == "__main__"):
    p_match()