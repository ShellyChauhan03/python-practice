"""Given a number, check whether the given number is an
Armstrong number or not. A positive integer is called an
Armstrong number of order n if:
abcd... = an
 + bn + cn
 + dn
 + ...
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
153 is an Armstrong number of order 3.
Inputs from the user will be number and order n.
"""

original = n = int(input('Enter a number: '))
o = int(input('Enter an order: '))
value = 0 
while n>0:
    unit = n%10
    n = (int)(n/10)
    x = unit**o
    value += x
print(value)
if value == original:
    print('Armstrong number!')
else:
    print('Not an armstrong number')
