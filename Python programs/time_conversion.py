#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    x=s.split(":")#07,05,45PM
    x[0]=int(x[0])%12
    if "PM" in x[-1] and [0]:
        x[0]+=12
    x[0]='%02d'%x[0]
    return ":".join(x)[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
