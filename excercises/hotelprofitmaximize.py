'''
There are n persons who want same room in a hotel. Each person wants to stay in the hotel for his own convenient time
but only one person can stay at a time.
Assume that room is available from 5AM to 11PM. Hotel manager takes 500 rupees from each person who is staying in that
 room.
It does not matter how long a person stays in that room.
You have to maximize the profit of the manager. Let us say that n =4 i.e. four persons want same room.
 Let us say that 1st person wants the room from 6AM to 8AM and 2nd person wants room from 7AM to 8AM,
 3rd person wants room from 8AM to 12PM and 4th person wants room from 11AM to 1PM.

By observing above figure, you can easily see that manager can only allow maximum of two persons to stay
(1st and 3rd or 1st and 4th or 2nd and 3rd or 2nd and 4th). So maximum profit he can get is 500+500 = 1000 rupees.
So you have to implement an algorithm which can find maximum profit value. Assume that the persons want the room
only b/w 5AM to 11PM and each person wants room in multiple of hours.


Input Format
Input should be an array of strings describing
 {< 1st job starting time >#< 1st job ending time >,< 2nd job starting time >#
 < 2nd job ending time >,...,< nth job starting time >#< nth job ending time >}

For the example considered in the question, input is
{6AM#8AM,11AM#1PM,7AM#3PM,7AM#10AM,10AM#12PM,2PM#4PM,1PM#4PM,8AM#9AM}.


Constraints
1 <= |S| <= 10^4

Output Format
Output should be maximum profit value(Integer).

Sample TestCase 1
Input
8
6AM#8AM
11AM#1PM
7AM#3PM
7AM#10AM
10AM#12PM
2PM#4PM
1PM#4PM
8AM#9AM
Output
2000

'''


from datetime import datetime


def getTime(time):
    return datetime.strptime(time, '%I%p')


def duration(timings):
    startTime = getTime(timings[0])
    endTime = getTime(timings[1])
    duration = endTime - startTime
    return duration


def main():
    bookedRequests = []
    timingsList = [
        ('6AM', '8AM'), ('11AM', '1PM'), ('7AM', '3PM'), ('7AM', '10AM'), ('10AM', '12PM'), ('2PM', '4PM'),
        ('1PM', '4PM'), ('8AM', '9AM'), ('5AM', '6AM'), ('5AM', '6AM')
    ]
    timingsList = sorted(timingsList, key=duration)
    print(timingsList)

    for timings in timingsList:
        eligible = True
        if bookedRequests:
            for tb in bookedRequests:
                if getTime(timings[0]) >= getTime(tb[0]) or getTime(timings[1]) > getTime(tb[0]):
                    if getTime(timings[0]) < getTime(tb[1]) or getTime(timings[1]) <= getTime(tb[1]):
                        eligible = False
                        break
            if eligible:
                bookedRequests.append(timings)

        if not bookedRequests:
            bookedRequests.append(timings)

    print(len(bookedRequests) * 500)


main()
