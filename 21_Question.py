'''
TCS NQT Coding Question Day 1 Slot 2 – Question 1
Jack is always excited about sunday. It is favourite day, when he gets to play all day. And goes to cycling with his friends.
So every time when the months starts he counts the number of sundays he will get to enjoy. Considering the month can start with any day, 
be it Sunday, Monday…. Or so on.Count the number of Sunday jack will get within n number of days.

 Example 1:

Input 

mon-> input String denoting the start of the month.

13  -> input integer denoting the number of days from the start of the month.

Output :

2    -> number of days within 13 days.

Explanation:

The month start with mon(Monday). So the upcoming sunday will arrive in next 6 days. And then next Sunday in next 7 days and so on.
Now total number of days are 13. It means 6 days to first sunday and then remaining 7 days will end up in another sunday.
Total 2 sundays may fall within 13 days.
'''

day = input()
date = int(input())

dict = {
    'sun' : 8,
    'mon' : 7,
    'tue' : 6,
    'wed' : 5,
    'thus' : 4,
    'fri' : 3,
    'sat' : 2
}

sun_1 = dict[day]
print(sun_1)
cnt_sun = 0

for i in range(sun_1, date+2, 7):
    print("bcsudgbvfoir : ",i)
    if i == sun_1+1:
        continue
    cnt_sun +=1
print(cnt_sun)  
    