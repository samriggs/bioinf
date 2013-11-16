'''
Created on Nov 13, 2013

@author: samriggs

CODE CHALLENGE: Solve the Approximate Pattern Matching Problem.
https://beta.stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Elusive-than-Others-9/#step-3
'''
import itertools

from bi_utils.helpers import sane_open
from cStringIO import StringIO

def approxPMP(dataset=''):
    if (not dataset):
        dataset = "stepic_dataset.txt"
        
    with sane_open(dataset) as f:
        pattern = f.readline().rstrip()
        fullSequence = f.readline().rstrip()
        maxMismatches = int(f.readline())
        
        pLength = len(pattern)
        
        fileStr = StringIO()
        for i in range(len(fullSequence)):
            if ( num_mm(fullSequence[ i:pLength+i ], pattern) <= maxMismatches ):
                fileStr.write( str(i) )
                fileStr.write(" ")
                
        print fileStr.getvalue().strip()
            
'''
source for the simultaneous string iteration:
http://stackoverflow.com/questions/1663807/how-can-i-iterate-through-two-lists-in-parallel-in-python

return the # of differences in two strings.
'''
def num_mm(s1, s2):
    # if one string is shorter than the other, then the delta counts.
    count = abs(len(s1) - len(s2))
    for i, j in itertools.izip(s1, s2):
        if i != j:
            count += 1
            
    return count
        
approxPMP("dataset_8_3.txt")