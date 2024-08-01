'''
Question:11
(Asked in Accenture Offcampus 1 Aug 2021, Slot 3)

Problem Statement
You are given a function,
Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);
The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments .
Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and 
all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.
Assumption: String Contains only lower-case alphabetical letters.

Note:
Return null if string is null.
If both characters are not present in string or both of them are same , then return the string unchanged.
Example:
Input:
Str: apples
ch1:a
ch2:p
Output:
paales
Explanation:

‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, thus output is paales.
'''

def replacechar(str1, ch1, ch2):
    if str1 is None:
        return None
    if ch1 not in str1 or ch2 not in str1 or ch1==ch2:
        return "The String Unchanged!"
    
    str2=''
    for i in str1:
        if i == ch1:
            str2+=ch2
        elif i == ch2:
            str2+=ch1
        else:
            str2+=i
    return str2

str1=input()
ch1=input()
ch2=input()
print(replacechar(str1,ch1,ch2))