# Given a number n, write a function to print all prime factors of
# n. For example, if the input number is 12, then output should be
# “2 2 3”.
"""A prime factor is a natural number, other than 1, whose only factors are 1 and itself. 
The first few prime numbers are actually 2, 3, 5, 7, 11, and so on.
"""

n = int(input('Enter a number'))
t = list()
i = 2
while i > 0 and n > 1:
    if n % i == 0:
        t.append(i)
        n = n / i
    else:
        i = i+1
print(t)
