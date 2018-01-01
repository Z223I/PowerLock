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

        self.powerRelay = 3
        self.poleA = 40
        self.poleB = 58
        self.heater = PowerLock(self.powerRelay, self.poleA, self.poleB)

    def tearDown(self):
        self.heater = None

    def test_powerRelay(self):
        self.assertEqual(self.heater.powerRelay, self.powerRelay,
                'Wrong relay port.')

    def test_islock(self):
        self.assertFalse(self.heater.isLocked, 'Heater should be off.')

    def test_lock(self):
        self.assertTrue(self.heater.lock(), 'Heater should be lock.')

    def test_unlock(self):
        self.assertFalse(self.heater.unlock(), 'Heater should be off.')



if __name__ == '__main__':
    unittest.main()
