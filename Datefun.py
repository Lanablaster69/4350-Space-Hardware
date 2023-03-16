import datetime
'''
function   doy   calculates day of year for a given date using the gregorian calander
Returns: The day of the year as an int'''
       
def doy(YR, MO, D): # arguments: YR=year , MO=month , D = day [all ints] 
    start = datetime.date(YR, 1, 1) #sets the start date as january 1st of the same year as the date specified
    date = datetime.date(YR, MO, D) #creates object date in datetime module from arguments YR, MO, D
    delta = date - start
    #print(f"delta=",{delta})
    return delta.days + 1 #returns number of days in delta (add one to account for Jan 1st)
# Test doy function
year = 2023
month = 3
day = 5
dayofyear = doy(year, month, day)
print(f"doy:  The day of the year for {day}/{month}/{year} is {dayofyear}")

#################################################################################

# function   frcofd   calculates the fraction of a day at the specified input time and returns fraction of day as a float
def frcofd(HR, MI, SE): #hour, minute, second [int,int,float]
    secondsum = HR * 3600 + MI * 60 + SE #computes total seconds in the day
    return secondsum / 86400 #divides total seconds in the day by total seconds per full day to return fraction of a day

# Test frcofd function
hour = 12
minute = 3
second = 14.12345678901234
day_fraction = frcofd(hour, minute, second)
print(f"frcofd:  The fraction of a day for {hour}:{minute}:{second} is {day_fraction}")  


#################################################################################

# function  ep2date  converts an Epoch (date format in TLE) to text string CDATE - UTC

def ep2dat(TLE_Epoch):
    year = int(TLE_Epoch[:2]) #takes first 2 chars of TLE_Epoch as year
    day_of_year = int(TLE_Epoch[2:5]) #char 3-5 as day of year
    fod = float(TLE_Epoch[5:]) #char 5+ as fraction of day
    hour, remainder = divmod(fod * 24, 1) #multiplies fod by 24 and calculates the quotient and remainder when divided by 1. quotient=hour, remainder= duh...
    minute, remainder = divmod(remainder * 60, 1) #similar to above, calculates the minute and updates remainder
    second = remainder * 60 #duh
    epoch = datetime.datetime(2000 + year - (year > 50) * 100, 1, 1) #creates a datetime object representing January 1
    epoch_datetime = epoch + datetime.timedelta(days=day_of_year - 1, hours=hour, minutes=minute, seconds=second) #specific date and time from TLE_Epoch
    CDATE = epoch_datetime + datetime.timedelta(hours=12) #makes cdate = a timedelta object of 12 hrs
    month = CDATE.strftime("%b") #makes month the first 3 letters of the month as opposed to just a numberrrrrr
    return f"{CDATE.year}-{month}-{CDATE.day} {CDATE.hour}:{CDATE.minute}:{CDATE.second}"

# Test ep2dat function
TLE_Epoch = '23064.61816216'
date_string = ep2dat(TLE_Epoch)
print(f"ep2dat:  The date string for TLE date {TLE_Epoch} is {date_string}")


#################################################################################
"""
function  curday  reads the system clock and returns the current UTC date and time
returns the formatted CURRENT date and time in UTC in CDATE as
1997-02-24 19:11:00.00 """

def curday():
   
    now_utc = datetime.datetime.utcnow() #module.class.utcnow
    return now_utc.strftime("%Y-%m-%d %H:%M:%S.%f") #formatting duh

# Test curday function
now_utc = curday()
print(f"curday: The current UTC date and time is {now_utc}")
