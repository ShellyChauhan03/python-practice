"""Input a text file (containing 1 or more paragraphs of English
text) from the user, parse this file to display the frequency of
occurrence of each word in this text file. Find the 3 most frequent
words as well.
A Histogram problem.
"""
import time
import string
#import os
#import csv

#absolute_path = os.path.dirname(os.path.abspath('.'))
# C:\\Users\\snchauhan\\Documents\\Tech\\Sem-1\\Python
# Absolute path is not working on my system as of now
try:
    print('Start Time',time.time())
    f = open("SumOfDigits.py")
    contents = f.read()
    lines = contents.split("\n")
    d = dict()
    for line in lines:
        print('Line: ',line)
        #below line remove the punctuation from the string
        line.translate(line.maketrans('','',string.punctuation))
        #print('Formatted Line: ',line)
        words = line.split(' ')
        if len(words)>0:
            for word in words:
                if word in d:
                    d[word] = d[word]+1
                else:
                    d[word] = 1
    
    l = list()
    
    for key,value in d.items():
        l.append((value,key))
    
    l = sorted(l, reverse=True)
    print(l)
    for i in range(0,4):
        a,b = l[i]
        print(b)
    
    f.close()
    print('End Time:',time.time())
except Exception as e:
    print(e)
