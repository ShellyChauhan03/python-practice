#Given two numbers n and r, find the value of nCr (binomial
#coefficient: nCr = (n!) / (r! * (n-r)!))

n = int(input('n: '))
r = int(input('r: '))

def factorial(p):
    i = 1
    for iterator in range(1,p+1):
        i = i*iterator
    return i


print(n,'Coefficient',r,' is ',(int)((factorial(n)/(factorial(r)*(factorial(n-r))))))
