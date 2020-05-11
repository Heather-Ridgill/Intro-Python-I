"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

print(calendar.weekheader(3))
print()



# calendar.setfirstweekday(calendar.Sunday)

print(calendar.firstweekday())
print()

print(calendar.month(2020,5))

print(calendar.monthcalendar(2020, 5))

print(calendar.calendar(2020))

#0-Mon 1-Tues 2-Weds 3-Thurs 4-Fri 5-Sat 6-Sun
day_of_the_week = calendar.weekday(2020, 5, 11)
print(day_of_the_week)

# So you can see if a year is a leap year
is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_Days = calendar.leapdays(2000,2021)
print(how_many_leap_Days)

# You have to make sure that the user doesnt enter a number higher than the number of months in a year (12, duh!)

inputs = sys.argv

def check_month_input(monthNum):
    try:
        monthNum = int(monthNum)
    except:
        print("Invalid string type for year input: please enter a number between 1-12")
        return
    else:
        if monthNum < 0:
            print('Invalid year input: please enter a number between 1-12')
            return
        else:
            return monthNum
    
  # Year format

def check_year_input(yearNum):
    try:
        yearNum = int(yearNum)
    except:
        print("Invalid string type for year input - please only use numbers for year in format YYYY.")
        return
    else:
        if yearNum < 0:
            print('Invalid year input - please dont use negative numbers for years.')
            return
        else:
            return yearNum

  
if len(inputs) == 1:
    month = datetime.today().month	    
    year = datetime.today().year	   
    print(calendar.month(year, month))	    
elif len(inputs) == 2:	
    month = check_month_input(inputs[1])	    
    year = datetime.today().year	    
    if type(month) == int:	    
        print(calendar.month(year, month))	        
elif len(inputs) == 3:
    month = check_month_input(inputs[1])
    year = check_year_input(inputs[2])
    if type(year) == int and type(month) == int:
        print(calendar.month(year, month)) 