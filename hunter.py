# Hunter is doubly-derived from the Mobile_Simulton and Pulsator classes:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        self.randomize_angle()
        Mobile_Simulton.__init__(self, x, y, self.get_dimension()[0], self.get_dimension()[1], self._angle, 5)   
        
    def update(self, model):
        set1 = Pulsator.update(self, model)
        preylist = model.find(lambda x : isinstance(x, Prey))
        preylist = [x for x in preylist if self.distance(x.get_location()) <= 200]  
        distancelist = [self.distance(x.get_location()) for x in preylist] 
        if preylist:  
            for i in preylist:
                if self.distance(i.get_location()) == min(distancelist):
                    self.set_angle(atan2(i.get_location()[1]-self.get_location()[1],i.get_location()[0]-self.get_location()[0]))
        self.move()
        return set1
        
            
            