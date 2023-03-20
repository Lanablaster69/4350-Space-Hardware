import datetime
import platform
import sys
#import os
import urllib
import winsound
import msvcrt  # only works on windows Microsoft! Visual C/C++ Runtime Library
#####################
import numpy as np
from collections import namedtuple
#from Fileio import BANNER, ERRMSG, Station, Satellite, anykey, STKout
#from Datefun import doy, frcofd, ep2dat, curday

from OMPython import ModelicaSystem

mod=ModelicaSystem("D:/school 22-23/4350 Space Hardware/P-setion","Sattrak.Sattest", ["Modelica.Constants"])
######## Datefun ###################################################
######## Datefun ###################################################
######## Datefun ###################################################

######################################### doy #############################
'''
function   doy   calculates day of year for a given date using the gregorian calander
Returns: The day of the year as an int'''
       
def doy(YR, MO, D): # arguments: YR=year , MO=month , D = day [all ints] 
    start = datetime.date(YR, 1, 1) #sets the start date as january 1st of the same year as the date specified
    date = datetime.date(YR, MO, D) #creates object date in datetime module from arguments YR, MO, D
    delta = date - start
    #print(f"delta=",{delta})
    return delta.days + 1 #returns number of days in delta (add one to account for Jan 1st)

#################################### frcofd #############################################

# function   frcofd   calculates the fraction of a day at the specified input time and returns fraction of day as a float
def frcofd(HR, MI, SE): #hour, minute, second [int,int,float]
    secondsum = HR * 3600 + MI * 60 + SE #computes total seconds in the day
    return secondsum / 86400 #divides total seconds in the day by total seconds per full day to return fraction of a day
############################## ep2date ###################################################

# function  ep2date  converts an Epoch (date format in TLE) to text string CDATE - UTC
'''
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

dt = ep2dat('23064.61816216')
print(dt)
print(".epdatsec:", dt.second)'''
def ep2dat(TLE_Epoch):
    year = int(TLE_Epoch[:2])
    day_of_year = int(TLE_Epoch[2:5])
    fod = float(TLE_Epoch[5:])
    hour, remainder = divmod(fod * 24, 1)
    minute, remainder = divmod(remainder * 60, 1)
    second = remainder * 60
    epoch = datetime.datetime(2000 + year - (year > 50) * 100, 1, 1)
    epoch_datetime = epoch + datetime.timedelta(days=day_of_year - 1, hours=hour, minutes=minute, seconds=second)
    CDATE = epoch_datetime + datetime.timedelta(hours=12)
    return CDATE
'''
dt = ep2dat('23064.61816216')
print(dt)
print(".dayofyear:", dt.strftime('%j'))
print(".hour:", dt.hour)'''

######################## curday #################################################
"""
function  curday  reads the system clock and returns the current UTC date and time
returns the formatted CURRENT date and time in UTC in CDATE as
1997-02-24 19:11:00.00 """

def curday():
   
    now_utc = datetime.datetime.utcnow() #module.class.utcnow
    return now_utc.strftime("%Y-%m-%d %H:%M:%S.%f") #formatting duh
