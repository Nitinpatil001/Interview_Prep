'''
Question:9
(Asked in Accenture Offcampus 1 Aug 2021, Slot 1)

Implement the following functions.a

char*MoveHyphen(char str[],int n);

The function accepts a string “str” of length ‘n’, that contains alphabets and hyphens (-). Implement the function to move all hyphens(-) in the string to the front 
of the given string.

NOTE:- Return null if str is null.

Example :-

Input:
str:Move-Hyphens-to-Front
Output:
—MoveHyphenstoFront
Explanation:-

The string “Move-Hyphens -to-front” has 3 hyphens (-), which are moved to the front of the string, this output is “— MoveHyphen”

Sample Input

Str: String-Compare
Sample Output-

-StringCompare
'''

str1=input()

if str1 is None:
    print("Null")
    
demo=''
str2=''

for i in str1:
    if i == '-':
        demo+=i
    else:
        str2+=i
print(demo+str2)