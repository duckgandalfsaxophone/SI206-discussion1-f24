def time(hours, minutes):
    total_minutes = hours * 60 + minutes
    return f"It took us {total_minutes} minutes to get home"

def change(s):
    if len(s) <= 4:
        return "String must be longer than 4 characters."
    first_two = s[:2].upper()
    last_two = s[-2:].lower()
    middle = s[2:-2]
    new_middle = middle.capitalize()
    return new_middle + first_two + last_two

def merge_strs(a, b):
    if len(a) < len(b):
        short, long = a, b
    else:
        short, long = b, a
    return short + long + short

def alarm_clock(day, vacation):
    is_weekend = day == 0 or day == 6
    if vacation:
        if is_weekend:
            return "off"
        else:
            return "10:00"
    else:
        if is_weekend:
            return "10:00"
        else:
            return "7:00"

# Outputs
print(time(3, 13))
print(change('hello'))
print(change('pumpkin'))
print(merge_strs('Hi', 'there'))
print(merge_strs('ab', 'c'))
print(alarm_clock(1, False))
print(alarm_clock(0, True)) 