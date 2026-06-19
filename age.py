# Store date of birth as tuple (day, month, year)
birthday = (19, 10, 1995)
day, month, year = birthday

# Current date: June 15, 2026
current_date = (15, 6, 2026)
cur_day, cur_month, cur_year = current_date

# Calculate days old (simple approximation)
def days_between(d1, d2):
    """Calculate days between two dates (day, month, year)"""
    # Days in each month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 ==    0)
    
    def total_days(d, m, y):
        total = 0
        # Days from years
           
        for yr in range(0, y):
            total += 366 if is_leap(yr) else 365
        # Days from months
        for mr in range(0, m - 1):
            total += days_in_month[mr]
            if mr == 1 and is_leap(y):
                total += 1
        # Days from days
        total += d - 1
        return total
    
    return total_days(d2[0], d2[1], d2[2]) - total_days(d1[0], d1[1], d1[2])

days_old = days_between(birthday, current_date)

# Zeller's formula for day of week (no imports)
def zeller_day(day, month, year):
    """Zeller's formula: returns 0=Saturday, 1=Sunday, ..., 6=Friday"""
    if month < 3:
        month += 12
        year -= 1
    
    q = day
    m = month
    k = year % 100
    j = year // 100
    
    h = (q + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    # Convert: 0=Sat, 1=Sun, 2=Mon, ..., 6=Fri
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]

born_day = zeller_day(day, month, year)

# Days until next birthday
def days_until_next_birthday(bday, current):
    """Calculate days until next birthday"""
    bd_day, bd_month, bd_year = bday
    curr_day, curr_month, curr_year = current
    
    # Next birthday year
    next_bday_year = curr_year
    if (curr_month > bd_month) or (curr_month == bd_month and curr_day >= bd_day):
        next_bday_year += 1
    
    # Days from current date to end of year + days from start of year to birthday
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    
    def days_from_start(d, m, y):
        total = d - 1
        for mr in range(0, m - 1):
            total += days_in_month[mr]
            if mr == 1 and is_leap(y):
                total += 1
        return total
    
    def days_in_year(y):
        return 366 if is_leap(y) else 365
    
    days_remaining = days_in_year(curr_year) - days_from_start(curr_day, curr_month, curr_year)
    days_to_bday = days_from_start(bd_day, bd_month, next_bday_year)
    
    return days_remaining + days_to_bday

days_until_birthday = days_until_next_birthday(birthday, current_date)

print("=== Exercise 2: Birthday Countdown Machine ===")
print(f"Date of Birth: {day}/{month}/{year}")
print(f"Days old: {days_old}")
print(f"Born on: {born_day}")
print(f"Days until next birthday: {days_until_birthday}")
print()