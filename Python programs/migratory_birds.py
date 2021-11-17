#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    n=len(arr)
    arr.sort()# 1 3 4 4 4 5
    '''count=1
    maxm=1
    res=arr[0]
    for i in range(1,n):# 1,2,3,4,5,6
        if arr[i]==arr[i+1]: # if 1==2
            count+=1
        else:
            count=1
        if count>maxm:
            maxm=count
            res=arr[i]
            return res'''
    count=[0]*6
    for i in arr:
        count[i]+=1
    return count.index(max(count))
            
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip()) #6

    arr = list(map(int, input().rstrip().split()))#1 4 4 4 5 3

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()