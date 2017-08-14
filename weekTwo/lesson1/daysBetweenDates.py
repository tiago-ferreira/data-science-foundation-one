# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)

def isLeapYear(year):
    if(year % 4 != 0):
        return False
    elif(year % 100 != 0):
        return True
    elif(year % 400 != 0):
        return False
    else:
        return True
        


def dayInMonth(year,month):
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    elif(month == 2):
        if(isLeapYear(year)):
            return 29
        else:
            return 28
    else:
        return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < dayInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def date_is_before(year1, month1, day1, year2, month2, day2):
    if(year1 < year2):
        return True
    elif(year1 == year2):
        if(month1 < month2):
            return True
        elif(month1 == month2):
            if(day1 < day2):
                return True
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not date_is_before(year2, month2, day2, year1, month1, day1), "Houston we've got a problem"
    total_of_days = 0
    while date_is_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1,month1,day1)
        total_of_days += 1
    return total_of_days

def test():
    
    assert daysBetweenDates(2013,1,1,2013,1,1) == 0
    assert daysBetweenDates(2013,1,1,2013,1,2) == 1
    assert daysBetweenDates(2012,2,27,2012,3,1) == 3
    assert daysBetweenDates(2012,1,1,2013,1,1) == 366
    assert daysBetweenDates(2013,1,1,2014,1,1) == 365
    assert nextDay(2013,1,1) == (2013,1,2)
    assert nextDay(2013,4,30) == (2013,5,1)
    assert nextDay(2012,12,31) == (2013,1,1)
    assert nextDay(2012,2,28) == (2012,2,29)
    assert nextDay(2013,2,28) == (2013,3,1)
    assert isLeapYear(2000)
    assert not isLeapYear(1900)
    assert isLeapYear(2004)


    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()