'''
_________________________¶¶¶______________________
_____________________¶¶¶¶¶¶¶¶¶¶¶¶_________________
___________________¶¶¶_________¶¶¶________________
__________________¶¶_____________¶¶_______________
_________________¶¶________________¶______________
________________¶¶_________________¶¶_____________
________________¶__________________¶¶_____________
_______________¶¶___________________¶_____________
_______________¶¶___________________¶¶____________
_______________¶_¶¶_________________¶¶____________
_______________¶_¶¶_________________¶¶____________
_______________¶¶¶__________________¶_____________
___¶___________¶¶¶__________________¶_____________
___¶¶__________¶¶¶___¶¶¶¶____¶¶¶____¶___________¶¶
___¶¶__________¶¶¶__¶¶__¶¶__¶¶¶¶¶___¶¶__________¶¶
___¶¶¶_________¶¶¶_¶¶____¶__¶___¶¶_¶¶¶__________¶_
____¶¶_________¶¶¶_¶___¶¶¶__¶¶___¶_¶¶__________¶¶_
____¶¶¶_________¶__¶¶¶¶¶__¶__¶¶¶¶¶_¶__________¶¶¶_
____¶¶¶¶_______¶____¶¶¶__¶¶____¶¶¶_¶¶¶________¶¶¶_
_____¶_¶______¶¶¶_______¶¶¶¶________¶¶_______¶¶¶__
_____¶¶¶¶_______¶¶¶_____¶__¶_______¶¶_______¶¶¶¶__
______¶_¶¶________¶¶¶___¶__¶¶____¶¶¶________¶_¶___
_______¶_¶¶_____¶¶__¶___¶_¶¶¶___¶¶_________¶_¶____
_______¶¶_¶_____¶¶¶¶¶¶__¶¶¶¶¶__¶¶¶¶_______¶_¶¶____
________¶¶¶¶_____¶_¶¶¶__¶¶_¶___¶¶¶¶______¶¶_¶_____
_________¶_¶¶_____¶_¶¶¶_______¶¶¶¶______¶¶_¶______
__________¶_¶¶____¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶______¶_¶_______
___________¶_¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶_______
____________¶_¶¶____¶¶_________¶¶¶___¶¶_¶¶________
_____________¶_¶¶¶__¶¶¶¶¶¶_¶¶¶¶¶¶___¶¶_¶¶_________
______________¶¶_¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_¶¶__________
_______________¶¶_¶¶_¶_¶¶¶¶¶¶__¶_¶¶__¶¶___________
________________¶¶_¶¶_¶_______¶¶¶¶__¶_____________
_________________¶¶_¶¶¶¶¶¶¶¶¶¶¶¶__¶¶______________
________¶¶________¶¶_¶¶¶_¶¶¶¶¶___¶¶_______________
_______¶¶¶¶_________¶__¶¶__¶____¶¶________________
________¶¶¶¶_______¶_¶¶_¶¶¶¶¶¶¶¶__________¶¶______
_¶¶¶_____¶¶¶¶_¶¶¶¶¶¶¶_¶¶__¶¶¶¶¶_________¶¶¶¶¶_____
¶__¶¶¶¶¶__¶¶_¶¶¶¶____¶¶¶¶¶__¶¶¶¶¶______¶¶__¶______
¶__¶¶_¶¶¶¶¶¶¶_¶¶¶__¶¶¶¶__¶¶¶___¶¶¶¶¶__¶¶_¶¶_____¶¶
¶¶¶¶¶¶_____¶¶_¶¶¶¶¶¶¶______¶¶¶____¶¶¶¶¶¶¶¶_____¶¶¶
__¶__¶¶¶¶¶¶¶¶_¶______________¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_
_____________¶¶¶________________¶¶¶¶¶_¶¶______¶¶¶¶
_____________¶¶¶¶¶¶________________¶¶¶¶¶¶¶¶¶¶¶¶___
______________¶¶¶¶¶____________¶¶¶¶¶_¶____________
_______________________________¶¶__¶¶_____________

'''
############### Fileio ############################################################
############### Fileio ############################################################
############### Fileio ############################################################


################################# P1 ###################################
def BANNER():
    #Prints the ENG4350 team info, program name, date, version and welcome message.
    names = "Spencer Reznick 213602792, Celeste Collura 215470636"
    course = "ENG 4350"
    program = "Python"
    date = datetime.date.today().strftime("%Y-%m-%d")
    version = platform.python_version()
    print(f"{names}, {course}, {program}, {date}, {version}, OKAY LEZGO!")

# Call the BANNER function to test 
#BANNER()

###############################ERRMSG#################################

def ERRMSG(string):
    # "beeps" the terminal (plays a tune), displays an error message STRING and exits.
    if platform.system() == 'Windows':
        c = 261  # Hz
        e = 329  # Hz
        g = 391  # Hz

        winsound.Beep(c, 250)   # C
        winsound.Beep(e, 250)   # E
        winsound.Beep(g, 250)   # G
        winsound.Beep(c*2, 250) # C
        winsound.Beep(c, 999)   # C
    else: 
        print("\a") #should play a beep I think
    

    print(f"Error: {string}")
    sys.exit()                         #   I COMMENTED THIS OUT

#ERRMSG("test error")

################## STATION ##############################

from collections import namedtuple

class Station:
    def __init__(self, STNFIL):
        Station.name = 'ARO'
        Station.stnlat = 45.95550333333333
        Station.stnlong = 281.9269597222222
        Station.stnalt = 260.42
        Station.utc_offset = -4.0
        Station.az_el_nlim = 1
        Station.az_el_lim = namedtuple('AzElLim', ['az', 'elmin', 'elmax'])
        Station.az_el_lim_1 = Station.az_el_lim(0, 9.0, 89.0)
        Station.st_az_speed_max = 24.0
        Station.st_el_speed_max = 5.0

################## Satellite ###########################

