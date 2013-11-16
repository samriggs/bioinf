'''
Created on Nov 14, 2013

@author: samriggs

CODE CHALLENGE: Solve the Frequent Words with Mismatches Problem.
https://beta.stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Elusive-than-Others-9/#step-4

CODE CHALLENGE: Solve the Frequent Words with Mismatches and Reverse Complements Problem.
https://beta.stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Elusive-than-Others-9/#step-5
'''
from bi_utils.helpers import sane_open
from collections import defaultdict
from itertools import combinations
from heapq import heapify
from quiz2_solution import revComp
from quiz1_solution import freqSeqs, mostCommon

'''
Solve said problem.
'''
def freqFuzzyMatch(dataset, revC=False):
    parsedInput = dataset.split()
    fullSeq = parsedInput[0]
    seqLen = int(parsedInput[1])
    maxMismatches = int(parsedInput[2])
    
    
    # calculate the most frequent sequences
    freqSeqDict = freqSeqs(fullSeq, seqLen, False)
    
    # make a mismatches / reverse complement mismatches dictionary
    mismatchDict = dict()
    for s in freqSeqDict:
        mismatchDict[s] = genMutations(s, maxMismatches)
        if (revC):
            mismatchDict[s].extend(genMutations(revComp(s), maxMismatches))
    
    # count the tally in a separate dictionary:
    fuzzyDict = defaultdict(int)
    for seq, frequency in freqSeqDict.iteritems():
        for mismatch in mismatchDict[seq]:
            fuzzyDict[mismatch] += frequency
        fuzzyDict[seq] += frequency
            
            
    # Now min heapify the fuzzy matching dictionary, like quiz 1.
    minHeap = [tuple(reversed(x)) for x in fuzzyDict.items()]
    heapify( minHeap )
    mostCommon(minHeap) 
            
'''
Generates mutations from a sequence 'seq' with up to k differences.
'''
def genMutations(seq, k):
    sequences = []
    
    currentSeq = [c for c in seq]
    # generate indicies we need to change, UP TO k
    indices = {iTuple for i in range(k) \
               for iTuple in combinations( range(len(seq)), i+1)}
    for i in indices:
        sequences.extend(genMutHelper( list(i), [currentSeq]))
                
    return sequences

'''
return the mutations of a given sequence *differing in all the places indicated
by the tuple list.*
'''
def genMutHelper(indices, mutations):
    index = indices.pop()

    tempMutations = []
    
    # base case
    for seq in mutations:
        charToFlip = seq[index]
        leftovers = ["A", "C", "G", "T"]
        leftovers.remove(charToFlip)
        for c in leftovers:
            newSeq = list(seq)
            newSeq[index] = c
            tempMutations.append(newSeq)
            
    if(len(indices) == 0):
        for i in range(len(tempMutations)):
            tempMutations[i] = ''.join(tempMutations[i])
        return tempMutations
    else:
        return genMutHelper(indices, tempMutations)

with sane_open("dataset_8_5.txt") as f:
    freqFuzzyMatch(f.readline(), True)