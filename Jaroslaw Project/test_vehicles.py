import unittest

from microproject import vehicles as vh
class TestVehicles(unittest.TestCase):

    def test_engine(self):

        '''Tests if the engine functions are working correctly
        '''
        importing_class = vh.Vehicle('Camaro')
        results = importing_class.turn_engine_on_off()
        self.assertEqual(results, True)
        results = importing_class.turn_engine_on_off()
        self.assertEqual(results, False)
        results = importing_class.turn_engine_on_off()
        self.assertEqual(results, True)
        results = importing_class.turn_engine_on_off()
        self.assertEqual(results, False)
            
if __name__ == '__main__':
    unittest.main()
