import Fileio as fio
import Datefun
import numpy as np
import datetime as dt
##from OMPython import ModelicaSystem
#mod=ModelicaSystem("D:/school 22-23/4350 Space Hardware/P-setion","Sattrak.Sattest", ["Modelica.Constants"])
import urllib



#Read in TLEs
# Get latest GPS data from Celestrak web site, write it to a file
tlefile=r'D:\school 22-23\4350 Space Hardware\P-setion\gps-ops.txt'
Scenariofile=r'D:\school 22-23\4350 Space Hardware\P-setion\gps-ops.txt'
tleurl = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=gps-ops&FORMAT=tle'

# Write the file to the same directory as the code
urllib.request.urlretrieve(tleurl, tlefile)

# Write the same file to the STK Scenario directory
urllib.request.urlretrieve(tleurl, Scenariofile)

# Open the code copy of the GPS TLE file and read in the satellites
TLEfile=open(tlefile, 'rt')

SatCons = list()
line0=''
i=0
try:
    while True:
        line0=TLEfile.readline()
        line1=TLEfile.readline()
        line2=TLEfile.readline()
        Satellite_i = fio.Satellite(line0, line1, line2)
        Satellite_i.wasif()
        SatCons.append(Satellite_i)
        i+=1
except ValueError:
    print("Read in", len(SatCons), "satellites")
    TLEfile.close()

# Obect Printing
satrack =0
idx=0
for sat in SatCons:
    if 'PRN 01' in sat.name:
        satrack=sat
        idx = SatCons.index(sat)
        print("index=", idx)
        sat.wasif()
        #I think I pass stuff to openmodelica here?? IDK
#20 Mar 2023 16:35:00
trackingtime = dt.datetime(2023, 3, 20, hour=16, minute=35, second=0, microsecond=0)
trackingtime.strftime('%d %b %Y %H:%M:%S.%f')
deltat = trackingtime.second - satrack.refepoch 
print("delta t = "+ str(deltat))
#deltat
epsec = deltat




#Extract datetime from Reference Epoch in TLE
#refEp = fio.Satellite(refepoch)                                 #HELP
Epoch = Datefun.ep2dat(str(satrack.refepoch)  )                           #HELP

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


