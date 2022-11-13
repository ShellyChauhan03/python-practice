"""Given a string, write a python function to check if it is
palindrome or not. A string is said to be palindrome if the reverse
of the string is the same as string. For example, “malayalam” is a
palindrome, but “music” is not a palindrome.
"""

while True:
    astr = input('Enter a string')
    if astr=='done' or astr=='Done':
        break
    t = tuple(astr)
    #print(t,t[0],t[-0])
    #print(t[-1],t[-2])
    counter=0
    for i in range(0,len(t)):
        #print('inside loop ',astr[i] , astr[-i])
        if astr[i] != astr[-i-1]:
            counter = counter+1
            break
    if(counter==0):
        print('String is a Palindrome string.')
    else:
        print('String is not a Palindrome string.')
