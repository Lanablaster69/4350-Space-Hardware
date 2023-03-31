import datetime
import platform
#import sys
#import os
import urllib
import winsound
import msvcrt  # only works on windows Microsoft! Visual C/C++ Runtime Library
import Datefun as df
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
    #sys.exit()                            I COMMENTED THIS OUT

#ERRMSG("test error")

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
        self.name = line0.strip()#.replace(' ','_')
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
        self.line0 = line0
        self.line1 = line1
        self.line2 = line2
        self.SSC = float(line1[2:6])
        self.refepochdt = df.ep2dat(line1[18:32])
    
    def wasif(self):
        print("Satellite name: " + self.name)
        #print("SSC Number: "+ self.SSC)
        print("Ref Epoch, ndot2, nndot6, bstar: " + str(self.refepoch) + ", " + str(self.ndot2) + ", " + str(self.nddot6) + ", " + str(self.bstar))
        print("Eccentricity, Inclination, RAAN, ArgPer, MeanAnom, meanmotion:  "+str(self.eccn), str(self.incl), str(self.raan) , str(self.argper) , str(self.meanan) , str(self.meanmo) , str(self.orbitnum))
        print("TLE data: " + self.line0,self.line1,self.line2)
        print("refepoch" + str(self.refepochdt))
"""
    def __str__(self):
        str="Satellite name: %s \n" %self.name
        #print("SSC Number: "+ self.SSC)
        str+="Ref Epoch, ndot2, nndot6, bstar:  %8.4f \n " + %s(self.refepoch) + ", " + str(self.ndot2) + ", " + str(self.nddot6) + ", " + str(self.bstar))
        ("Eccentricity, Inclination, RAAN, ArgPer, MeanAnom, meanmotion: %8.4f \n "+str(self.eccn), str(self.incl), str(self.raan) , str(self.argper) , str(self.meanan) , str(self.meanmo) , str(self.orbitnum))
        ("TLE data: " + self.line0,self.line1,self.line2)
"""
SatCons = []
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
    SatCons.append(Satellite(line0, line1, line2))
    i += 1
tlefile.close()
#print(SatCons)
#SatCons[0].wasif()
'''
# print some of the satellite properties as a test
satellite = SatCons[0]
print("Satellite meananom: ", satellite.meanan)
print("Satellite meanmot: ", satellite.meanmo)
print("Satellite right ascension of the ascending node: ", satellite.raan)
print("Satellite eccentricity: ", satellite.eccn)
print("Satellite ndot2: ", satellite.ndot2)
print("Satellite nddot6: ", satellite.nddot6)
print("Satellite inc: ", satellite.incl)
print("Satellite argper: ", satellite.argper)
print("Satellite raan: ", satellite.raan)
'''
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

        # Sample input data
'''
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
    print(f.read())
'''
def STKout(EphemFile, StartString, epsec, Coord, time, position, velocity):
    num_points = len(time)
    to_write = []
    to_write.append("stk.v.4.3")
    to_write.append("")
    to_write.append("BEGIN Ephemeris")
    to_write.append("")
    to_write.append("NumberOfEphemerisPoints " + str(num_points))
    to_write.append("")
    to_write.append("ScienarioEpoch " + StartString)
    to_write.append("InterpolationMethod Lagrange")
    to_write.append("InterpolationOrder 7")
    to_write.append("CentralBody Earth")
    to_write.append("CoordinateSystem " + Coord)
    to_write.append("")
    to_write.append("EphemerisTimePosVel")
    to_write.append("")

    for i in range(num_points):
        to_write.append(str(time[i]) + " " 
                        + str(position[i][0]) + " "
                        + str(position[i][1]) + " " 
                        + str(position[i][2]) + " "
                        + str(velocity[i][0]) + " "
                        + str(velocity[i][1]) + " "
                        + str(velocity[i][2]))

    to_write.append("")
    to_write.append("END Ephemeris")

    for i in range(len(to_write)):
        to_write[i] += "\n"

    with open("thing.e", 'w') as file:
        file.writelines(to_write)

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

################ Class notes below #####################
#####################
'''
TLEFile= open(tleFile, 'rt')
satcons = list()
line0=''
i=0
try:
    while True:
        line0= tleFile.readline
        line1= tleFile.readline
        line2= tleFile.readline
        Satellite_i = fio.Satellite(line0, line1, line2)
        print(Stlellite_i)
        i+=1
except ValueError:
    print("read in", len(SatCons), "satellites")
    tleFile.close

    '''#lots of typos above

'''
#####################
idx=0
for sat in SatCons:
    if "PRN 01" in sat.line0:
        idx = SatCons.index(sat)
        print("index=", idx)
        print(sat)'''
