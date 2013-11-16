'''
Created on Nov 11, 2013

@author: samriggs
'''
from collections import deque

class ClumpTracker():
    '''
    Contains:
    * the particular k-mer to track
    * number of sequences in the clump
    * a queue that holds the indices of the subsequences
    '''


    def __init__(self, subSeq, subSeqIndex, subSeqLen, windowSize, maxNumSeq):
        '''
        Constructor
        '''
        self.subSeq = subSeq
        self.currentClumpWidth = len(subSeq)
        
        self.seqQueue = deque()
        self.seqQueue.append(subSeqIndex)
        
        self.seqLength = subSeqLen
        self.window = windowSize
        self.numSeq = maxNumSeq
        
        self.fits = False
        
    def __str__(self):
        return str(self.seqQueue)

    '''
    subSeqStart is where the subsequence is in the given string
    windowSize is L
    maxNumSeq is t
    '''    
    def updateClump(self, subSeq, subSeqIndex):
        # base case #0: If the current clump fits, we should not update at all.
        if (self.fits):
            return 0
        # induction step
        else:
            # part one: window size not reached yet.
            if (len(self.seqQueue) < self.numSeq):
                self.seqQueue.append(subSeqIndex)
            elif (len(self.seqQueue) == self.numSeq):
                self.seqQueue.popleft()
                self.seqQueue.append(subSeqIndex)
            '''
            update the width of the current window: 
            most recent index - least recent index + sequence length
            '''
            self.currentClumpWidth = (
                self.seqQueue[-1] - self.seqQueue[0] + self.seqLength)
            self.fitCheck()
            return self.currentClumpWidth
    '''
    Mark the sequence as fitting a (L, t) clump
    (denoted by windowSize and maxNumSeq, respectively)
    only if the batch of sequences are at most t and where the clump size is
    within L.
    '''
    def fitCheck(self):
        if ((len(self.seqQueue) == self.numSeq) and 
            (self.currentClumpWidth <= self.window)):
            self.fits = True
        else:
            self.fits = False