import urllib.request
# Get latest GPS data from Celestrak web site, write it to a file
tlefile = open(r'D:\school 22-23\4350 Space Hardware\P-setion\gps-ops.txt', 'wt')
tleurl = 'https://celestrak.com/NORAD/elements/gps-ops.txt'
for line in urllib.request.urlopen(tleurl):
    tlefile.write('%s' % line.decode().rstrip('\n'))
tlefile.close()
# Open the file we just wrote and create a list of Satellite objects
tlefile = open(r'D:\school 22-23\4350 Space Hardware\P-setion\gps-ops.txt', 'rt')

class Satellite:
    def __init__(self, line0, line1, line2):
        self.name = line0.strip()
        self.refepoch = float(line1[18:32])
        self.incl = float(line2[8:16])
        self.raan = float(line2[17:25])
        self.eccn = float("0." + line2[26:33])
        self.argper = float(line2[34:42])
        self.meanan = float(line2[43:51])
        self.meanmo = float(line2[52:63])
        self.ndot2 = float(line1[33:43].replace(' ', '0'))
        self.nddot6 = float(line1[44:50].replace(' ', '0'))
        self.bstar = float(line1[51:59].replace(" ", ""))
        self.orbitnum = int(line2[64:68])
#Constellation = []
    
i = 0
while True:
    line0 = tlefile.readline()
    line1 = tlefile.readline()
    line2 = tlefile.readline()
#print(f"line0=",{line0})
#print(f"line1=",{line1})
#print(f"line2=",{line2})
    if not line2:
        break
    Constellation.append(Satellite(line0, line1, line2))
    i += 1
tlefile.close()
'''
# print some of the satellite properties as a test
satellite = Constellation[0]
print("Satellite meananom: ", satellite.meanan)
print("Satellite meanmot: ", satellite.meanmo)
print("Satellite right ascension of the ascending node: ", satellite.raan)
print("Satellite eccentricity: ", satellite.eccn)
print("Satellite ndot2: ", satellite.ndot2)
print("Satellite nddot6: ", satellite.nddot6)
print("Satellite inc: ", satellite.incl)
print("Satellite argper: ", satellite.argper)
print("Satellite raan: ", satellite.raan)'''

######################################## PART 2 ####################################
######################################## PART 2 ####################################
######################################## PART 2 ####################################

def anykey(): #this will pause the program until the user presses any key
    print("Press any key to continue...")
    msvcrt.getch() # getch() function reads a single character from the console

#anykey()
######################################################################################

# Define the function with input parameters:
def STKout(EphemFile, StartString, epsec, Coord, time, position, velocity):
    # Open the file in write mode:
    with open(EphemFile, 'w') as f:
        # Write the header information to the file:
        f.write("BEGIN Ephemeris\n")
        f.write(" \n")
        f.write("NumberOfEphemerisPoints " + str(len(time)) + "\n") #f.write("NumberOfEphemerisPoints " + str(len(time, position, velocity))+"\n") 
        f.write(" \n")
        f.write("ScenarioEpoch " + StartString + "\n") # start time of the scenario
        f.write("InterpolationMethod LAgrange\n") # linear interpolation for simplicity
        f.write("InterpolationOrder  7")
        f.write("CentralBody    Earth\n") # assuming the central body is Earth
        f.write("CoordinateSystem " + Coord + "\n") # specified coordinate system   #TEMED
        '''
        # Write the time, position, and velocity data to the file:
        f.write("EphemerisTimePosVel")
        for i in range(len(time)):
            f.write('%-16.14E %-16.14E %-16.14E %-16.14E %-16.14E %-16.14E %-16.14E \n'\
                     %(time[i]+epsec, position[i,0], position[i,1], position[i,2], \
                    velocity[i,0], velocity[i,1], velocity[i,2]))'''
        for i in range(len(time)):
            f.write('%-16.14E %-16.14E %-16.14E %-16.14E %-16.14E %-16.14E %-16.14E \n'\
             %(time[i]+epsec, position[i][0], position[i][1], position[i][2], \
            velocity[i][0], velocity[i][1], velocity[i][2]))

            
        # Write the end of file marker:
        f.write("END Ephemeris\n")
'''
        # Sample input data
EphemFile = "satellite.eph"
StartString = "2023 Mar 18 12:00:00"
epsec = 0
Coord = "TEMED"
time = [0, 1000, 2000, 3000] # in seconds
position = [[0, 0, 0], [100, 200, 300], [200, 400, 600], [300, 600, 900]] # in kilometers
velocity = [[0, 0, 0], [10, 20, 30], [20, 40, 60], [30, 60, 90]] # in kilometers per second

# Call the STKout function
STKout(EphemFile, StartString, epsec, Coord, time, position, velocity)

# Read the contents of the file and print to the terminal
with open(EphemFile, 'r') as f:
    print(f.read())'''

