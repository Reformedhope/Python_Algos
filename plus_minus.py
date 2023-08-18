import math
import os
import random
import re
import sys


        
        
    
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#



def plusMinus(arr):
    
    postive_number = 0
    negative_number = 0
    zero_number = 0

    for num in arr:
        if  num > 0:
            postive_number += 1
        elif num < 0:
            negative_number+= 1
        else: 
            zero_number += 1
        
    total_elements = len(arr)
    postive_fact = postive_number/total_elements
    negative_fraction = negative_number/total_elements
    zero_fraction = zero_number/total_elements
    
    
    print("{:.6f}".format(postive_fact))
    print("{:.6f}".format(negative_fraction))
    print("{:.6f}".format(zero_fraction))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
