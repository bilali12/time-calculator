days_of_the_week = {
    '1': 'Monday',
    '2': 'Tuesday',
    '3': 'Wednesday',
    '4': 'Thursday',
    '5': 'Friday',
    '6': 'Saturday',
    '7': 'Sunday'
}

def split_time(time):
    """
        this function split time without the : sign and return a list
    """
    return time.split(':')

def add_hours(h1, h2):
    """
        this function add two hours and return the result
    """
    return int(h1) + int(h2)

def add_minutes(m1, m2):
    """
        this function add two minutes and return the result
    """
    return int(m1) + int(m2)

def format_hour(hour):
    """
        this function return a tuple of the modulo by 12 and interger divison by 12 
    """
    return (hour % 12, int(hour / 12))

def format_minute(minute):
    """
        this function return a tuple of the modulo by 60 and interger divison by 60
    """
    return (minute % 60, int(minute / 60))


def add_time(start_time, duration_time, days=None):
    """
        this function return a string of times after some calculation and test
    """
    start_time = start_time.split()
    start_time_hours_minute = split_time(start_time[0])
    duration_time = split_time(duration_time)
    if int(start_time_hours_minute[1]) > 59 or int(duration_time[1]) > 59:
        return "Error: minutes shouldn't greater than 59"

    minute = add_minutes(start_time_hours_minute[1], duration_time[1])
    minute = format_minute(minute)
    hour = add_hours(start_time_hours_minute[0], duration_time[0]) + minute[1]
    hour = format_hour(hour)
    day = 1
    if hour[1] % 2 == 0:
        state = start_time[1]
    else:
        if start_time[1].upper() == 'AM':
            state = 'PM'
            day = 0
        if start_time[1].upper() == 'PM':
            state = 'AM'
                
    if day != 0:
        day = int(hour[1] / 2) + (hour[1]  % 2)
    

    if days is None:
        if day == 0:
            if hour[0] == 0:
                if minute[0] < 10:
                    return f"12:0{minute[0]} {state}"
                else:
                    return f"12:{minute[0]} {state}"
            else:
                if minute[0] < 10:
                    return f"{hour[0]}:0{minute[0]} {state}"
                else:
                    return f"{hour[0]}:{minute[0]} {state}"
        else:
            if day == 1:
                if hour[0] == 0:
                    if minute[0] < 10:
                        return f"12:0{minute[0]} {state} (next day)"
                    else:
                        return f"12:{minute[0]} {state} (next day)"
                else:
                    if minute[0] < 10:
                        return f"{hour[0]}:0{minute[0]} {state} (next day)"
                    else:
                        return f"{hour[0]}:{minute[0]} {state} (next day)"
            else:
                if hour[0] == 0:
                    if minute[0] < 10:
                        return f"12:0{minute[0]} {state} ({day} days later)"
                    else:
                        return f"12{minute[0]} {state} ({day} days later)"
                else:
                    if minute[0] < 10:
                        return f"{hour[0]}:0{minute[0]} {state} ({day} days later)"
                    else:
                        return f"{hour[0]}:{minute[0]} {state} ({day} days later)"
    else:
        if day == 0:
            if hour[0] == 0:
                if minute[0] < 10:
                    return f"12:0{minute[0]} {state}, {days}"
                else:
                    return f"12:{minute[0]} {state}, {days}"
            else:
                if minute[0] < 10:
                    return f"{hour[0]}:0{minute[0]} {state}, {days}"
                else:
                    return f"{hour[0]}:{minute[0]} {state}, {days}"
        else:
            for key, value in days_of_the_week.items():
                if value.upper() ==  days.upper():
                    if key == '7':
                        key = int(key) - 7 + day
                    else:
                        key = int(key) + day
                    break
                   
            key = str(key)
                    
            if day == 1:
                if hour[0] == 0:
                    if minute[0] < 10:
                        return f"12:0{minute[0]} {state}, {days_of_the_week[key]} (next day)"
                    else:
                        return f"12:{minute[0]} {state}, {days_of_the_week[key]} (next day)"
                else:
                    if minute[0] < 10:
    
                        return f"{hour[0]}:0{minute[0]} {state}, {days_of_the_week[key]} (next day)"
                    else:
                        return f"{hour[0]}:{minute[0]} {state}, {days_of_the_week[key]} (next day)"
            else:
                if hour[0] == 0:
                    # print(key)
                    if minute[0] < 10:
                        return f"12:0{minute[0]} {state}, {days_of_the_week[key]} ({day} days later)"
                    else:
                        return f"12{minute[0]} {state}, {days_of_the_week[key]} ({day} days later)"
                else:
                    if minute[0] < 10:
                        return f"{hour[0]}:0{minute[0]} {state}, {days_of_the_week[key]} ({day} days later)"
                    else:
                        return f"{hour[0]}:{minute[0]} {state}, {days_of_the_week[key]} ({day} days later)"

