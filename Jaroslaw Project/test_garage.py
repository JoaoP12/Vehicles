import unittest
from microproject import vehicles as vh

class TestGarage(unittest.TestCase):
    
    '''Tests the methods of the class Garage
    '''
    
    def test_insertion(self):
        
        ''' Tests if the vehicles insertion is ok
        '''
        
        vehicles = [vh.Motorcycle('Hornet'),
                    vh.Car('Camaro'),
                    1
                    ]
        garage = vh.Garage(vehicles)
        self.assertEqual(garage, ?)
        
if __name__ == '__main__':
    unittest.main()