daysOfWeek = { 
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6,
     }
daysOfWeekInverse = {v:k for (k,v) in daysOfWeek.items()}

def solution(s, k):
    endDay = (daysOfWeek[s] + k) % len(daysOfWeek)
    return daysOfWeekInverse[endDay]


if __name__ == '__main__':
    startDay = "Sat"
    increment = 23
    endDay = solution(startDay, increment)

    print(endDay)
