#!/usr/bin/python
# -*- coding: utf-8 -*-

#

# Import required libraries

import time
import RPi.GPIO as GPIO
from relaypipy import RelayPiPy


########################################################
#
# Class PowerLock
#
########################################################

class PowerLock:

    """
    This class uses a relay to turn on a water heater
    indirectly.  This class directly powers a water pump
    which activates the portable water heater.

    It takes a single GPIO pin to control the water pump.
    The calling script must have already established
    a RelayPiPy object and called its init method to
    establish which pins are used.  The number of pins
    determines the number of relays.
    """

    relay = RelayPiPy()

########################################################
# method __init__
########################################################

    def __init__(self, _powerRelay, _pollA, _poleB):
        self.isLocked = False
        self.powerRelay = _powerRelay
        self.pollA = _pollA
        self.poleB = _poleB

# TODO tell relay to reserve one relay

#
# End method __init__
#


########################################################
# method unlock
########################################################

    def unlock(self):

        """
        Powers unlock the heater.
        """

        PowerLock.relay.off(self.powerRelay)
        self.isLocked = False
        return self.isLocked

#
# End method unlock
#


########################################################
# method lock
########################################################

    def lock(self):

        """
        Powers on the heater.
        """
#        print "Relay = ", self.powerRelay
#        print "pinList = ", PowerLock.relay.pinList

        PowerLock.relay.on(self.powerRelay)
        self.isLocked = True
        return self.isLocked

#
# End method lock
#


########################################################
# method setpollA
########################################################

    def setpollA(self, _pollA):
        self.pollA = _pollA

#
# End method setpollA
#


########################################################
# method setpoleB
########################################################

    def setpoleB(self, _poleB):
        self.poleB = _poleB


#
# End method setpoleB
#



########################################################
#
# End class PowerLock
#
########################################################
