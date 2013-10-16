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
with sane_open("stepic_dataset.txt") as f:
    # We will assume the file is well formed.
    seq = f.readline()
    size = int(f.readline())
    
    # populate sequences and count the # of times.
    # need to count negatively b/c Python only has a minheap.
    
    # Making this dictionary is O(n)
    seq_dict = defaultdict(int)
    start = 1
    end = size + 1
    while ( len(seq[start:end]) is size ):
        seq_dict[seq[start:end]] -= 1 
        start += 1
        end += 1

    # create min heap: O(n)
    '''
    Need to reverse all tuples inside list (O(n)) SO THAT THE NUMBERS ARE FIRST;
    this allows for a heap to be made off the tuples
    '''
    min_heap = [tuple(reversed(x)) for x in seq_dict.items()]
    heapify( min_heap )
    
    most_common_val = min_heap[0][0]
    current_item = heappop(min_heap)
    while (current_item[0] == most_common_val):
        sys.stdout.write(current_item[1] + "    ")
        current_item = heappop(min_heap)
    # pull only while 
        