########################################### STKout_sp(SPFile, time, epsec, Azimuth, Elevation)

def STKout_sp(SPFile, time, epsec, Azimuth, Elevation):
    with open(SPFile, 'w') as f:# Open the file in write mode
        f.write("stk.v.4.1.1\n") #stk version
        f.write("Begin   Attitude\n")
        f.write("NumberofAttitudePoints " + str(len(time))+ '\n')
        f.write("Sequence        323\n")
        f.write('AttitudeTimeAzElAngles\n')
        #writing time, az, el data to file as array for length of time
        for i in range(len(time)): 
            f.write('%-6.2f %-6.2f %-6.2f \n' \
                    %(time[i]+epsec, Azimuth[i], Elevation[i]))
        # Write the end of file marker:
        f.write("END Attitude")
'''
    #testing
time = [0.0, 1.0, 2.0, 3.0, 4.0]
epsec = 6.66
azimuth = [10.0, 20.0, 30.0, 40.0, 50.0]
elevation = [60.0, 70.0, 80.0, 90.0, 100.0]
SPFile = "attitude.txt"

# Call the STKout_sp function with the example data:
STKout_sp(SPFile, time, epsec, azimuth, elevation)

# Print the contents of the output file to the terminal:
with open(SPFile, 'r') as f:
    print(f.read())
'''
'''
────────────────████
───────────────█░░███
───────────────█░░████
────────────────███▒██─────████████
──────████████─────█▒█──████▒▒▒▒▒▒████
────███▒▒▒▒▒▒████████████░░████▒▒▒▒▒███
──██▒▒▒▒░▒▒████░░██░░░░██░░░░░█▒▒▒▒▒▒▒███
─██▒▒░░░░▒██░░░░░█▒░░░░░██▒░░░░░░░▒▒▒▒▒▒█
██▒░░░░░▒░░░░░░░░░▒░░░░░░░▒▒░░░░░░░▒▒▒▒▒██
█░░░░░░▒░░░██░░░░░░░░░░░░░██░░░░░░░░▒▒▒▒▒█
█░░░░░░░░█▒▒███░░░░░░░░░█▒▒███░░░░░░░▒▒▒▒█
█░░░░░░░████████░░░░░░░████████░░░░░░▒▒▒▒█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█
██░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░▒▒▒▒█
─█░░░░██░█░░░░░░░░░░░░░░░░░░░░░░░███▒▒▒▒▒█
─█▒▒░░░░█████░░░█░░░░██░░░██░░████░▒▒▒▒▒▒█
─██▒▒░░░░░█████████████████████░░░▒▒▒▒▒▒██
──██▒▒▒▒░░░░░██░░░███░░░██░░░█░░░▒▒▒▒▒▒██
───███▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█████
─────███▒▒▒▒▒▒░░░░░░░░░░░░░▒▒▒▒▒▒████
────────██████████████████████████

'''
##################### Class 2023-03-20 ###############################################
'''Read in TLEs
http://www.celestrak.com/NORAD/elements/gps-ops.txt (http://www.celestrak.com/NORAD/elements/gps-ops.txt)
Here is a snippet of code to read in all satellites in the file. It uses a Python try/except block as follows:'''
tlefile=open(r'D:\school 22-23\4350 Space Hardware\P-setion\gps-ops.txt', 'rt')
SatCons = list()                                                                         #I dOnt UnDerStand
line0=''
i=0
try:
    while True:
        line0=tlefile.readline()
        line1=tlefile.readline()
        line2=tlefile.readline()
        print(line0, "index=",i)
        Satellite_i = Satellite(line0, line1, line2)   #Why is fileio not defined???????????? Changed from:    Satellite_i = Fileio.Satellite(line0, line1, line2)
        SatCons.append(Satellite_i)
        i+=1
except ValueError:
    print("Read in", len(SatCons), "satellites")
    tlefile.close()

    ########
#To print out a Satellite object we can define a __str__(self) method in the class and use as follows
idx=0
for i in range(len(SatCons)):
    if 'PRN_01' in SatCons[i].name:
        print("index=",i)
        idx=i
        print(SatCons[i])
        print("\n\n")
#Extract datetime from Reference Epoch in TLE
# Here we chose GPS satellite {{SatCons[idx].name[-6:]}}, which from the above list is index {{idx}}
# self.RefEpochdt = self.convertRefEpoch()
refepochFloat = SatCons[idx].refepoch

refepochString = str(refepochFloat)

RefEpochdt = dt.datetime.strptime(refepochString[:5],'%y%j')

