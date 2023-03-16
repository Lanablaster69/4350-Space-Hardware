import Datefun

# Test doy function
print("Test doy function:")
print("doy(2023, 3, 16) =", Datefun.doy(2023, 3, 16))
print("doy(2022, 12, 31) =", Datefun.doy(2022, 12, 31))

# Test frcofd function
print("Test frcofd function:")
print("frcofd(1, 30, 0) =", Datefun.frcofd(1, 30, 0))
print("frcofd(0, 0, 0) =", Datefun.frcofd(0, 0, 0))

# Test ep2dat function
print("Test ep2dat function:")
print("ep2dat('22075.45887149') =", Datefun.ep2dat('22075.45887149'))
print("ep2dat('21001.00000000') =", Datefun.ep2dat('21001.00000000'))

# Test curday function
print("Test curday function:")
print("curday() =", Datefun.curday())
