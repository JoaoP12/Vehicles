import pandas as pd
import ast
class Garage:
    
    '''Calculates how many places there are for parking and store the vehicles parked
    '''
    
    vehicles = []
    def __init__(self, vehicle):
        self.valor = ast.literal_eval(vehicle)
        
        if type(self.valor) == list:
            for i in vehicle:
                if vehicle(i) != str:
                    print('Just string is supported for vehicles names!')
                    return False
                
                else:
                    self.vehicles.append(vehicle(i))
                    return True
                
        elif self.valor != str:
            print('Just string is supported for vehicles names!')
            return False
        
        else:
            self.vehicles.append(vehicle)
            
        self.parking_places = 4
        self.parked_vehicles = []
        self.unparked_vehicles = []
        
    def park(self):
        
        '''Checks if there are parking places and parks the vehicle if true
        '''
        for vehicle in self.vehicles:
            space = vehicle.parking_space
            if self.parking_places >= space:
                self.parking_places -= space
                self.parked_vehicles.append(vehicle.name)
                print(f"{vehicle.name} parked!")
                return True
            else:
                self.unparked_vehicles.append(vehicle)
                print(f"There is no parking place for {vehicle.name}")
                return False
    
    def vehicles_parked(self):
        
        '''Shows all the vehicles that were parked in the Garage
        '''
        
        data_frame = pd.DataFrame(self.parked_vehicles, columns = ['Name'])
        pd.set_option('display.expand_frame_repr', False)
        print(data_frame)
        return True
    
    def vehicles_unparked(self):
        
        '''Shows all the vehicles that aren't parked in the Garage
        '''
        
        data_frame = pd.DataFrame(self.unparked_vehicles, columns = ['Name'])
        pd.set_option('display.expand_frame_repr', False)
        print(data_frame)
        return True
    
    def all_vehicles(self):
        
        '''Shows all the vehicles that are in the Garage, parked or not
        '''
        all_vehicles = self.parked_vehicles + self.unparked_vehicles
        data_frame = pd.DataFrame(all_vehicles, columns = ['Name'])
        pd.set_option('display.expand_frame_repr', False)
        print(data_frame)
        return True
                
class Vehicle:
    
    '''The parent class, turn on and off the engine
    '''
    
    engine_on_off = False
    
    def __init__(self, name):
        self.name = name
        

    def turn_engine_on_off(self):
        
        '''If the engine is off, then it turns it on, and if it is already on, it turns it off
        '''
        
        if self.engine_on_off:
            self.engine_on_off = False
            print("{}'s engine is off".format(self.name))
            return self.engine_on_off
        else:
            self.engine_on_off = True
            print("{}'s engine on".format(self.name))
            return self.engine_on_off
        
class Car(Vehicle):
    
    '''Stores the cars
    '''
    
    hand_brake = False
    parking_space = 1
    
    def pull_push_hand_brake(self):

        '''Pulls car's hand brake
        '''
        
        if self.hand_brake:
            self.hand_brake = False
            print("{}'s hand brake pushed!".format(self.name))
            return self.hand_brake
        else:
            self.hand_brake = True
            print("{}'s hand brake pulled!".format(self.name))
            return self.hand_brake
                  
class Motorcycle(Vehicle):
    
    '''Stores the motorcycles
    '''
    
    lights = False
    parking_space = 0.5
    def lights_on_off(self):
                  
        '''Turns the motorcycle lights on or off
        '''

        if self.lights:
            self.lights = False
            print("{}'s lights off!".format(self.name))
            return self.lights
        else:
            self.lights = True
            print("{}'s lights on!".format(self.name))
            return self.lights
        
vehicle = Motorcycle('Hornet')
garage_vehicles = Garage(vehicle)
garage_vehicles.park()
garage_vehicles.vehicles_parked()
garage_vehicles.vehicles_unparked()
garage_vehicles.all_vehicles()