'''
Question 2
Problem Description -:  Given two non-negative integers n1 and n2, where n1

For example:
Suppose n1=11 and n2=15.
There is the number 11, which has repeated digits, but 12, 13, 14 and 15 have no repeated digits. So, the output is 4.

Example1:
Input:
11 — Vlaue of n1
15 — value of n2
Output:
4

Example 2:
Input:
101 — value of n1
200 — value of n2
Output:
72
'''

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))

cnt = 0

for i in range(n1,n2+1):
    if len(str(i))==len(set(str(i))):
        cnt+=1
print(cnt)