dfrac = np.modf(refepochFloat)[0]
[rem, hr]= np.modf(dfrac*24)
[rem2, mins] = np.modf(60*rem)
[rem3, secs] = np.modf(60*rem2)
mics = np.modf(rem3*10**6)[1]

RefEpochdt = RefEpochdt.replace(hour=int(hr), minute=int(mins), 
                                second=int(secs), microsecond=int(mics))


print(RefEpochdt.strftime('%d %b %Y %H:%M:%S.%f'))

#Tracking time - datetime object
#20 Mar 2023 16:35:00
trackingtime = dt.datetime(2023, 3, 20, hour=16, minute=35, second=0, microsecond=0)
trackingtime.strftime('%d %b %Y %H:%M:%S.%f')

deltat = trackingtime - RefEpochdt
print(deltat)

epsec = deltat.total_seconds()
print(epsec)

# Read in station data#############################

stnfile=open(r'C:\Notebooks\ENG4350\Station.dat', 'rt')

aro = fio.Station(stnfile)

stnfile.close()
print(aro)

#GMST calculation

J2000dt = dt.datetime(2000, 1, 1, 0, 0, 0)
ttmid = trackingtime.replace(hour=0, minute=0, second=0, microsecond=0)
Since2000 = ttmid - J2000dt
days = Since2000.total_seconds()/86400
print(days)


#%precision 4
hours = (trackingtime - ttmid).total_seconds()/3600.
print(hours)


######################################### Call ########################################
######################################### Call ########################################
######################################### Call ########################################
# Pass in parameter values to OM 
gpsParams = ['gps.M0 = %8.4f' % SatCons[idx].meanan, 'gps.N0 = %14.12f' % SatCons[idx].meanmo, \
                 'gps.eccn = %9.7f' % SatCons[idx].eccn, 'gps.Ndot2 = %3.1e' % SatCons[idx].ndot2, \
                 'gps.Nddot6 = %3.1e' % SatCons[idx].nddot6, 'gps.tstart = %8.1f' % epsec ]
mod.setParameters(gpsParams)
gps_orbParams = ['gps.argper0 = %8.4f' % SatCons[idx].argper, 'gps.incl = %7.4f' % SatCons[idx].incl, \
                 'gps.raan0 = %8.4f' % SatCons[idx].raan ]
mod.setParameters(gps_orbParams)

# ARO Params
aroParams = [ 'aro.stn_lat = %7.4f' % aro.stnlat, 'aro.stn_long = %8.4f' % aro.stnlong, \
             'aro.stn_elev = %6.2f' % aro.stnalt ]
mod.setParameters(aroParams)

# Time Params
tParams = ['d0 = %5.1f' % days, 'hr0 = %7.4f' % hours]
mod.setParameters(tParams)

#Check params have been set

print(SatCons[idx], aro)
mod.getParameters()
'''
___________________________________¶¶¶¶          
________________________¶¶¶¶____¶¶¶¶11¶             
________________________¶¶1¶¶_¶¶¶¶1111¶             
_______________________¶¶111¶¶¶1111111¶             
___________________¶¶¶_¶1111¶¶1111111¶              
___________________¶11¶¶111¶¶111111¶¶               
___________________¶11¶1111¶111111¶¶                
__________________¶¶11¶111¶111111¶¶                 
__________________¶11¶111¶¶111111¶                  
__________________¶11¶111¶1111111¶                  
_________________¶11¶111¶11111111¶                  
_________________¶1¶111¶¶1111111¶¶                  
________________¶1¶¶111¶1111111¶¶                   
_______________¶¶1¶111¶1111111¶¶                    
_______________¶¶¶111¶11111111¶                     
______________¶¶¶11¶¶111111111¶                     
______________¶¶11¶¶111111¶¶¶1¶¶                    
_____________¶11¶¶1111111¶111111¶¶                  
___________¶¶¶¶¶1111111¶¶11111111¶¶¶                
__________¶¶¶1111111¶¶1111111111111¶¶¶              
_________¶¶111111¶¶¶11111111111111111¶¶¶¶           
_________¶111111¶¶1111111111111111111111¶¶¶         
_________¶111111¶1111111111¶¶¶1111111111111¶        
________¶11111111111111111¶¶_¶¶¶¶¶¶¶¶111111¶        
_______¶¶111111111111111¶¶¶________¶111111¶¶        
_______¶11111111111¶¶¶¶¶¶__________¶111111¶         
______¶¶11111111111¶¶_____________¶¶11111¶¶        
______¶111111111111¶______________¶¶11111¶         
_____¶¶111111111111¶________________¶¶¶¶¶¶¶¶¶¶¶¶   
_____¶1111111111111¶________________¶¶¶111111¶¶¶¶  
_____¶1111111111111¶¶_____________¶¶¶111111¶¶¶11¶  
____¶¶1111111111111¶¶¶_________¶¶¶1111111¶¶11111¶  
____¶1111111111111111¶¶¶¶¶¶¶¶¶¶¶111111111¶1111¶¶ 
____¶111111111111111111¶¶¶¶11111111111111¶¶¶¶¶¶  
___¶111111111111111111111111111111111111111¶¶¶   
__¶111111111111111111111111111111111111111¶¶     
¶¶11111111111111111111111111111111111111¶¶¶      
111111111111111111111111111111111¶¶¶¶¶¶¶¶        
111111111111111111111111111111¶¶¶¶               
1111111111111111111111111111¶¶¶                  
111111111111111111111111111¶¶                    
1111111111111111111111111¶¶                      
111111111111111111111111¶¶                       
1111111111111111111111¶¶                         
111111111111111111¶¶¶¶                           
111111111¶¶¶¶¶¶¶¶¶¶                              
111111¶¶¶                                        
¶¶¶¶¶¶¶
'''

