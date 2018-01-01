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

    def __init__(self, _powerRelay, _poleA, _poleB):
        self.isLocked = False
        self.powerRelay = _powerRelay
        self.poleA = _poleA
        self.poleB = _poleB

#
# End method __init__
#


########################################################
# method unlock
########################################################

    def unlock(self):

        """
        Unlocks the powerlock.
        """

        # Guarantee power is off.
        PowerLock.relay.off(self.powerRelay)

        # Set poles
        PowerLock.relay.off(self.poleA)
        PowerLock.relay.on(self.poleB)
        time.sleep(1) # For test only


        self.powerThenOff()

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
# method setPolarity
########################################################

    def setPolarity(self, _normalPolarity):

        """
        Sets polarity of powerlock.
        """

        if _normalPolarity:
            self.relay.on(self.poleA)
            self.relay.off(self.poleB)
        else:
            self.relay.off(self.poleA)
            self.relay.on(self.poleB)

        return _normalPolarity

#
# End method setPolarity
#


########################################################
# method powerThenOff
########################################################

    def powerThenOff(self):
        # Apply power for a little bit.
        PowerLock.relay.on(self.powerRelay)
        time.sleep(2)

        # Turn the three relays back.
        # Shut of power first.
        PowerLock.relay.off(self.powerRelay)
        PowerLock.relay.off(self.poleA)
        PowerLock.relay.off(self.poleB)

#
# End method powerThenOff
#



########################################################
#
# End class PowerLock
#
########################################################
