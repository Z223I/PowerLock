import unittest
from PowerLock import PowerLock
from relaypipy import RelayPiPy

class PowerLockTestCase(unittest.TestCase):
    relay4 = None 

    def setUp(self):
        global relay4

        relay4 = RelayPiPy()
        pinList = [ 6, 13, 19, 26 ]
        relay4.init( pinList )

        self.powerRelay = 0
        self.poleA = 1
        self.poleB = 2
        self.powerLock = PowerLock(self.powerRelay, self.poleA, self.poleB)

    def tearDown(self):
        self.powerLock = None

    def test_powerRelay(self):
        self.assertEqual(self.powerLock.powerRelay, self.powerRelay,
                'Wrong relay port.')

    def test_isLocked(self):
        self.assertFalse(self.powerLock.isLocked, 'Should be locked.')

    def test_lock(self):
        self.assertTrue(self.powerLock.lock(), 'Should be locked.')

    def test_unlock(self):
        self.assertFalse(self.powerLock.unlock(), 'Should be unlocked.')



if __name__ == '__main__':
    unittest.main()
