import calendar
from typeguard import typechecked

all_months ={ **{f"{i:02}": i for i in range(1, 13)}, 
              **{name: i for i,name in enumerate(calendar.month_name) if name},
              **{name: i for i, name in enumerate(calendar.month_abbr) if name}
            }

all_weekdays ={ **{name: i for i, name in enumerate(calendar.day_name, start=1)}, 
                **{calendar.day_abbr[i]: i+1 for i in range(7)}
              }

@typechecked
def isleap(year:int)->bool:  
    """
    Returns whether the year is leap or not

    Parameters
    year:  integer
        possible values include all whole numbers

    Return values
    isLeap: boolean
        possible values include True or False

    Example code
    >>> isleap(2024)
    True
    >>> isleap(0)
    ValueError:"Invalid year value: 0"
    """
    if year<1:
        raise ValueError(f"Invalid year value: {year}")
    elif year%4:
        if year%400==0: return True
        elif year%100==0: return False
        else: return True
    else: return False

@typechecked
def days_in_month(year: int, month: int|str)->int: 
    """
    Returns the number of days in a month

    Parameters
    year: integer
    month: integer or string
            possible values include from 1 to 12,  "January", "February", ..."December", "Jan", "Feb", ..."Dec" 
    
    Return values
    days: integer
        possible values include 28,29,30,31

    Example code
    >>> days_in_month(2025, "April")
    30
    >>> days_in_month(2000, 02)
    29
    """
    if isinstance(month, str):
        if month not in all_months:
            raise ValueError(f"Invalid month name: {month}")
        month=all_months[month]
    if month<1 or month>12:
        raise ValueError(f"Invalid month Value: {month}")
    
    if month==2 : 
        days= 29 if isleap(year) else 28
    elif month in {4, 6, 9, 11}: days= 30
    else: days= 31
    return days

@typechecked
def count_weekday_in_month(year:int, month: int|str, weekday: int|str)->int:
    """
    Returns the number of times a specific weekday occurs in a month in O(1) time complexity

    Parameters
    year:  integer
    month: integer or string
           possible values include from 1 to 12,  "January", "February", ..."December", "Jan", "Feb", ..."Dec" 
    weekday: integer or string
           possible values include from 1 to 7, "Mon", "Tue", ..., "Sun", "Monday", "Tuesday", ..., "Sunday" 
    
    Return values
    weekdaycount: integer
        possible values include 4 or 5

    Example code
    >>> count_weekday_in_month(2025,12,"Sun")
    4
    >>> count_weekday_in_month(2000,02,"Mon")
    4
    """

    if isinstance(month, str):
        if month.title() not in all_months:
            raise ValueError(f"Invalid month name: {month}")
        month=all_months[month.title()]
    if month<1 or month>12:
        raise ValueError(f"Invalid month Value: {month}")

    if isinstance(weekday,str):
        if weekday.title() not in all_weekdays:
            raise ValueError(f"Invalid weekday name: {weekday}")
        weekday=all_weekdays[weekday.title()]
    if weekday>7 or weekday<1:
        raise ValueError(f"Invalid weeday value: {weekday}")
        
    
    if days_in_month(year,month)%7>=weekday:
        weekdaycount= days_in_month(year,month)//7+1
    else: 
        weekdaycount= days_in_month(year,month)//7
    
    return weekdaycount
