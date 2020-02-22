import unittest

from microproject import vehicles as vh
class TestCar(unittest.TestCase):

    def test_handbrake(self):

        '''Tests if the engine functions are working correctly
        '''
        importing_class = vh.Car('Camaro')
        results = importing_class.pull_push_hand_brake()
        self.assertEqual(results, True)
        results = importing_class.pull_push_hand_brake()
        self.assertEqual(results, False)
        results = importing_class.pull_push_hand_brake()
        self.assertEqual(results, True)
        results = importing_class.pull_push_hand_brake()
        self.assertEqual(results, False)
            
if __name__ == '__main__':
    unittest.main()