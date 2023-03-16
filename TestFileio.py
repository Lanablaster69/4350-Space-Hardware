import datetime
import platform
import urllib
import winsound
import msvcrt
from collections import namedtuple
from Fileio import BANNER, ERRMSG, Station, Satellite

# Test BANNER function
print("BANNER():")
BANNER()

# Test ERRMSG function
print("\nERRMSG():")
ERRMSG("Test error message")

# Test Station class
print("\nStation class:")
stn = Station('STNFIL')
print("stn.name:", stn.name)  
print("stn.stnlat:", stn.stnlat)  
print("stn.stnlong:", stn.stnlong)  
print("stn.stnalt:", stn.stnalt)  
print("stn.utc_offset:", stn.utc_offset)  
print("stn.az_el_nlim:", stn.az_el_nlim)  
print("stn.az_el_lim_1:", stn.az_el_lim_1)  
print("stn.st_az_speed_max:", stn.st_az_speed_max) 
print("stn.st_el_speed_max:", stn.st_el_speed_max)  

# Test Satellite class
# Get latest GPS data from Celestrak web site, write it to a file
tlefile = open(r'D:\school 22-23\4350 Space Hardware\P-setion\gps-ops.txt', 'wt')
tleurl = 'https://celestrak.com/NORAD/elements/gps-ops.txt'
for line in urllib.request.urlopen(tleurl):
    tlefile.write('%s' % line.decode().rstrip('\n'))
tlefile.close()

# Open the file we just wrote and create a list of Satellite objects
tlefile = open(r'D:\school 22-23\4350 Space Hardware\P-setion\gps-ops.txt', 'rt')
Constellation = []
while True:
    line0 = tlefile.readline()
    line1 = tlefile.readline()
    line2 = tlefile.readline()
    if not line2:
        break
    Constellation.append(Satellite(line0, line1, line2))
tlefile.close()

# Print some of the satellite properties as a test
print("\nSatellite class:")
satellite = Constellation[0]
print("satellite.name:", satellite.name)
print("satellite.inclination:", satellite.incl)
print("satellite.right_ascension_of_the_ascending_node:", satellite.raan)
print("satellite.eccentricity:", satellite.eccn)
