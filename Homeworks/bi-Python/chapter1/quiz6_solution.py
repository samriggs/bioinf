'''
Created on Nov 13, 2013

@author: samriggs

CODE CHALLENGE: Solve the Minimum Skew Problem.
https://beta.stepic.org/Bioinformatics-Algorithms-2/Peculiar-Statistics-of-the-Forward-and-Reverse-Half-Strands-7/#step-6
'''

from bi_utils.helpers import sane_open
from cStringIO import StringIO

def min_skew(dataset=''):
    if (not dataset):
        dataset = "stepic_dataset.txt"
    
    # O(n)
    with sane_open(dataset) as f:
        skew = 0
        skew_list = []
        for c in f.readline():
            # calculate skew for each char
            skew_list.append(skew)
            if (c == "C"):
                skew -= 1
            elif (c == "G"):
                skew += 1
            
        # get min value, O(n)
        min_skew = min(skew_list)
        
        # O(n)
        position = 0
        file_str = StringIO()
        for num in skew_list:
            if (num == min_skew):
                file_str.write( str(position) )
                file_str.write(" ")
            position += 1
        
        print file_str.getvalue().strip()

if (__name__ == "__main__"):   
    min_skew()