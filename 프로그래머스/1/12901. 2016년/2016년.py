import datetime

def solution(a, b):
    date = datetime.date(2016, a, b)
    요일 = date.weekday()
    

    weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    return weekdays[(요일 + 1) % 7]
    
    
    
    
    
    
    return answer