mod.setSimulationOptions(["stepSize=2.0", "stopTime=1800."])
mod.getSimulationOptions()

mod.simulate()
mod.getSolutions()

#Extract data for ephemeris files and pointing file

tarr = mod.getSolutions("time")
# tarr shape is (1, npts) - reshape this
time = tarr[0,:]

p_sat_pf = np.zeros((np.size(time),3))
v_sat_pf = np.zeros((np.size(time),3))
(p_sat_pf[:,0], p_sat_pf[:,1], p_sat_pf[:,2]) = mod.getSolutions(["gps.p_sat_pf[1]", "gps.p_sat_pf[2]", 
                                                                 "gps.p_sat_pf[3]"])
(v_sat_pf[:,0], v_sat_pf[:,1], v_sat_pf[:,2]) = mod.getSolutions(["gps.v_sat_pf[1]", "gps.v_sat_pf[2]", 
                                                                 "gps.v_sat_pf[3]"])
np.shape(time), np.shape(p_sat_pf), np.shape(v_sat_pf), p_sat_pf[0,:], v_sat_pf[0,:]

Meanan = mod.getSolutions("gps.M")
Meanan[0,:10]

# Get the ECI position and velocity...
p_sat_eci = np.zeros((np.size(time),3))
v_sat_eci = np.zeros((np.size(time),3))
(p_sat_eci[:,0], p_sat_eci[:,1], p_sat_eci[:,2]) = mod.getSolutions(["p_sat_ECI[1]", "p_sat_ECI[2]", "p_sat_ECI[3]"])
(v_sat_eci[:,0], v_sat_eci[:,1], v_sat_eci[:,2]) = mod.getSolutions(["v_sat_ECI[1]", "v_sat_ECI[2]", "v_sat_ECI[3]"])
np.shape(p_sat_eci), np.shape(v_sat_eci), p_sat_eci[0,:], v_sat_eci[0,:]

#....and the ECF position and velocity...
p_sat_ecf = np.zeros((np.size(time),3))
v_sat_ecf = np.zeros((np.size(time),3))
(p_sat_ecf[:,0], p_sat_ecf[:,1], p_sat_ecf[:,2]) = mod.getSolutions(["p_sat_ECF[1]", "p_sat_ECF[2]", "p_sat_ECF[3]"])
(v_sat_ecf[:,0], v_sat_ecf[:,1], v_sat_ecf[:,2]) = mod.getSolutions(["v_sat_ECF[1]", "v_sat_ECF[2]", "v_sat_ECF[3]"])
np.shape(p_sat_ecf), np.shape(v_sat_ecf), p_sat_ecf[0,:], v_sat_ecf[0,:]

#...and the topo coordinates
p_sat_topo = np.zeros((np.size(time),3))
v_sat_topo = np.zeros((np.size(time),3))
(p_sat_topo[:,0], p_sat_topo[:,1], p_sat_topo[:,2]) = mod.getSolutions(["p_sat_topo[1]", "p_sat_topo[2]", "p_sat_topo[3]"])
(v_sat_topo[:,0], v_sat_topo[:,1], v_sat_topo[:,2]) = mod.getSolutions(["v_sat_topo[1]", "v_sat_topo[2]", "v_sat_topo[3]"])
np.shape(p_sat_topo), np.shape(v_sat_topo), p_sat_topo[0,:], v_sat_topo[0,:]

