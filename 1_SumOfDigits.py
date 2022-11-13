#Given a number, find the sum of its digits. Take the number as
#an input from the user.
n = int(input('Enter a number'))
print('n: ',n)
sumofdigit = 0
while True:
    if(n<=0):
        break
    else:
        unit_place = n % 10
        #print(n)
        n = (int)(n / 10)
        print('unit_place: ', unit_place)
        sumofdigit += unit_place
print('Sum :', sumofdigit)
