import unittest
from PowerLock import PowerLock
from relaypipy import RelayPiPy


relay4 = None 

relay4 = RelayPiPy()
pinList = [ 6, 13, 19, 26 ]
relay4.init( pinList )

powerRelay = 0
poleA = 1
poleB = 2
powerLock = PowerLock(powerRelay, poleA, poleB)

powerLock.lock()
powerLock.unlock()
