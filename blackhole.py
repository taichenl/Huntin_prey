# Black_Hole is singly derived from Simulton, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 2*10, 2*10)
        
        
    def display(self, canvas):
        canvas.create_oval(self._x-self.get_dimension()[0]/2, self._y-self.get_dimension()[1]/2, self._x+self.get_dimension()[0]/2, self._y+self.get_dimension()[1]/2, fill = 'black')
    
    def contains(self, xy):
        if self.distance(xy) <= 10:
            return True
        else:
            return False
        
    def update(self, model):
        a = set()
        for i in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(i.get_location()):
                a.add(i)
        for x in a:
            model.remove(x)
        return a
        
