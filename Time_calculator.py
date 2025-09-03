def add_time(start, duration, starting_day=None):
    # SPILT THE TIME
    start_time = start.split(':')
    start_hour = int(start_time[0])
    start_minute = int(start_time[1][:2])
    start_meridiem = start_time[1][3:]

    duration_time = duration.split(':')
    duration_hour = int(duration_time[0])
    duration_minute = int(duration_time[1])

    # CONVERT TO 24HR CLOCK
    if start_meridiem == 'PM' and start_hour != 12:
        start_hour += 12
    elif start_meridiem == 'AM' and start_hour == 12:
        start_hour = 0

    # ADD TIME
    total_hours = start_hour + duration_hour
    total_minutes = start_minute + duration_minute

    # SORT THE MINUTES
    if total_minutes >= 60:
        total_hours += 1
        total_minutes %= 60

    # CALCULATE DAYS LATER
    days_later = total_hours // 24
    hours_later = total_hours % 24

    # CONVERT BACK TO 12HR FORMAT
    if hours_later == 0:
        hours_later = 12
        meridiem = 'AM'
    elif hours_later < 12:
        meridiem = 'AM'
    elif hours_later == 12:
        meridiem = 'PM'
    else:
        hours_later -= 12
        meridiem = 'PM'

    # SORT OUT OPTIONAL DAYS OF WEEK
    if starting_day:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        starting_index = days.index(starting_day.capitalize())
        new_day_index = (starting_index + days_later) % 7
        new_day = days[new_day_index]
    else:
        starting_day = None

    # PRINT FORMATTED TIME
    new_time = f'{hours_later}:{total_minutes:02d} {meridiem}'
    if starting_day:
        new_time += f', {new_day}'
    if days_later == 1:
        new_time += f' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'

    return new_time


print(add_time('2:59 AM', '24:00', 'tuesday'))