#...and the topo coordinates
p_sat_topo = np.zeros((np.size(time),3))
v_sat_topo = np.zeros((np.size(time),3))
(p_sat_topo[:,0], p_sat_topo[:,1], p_sat_topo[:,2]) = mod.getSolutions(["p_sat_topo[1]", "p_sat_topo[2]", "p_sat_topo[3]"])
(v_sat_topo[:,0], v_sat_topo[:,1], v_sat_topo[:,2]) = mod.getSolutions(["v_sat_topo[1]", "v_sat_topo[2]", "v_sat_topo[3]"])
np.shape(p_sat_topo), np.shape(v_sat_topo), p_sat_topo[0,:], v_sat_topo[0,:]

#Write Ephemeris files and pointing file

# Choose Periapsis(BLL) vector for the Perifocal X-axis in STK
filename = r'C:\Notebooks\ENG4350\pf_test.e'
CoordSys = 'Custom Sat_perifocal_sys Satellite/'+SatCons[idx].stkname
fio.STKout(filename, RefEpochdt, epsec, CoordSys, time, p_sat_pf, v_sat_pf)


# TEMED is an "Installed" component, but you still need to declare it "Custom"
filename = r'C:\Notebooks\ENG4350\eci_test.e'
CoordSys = 'Custom TEMED CentralBody/Earth'
fio.STKout(filename, RefEpochdt, epsec, CoordSys, time, p_sat_eci, v_sat_eci)


filename = r'C:\Notebooks\ENG4350\ecf_test.e'
CoordSys = 'Fixed'
fio.STKout(filename, RefEpochdt, epsec, CoordSys, time, p_sat_ecf, v_sat_ecf)

filename = r'C:\Notebooks\ENG4350\topo_test.e'
CoordSys = 'Custom MyTopo_Sys Facility/Algonquin'
fio.STKout(filename, RefEpochdt, epsec, CoordSys, time, p_sat_topo, v_sat_topo)


filename=r'C:\Notebooks\ENG4350\pointing_test.sp'
fio.STKOut_sp(filename, time, epsec, Azimuth, Elevation)

GMSTarr = mod.getSolutions("GMST")
GMST = GMSTarr[0,:]

from bokeh.plotting import figure, output_notebook, output_file, show
from bokeh.models import HoverTool
output_notebook()

p = figure(x_range=[0., 1800.], y_range=[0., 360.], 
           width=900, height=700, 
           title="Open Modelica Output - Pointing Angles",
          tools="pan,wheel_zoom,box_zoom,reset,crosshair, save")

p.xaxis.axis_label = 'Time (Epsec)'
p.yaxis.axis_label = 'GMST (deg)'
p.background_fill_color = "khaki"

p.xgrid.grid_line_color = 'black'
p.xgrid[0].grid_line_alpha=0.8
p.xgrid.minor_grid_line_color = 'black'
p.xgrid.minor_grid_line_alpha = 0.2

p.ygrid.grid_line_color = 'black'
p.ygrid[0].grid_line_alpha=0.8
p.ygrid.minor_grid_line_color = 'black'
p.ygrid.minor_grid_line_alpha = 0.25

l1 = p.line(x=time, y=GMST, color='green', line_width=2, legend_label='Elevation')
p.add_tools(HoverTool(renderers=[l1], tooltips=[("(t, GMST)", "($x, $y)"),]))


