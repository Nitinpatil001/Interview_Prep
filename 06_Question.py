'''
Question:6
(Asked in Accenture OnCampus 11 Aug 2022, Slot 3)
You are required to implement the following Function 
def LargeSmallSum(arr)
The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and
second smallest from the odd position of given ‘arr’
Assumption:

All array elements are unique
Treat the 0th position as even
NOTE

Return 0 if array is empty
Return 0, if array length is 3 or less than 3
Example

Input
arr:3 2 1 7 5 4
Output
7

Explanation
Second largest among even position elements(1 3 5) is 3
Second smallest among odd position element is 4
Thus output is 3+4 = 7
Sample Input

arr:1 8 0 2 3 5 6
Sample Output
8
'''
def LargeSmallSum(arr):
    if arr is None and len(arr)>=3:
        return 0
    
    odd=[]
    even=[]
    
    for i in range(0,length+1,2):
        odd.append(arr[i])
    
    for i in range(1,length+1,2):
        even.append(arr[i])
    
    odd=sorted(odd)[-2]
    even=sorted(even)[-2]
    
    ans=odd+even
    
    print(ans)
        
   
length=int(input()) 
arr=list(map(int,input().split()))
LargeSmallSum(arr)


    
