'''
Accenture slot : jul 28 2024

Prime Number Picnic
input 1 : An integer value n

output specification :
return an integer value representing the sum of all the prime numbers till N in case the number of items is 0 or 1
return 0

Example 1 :
input 1 : 10
output 1 : 17

explanation:
here n =10 the prime numbers between 2 and 10 are 2,3,5,7 and their sum is 17 is returned as the output.
'''

N = int(input("Enter a Number : "))
l = []
for i in range(2,N+1):
    if(N%i)==0:
        l.append(i)
print(sum(l))
    