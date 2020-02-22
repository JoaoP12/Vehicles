import unittest

from microproject import vehicles as vh
class TestMotorcycle(unittest.TestCase):

    def test_bike_lights(self):

        '''Tests if the engine functions are working correctly
        '''
        importing_class = vh.Motorcycle('CB600')
        results = importing_class.lights_on_off()
        self.assertEqual(results, True)
        results = importing_class.lights_on_off()
        self.assertEqual(results, False)
        results = importing_class.lights_on_off()
        self.assertEqual(results, True)
        results = importing_class.lights_on_off()
        self.assertEqual(results, False)
            
if __name__ == '__main__':
    unittest.main()