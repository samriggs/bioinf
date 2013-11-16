'''
Created on Oct 14, 2013

CODE CHALLENGE: Solve the Frequent Words Problem.
https://beta.stepic.org/Bioinformatics-Algorithms-2/Hidden-Messages-in-the-Replication-Origin-2/#step-4
@author: samriggs
'''
from bi_utils.helpers import sane_open
from collections import defaultdict
from heapq import heappop, heapify
import sys

# File exists & is not empty. let's go to work. Exit otherwise.
def freqSeqs(fullSeq='', seqLength='', returnHeap=True):
    if (not fullSeq or not seqLength):
        # We will assume the file is well formed.
        with sane_open("stepic_dataset.txt") as f:
            seq = f.readline()
            size = int(f.readline())
    else:
        seq = fullSeq
        size = int(seqLength)

    # populate sequences and count the # of times.
    # need to count negatively b/c Python only has a minheap.    
    # Making this dictionary is O(n)    
    seq_dict = defaultdict(int)
    i = 0
    while ( len(seq[i:size+i]) == size ):
        seq_dict[seq[i:size+i]] -= 1
        i += 1

    # create min heap: O(n)
    '''
    Need to reverse all tuples inside list (O(n)) SO THAT THE NUMBERS ARE FIRST;
    this allows for a heap to be made off the tuples
    '''
    if (returnHeap):
        min_heap = [tuple(reversed(x)) for x in seq_dict.items()]
        heapify( min_heap )
        return min_heap
    else:
        return seq_dict
    
def mostCommon(minh):
    most_common_val = minh[0][0]
    current_item = heappop(minh)
    while (current_item[0] == most_common_val):
        sys.stdout.write(current_item[1] + " ")
        current_item = heappop(minh)

if (__name__ == "__main__"):
    print mostCommon(freqSeqs())