show(p)
'''
_________________¶¶111111¶11111111111111¶¶111¶____
_________________¶¶11111¶111111111111111¶¶111¶____
________________¶¶111111¶11111111¶¶11¶¶¶¶1111¶____
_______________¶¶1111111111111111¶¶¶¶¶¶¶11111¶____
_____________1¶¶11111111111111111¶¶___¶¶11111¶____
___________¶¶¶¶11111¶1111111¶¶1111¶¶¶11¶11111¶____
_________¶¶¶111111111111111111111111¶¶¶¶11111¶____
_______1¶¶11111111111111111111111111111¶¶¶111¶____
______¶¶111111111111111111111111111111111¶¶¶1¶____
_____¶¶1111111111111111¶11¶¶111111111111111¶¶¶____
____¶¶11111111111111111¶¶¶¶11111111111111111¶¶____
___¶¶1111111111111111111¶¶1111111111111111111¶¶___
__¶¶11111111111111111111¶¶11111111111111111111¶¶__
__¶111111111111111111111¶1111111111111111111111¶__
_¶¶11111111111111111111¶¶1111111111111111111111¶¶_
_¶111111111111111111111¶¶1111111111111111111111¶¶_
_¶111111111111111111111¶¶1111111111111111111111¶¶_
1¶111111111111111111111¶¶1111111111111111111111¶¶_
1¶111111111111111111111¶¶1111111111111111111111¶¶_
1¶111111111111111111111¶¶1111111111111111111111¶1_
_¶1111111111111111111111¶¶11111111111111111111¶¶__
_¶1111111111111111111111¶¶11111111111111111111¶1__
_¶111111111111111111111¶¶¶¶111111111111111111¶¶___
_¶¶1111111111111111111¶¶1¶¶¶¶111111111111111¶¶____
_1¶1111111111111111¶¶¶¶¶¶¶¶¶¶¶¶111111111111¶¶1____
__¶11111111111¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶11111¶¶¶1____
__¶¶1111111111¶¶¶¶11111¶¶_¶¶1111¶¶¶¶1111¶¶¶1¶¶____
__1¶¶¶11111111111111111¶¶_¶1¶1111111111¶¶¶11¶¶____
___¶¶¶¶¶1111111111111111¶¶¶¶1111111111¶¶_¶_1¶¶____
___1¶111¶¶¶11111111111111¶¶¶¶111111¶1¶¶_1¶_11¶____
____¶¶1111¶¶¶111111111111¶¶¶1111111¶¶¶_¶¶1111¶____
____1¶111111¶¶¶1111111111¶1¶¶1111111¶¶¶11¶11¶¶____
_____¶¶1111111¶¶¶¶1111111¶¶¶¶111111111¶1¶¶_1¶¶____
_____1¶1111111111¶¶¶¶1111¶¶1¶¶11111111¶¶¶¶_1¶1____
______¶¶11111111111¶¶¶¶111¶1¶¶111111111¶¶¶__¶1____
______1¶11111111111111¶¶¶¶¶_1¶1111111111¶¶111¶____
_______¶¶111111111111111¶¶¶1¶¶1111111111¶¶¶¶¶¶1___
________¶111111111111111¶¶__1¶¶¶11111111¶¶¶1¶¶¶___
________¶¶111111111111111¶1__1¶1¶¶¶¶¶1111¶¶¶¶¶¶1__
_________¶111111111111111¶¶___¶111¶¶¶¶¶¶¶¶¶¶_1¶___
_________¶¶11111111111111¶¶___¶¶1111111¶¶¶____¶___
__________¶1111111111111¶¶_____¶111111111¶________
__________¶¶111111111111¶¶_____¶¶1111111¶¶________
___________¶111111111111¶1______¶1111111¶¶________
___________¶¶11111111111¶_______¶¶111111¶¶________
____________¶1111111111¶¶________¶111111¶¶________
____________¶¶111111111¶¶________¶¶11111¶¶________
____________1¶111111111¶¶_________¶11111¶¶________
_____________¶¶11111111¶1_________¶¶1111¶¶________
_____________¶¶111¶1111¶__________1¶1111¶¶________
______________¶111¶¶111¶¶__________¶¶1111¶________
______________¶111¶¶111¶¶__________¶¶1111¶________
______________¶11111111¶1__________1¶1¶¶1¶¶_______
_____________¶¶11111111¶____________¶1¶¶11¶_______
____________1¶111111111¶____________¶11__1¶_______
____________¶¶11111111¶¶____________¶¶¶¶¶¶¶_______
____________¶111111111¶¶____________¶¶¶¶¶¶¶_______
____________¶1111111111¶____________¶¶¶¶¶¶¶¶______
___________1¶1111111111¶____________¶¶¶¶¶¶¶¶______
___________1¶1111111111¶1___________¶¶¶¶¶¶¶¶1_____
____________¶1111111111¶¶___________1¶¶¶¶¶¶¶______
____________¶1111111111¶¶____________¶¶¶¶¶¶¶______
____________¶¶111111111¶¶____________¶¶¶¶¶¶¶¶_____
____________1¶1111111111¶_____________¶¶¶¶¶¶¶_____
_____________¶1111111111¶_____________¶¶¶¶¶¶¶¶____
_____________¶¶111111111¶_____________1¶¶¶¶¶¶¶¶___
______________¶111111111¶1____________¶¶¶¶¶¶¶¶¶¶__
______________¶¶11111111¶1____________¶¶¶¶¶¶¶¶¶¶__
_______________¶11111111¶¶___________¶¶¶¶¶¶¶¶¶¶1__
_______________¶¶1111111¶¶___________¶¶¶¶¶¶¶¶¶¶___
________________¶¶111111¶¶____________¶¶¶¶¶¶¶¶____
_________________¶111111¶¶_____________¶¶¶¶¶¶_____
'''