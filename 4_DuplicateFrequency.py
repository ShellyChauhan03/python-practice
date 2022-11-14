#Given an array which may contain duplicates, print all elements
#and their frequencies.

n = [1,2,3,4,5,2,3,'A','B','A','A']
freq = dict()
for x in n:
    if x in freq:
        freq[x] = freq[x]+1
    else:
        freq[x] = 1
print(freq)
