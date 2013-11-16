'''
Created on Nov 11, 2013

@author: samriggs

CODE CHALLENGE: Solve the Clump Finding Problem.
https://beta.stepic.org/Bioinformatics-Algorithms-2/An-Explosion-of-Hidden-Messages-4/#step-4
'''
from bi_utils.helpers import sane_open
from collections import defaultdict
from ClumpTracker import ClumpTracker
from cStringIO import StringIO

# File exists & is not empty. let's go to work. Exit otherwise.
def find_clumps(dataset='', k='', L='', t='', countClumps=False):
    if (not dataset):
        dataset = "stepic_dataset.txt"    
    
    with sane_open(dataset) as f:
        # We will assume the file is well formed.
        seq = f.readline()
        params = f.readline().split()
        
        if (int(k) > 0):
            seqSize = int(k)
        else:
            seqSize = int(params[0])
        
        if (int(L) > 0):
            windowSize = int(L)
        else:        
            windowSize = int(params[1])
            
        if (int(t) > 0):
            clumpNum = t
        else:      
            clumpNum = int(params[2])
        
        # Making this dictionary is O(n). parse all sequences
        seqDict = defaultdict(int)
        i = 0
        while ( len(seq[i:seqSize+i]) is seqSize ):
            currentSeq = seq[i:seqSize+i]
            currentTracker = seqDict[currentSeq]
            if ( currentTracker == 0 ):
                seqDict[currentSeq] = ClumpTracker(currentSeq, i, seqSize, windowSize, clumpNum)
            else:
                currentTracker.updateClump(currentSeq, i)
            i += 1
            
        if ( countClumps ):
            clumps = 0
            for s, t in seqDict.iteritems():
                if t.fits is True:
                    clumps += 1
            print clumps
        else:  
            file_str = StringIO()
            for s, t in seqDict.iteritems():
                if t.fits is True:
                    file_str.write(s)
                    file_str.write(" ")
            
            print file_str.getvalue().strip()

if (__name__ == "__main__"):
    find_clumps()