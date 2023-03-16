import datetime
import platform
#import sys
#import os
import urllib
import winsound
import msvcrt  # only works on windows Microsoft! Visual C/C++ Runtime Library
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
BANNER()

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
    #sys.exit()                            I COMMENTED THIS OUT

ERRMSG("test error")

##################STATION############

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

################# Test ############################

stn = Station('STNFIL') #create an instance of station

print(stn.name)  
print(stn.stnlat)  
print(stn.stnlong)  
print(stn.stnalt)  
print(stn.utc_offset)  
print(stn.az_el_nlim)  
print(stn.az_el_lim_1)  
print(stn.st_az_speed_max) 
print(stn.st_el_speed_max)  


##################Satellite###########################

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
Constellation = []
    
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

# print some of the satellite properties as a test
satellite = Constellation[0]
print("Satellite name: ", satellite.name)
print("Satellite inclination: ", satellite.incl)
print("Satellite right ascension of the ascending node: ", satellite.raan)
print("Satellite eccentricity: ", satellite.eccn)


'''
parameters needed from OME
  Real r "Satellite radius(km)";
  Real theta "Satellite true anomaly (deg)";
  Real E "eccentric Anomaly (deg)";
  Real M "Mean Anomaly (deg)";
  '''

#TEMED

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
        f.write("NumberOfEphemerisPoints " + str(len(time, position, velocity))+"\n") 
        f.write(" \n")
        f.write("ScenarioEpoch " + StartString + "\n") # start time of the scenario
        f.write("InterpolationMethod LAgrange\n") # linear interpolation for simplicity
        f.write("InterpolationOrder  7")
        f.write("CentralBody    Earth\n") # assuming the central body is Earth
        f.write("CoordinateSystem " + Coord + "\n") # specified coordinate system
        
        # Write the time, position, and velocity data to the file:
        f.write("EphemerisTimePosVel")
        for i in range(len(time)):
            f.write('%-16.14E %-16.14E %-16.14E %-16.14E %-16.14E %-16.14E %-16.14E \n'\
                     %(time[i]+epsec, position[i,0], position[i,1], position[i,2], \
                    velocity[i,0], velocity[i,1], velocity[i,2]))
            
        # Write the end of file marker:
        f.write("END Ephemeris\n")


########################################### STKout_sp(SPFile, time, epsec, Azimuth, Elevation)

def STKout_sp(SPFile, time, epsec, Azimuth, Elevation):
    # Open the file in write mode:
    with open(SPFile, 'w') as f:
         # Write the header information to the file:
        f.write("stk.v.4.1.1\n")
        f.write("Begin   Attitude\n")
        f.write("NumberofAttitudePoints " + str(len(time, Azimuth, Elevation))+ '\n')
        f.write("Sequence        323\n")
        f.write('AttitudeTimeAzElAngles\n')
        for i in range(len(time)):
            f.write('%-6.2f %-6.2f %-6.2f \n' \
                    %(time[i]+epsec, Azimuth[i], Elevation[i]))
        # Write the end of file marker:
        f.write("END Attitude")

    
