import math
import os
import random
import re
import sys

#Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

#timeConversion has the following parameter(s):

#string s: a time in  hour format

def timeConversion(s):
    normal_time = s[8:10]
    dylans_hours = s[0:2]
    mcdonald_time = int(dylans_hours)
    new_time =  mcdonald_time + 12
    winning_time = str(new_time)
    
    Other_time = s[2:8]
    
    
    all_time = winning_time + Other_time
    
    morning_time = s[0:8]
    
    
    
    
    if s[8:10] == "AM":
        return morning_time
        
            
    elif s[8:10] == "PM":
        return all_time
         
        
         
    
         
         # I want to take the first number
         # add 12 
         # return a new string
        
        
    else:
        return "something is timley right"
