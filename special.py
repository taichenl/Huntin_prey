'''
Special inherits from Prey, and it has 50% chance to teleport in 200 range maximum. 
'''
from prey import Prey
import random

class Special(Prey):
    radius = 5
    def __init__(self,x,y):
        self.randomize_angle()
        Prey.__init__(self, x, y, 2*5, 2*5, self._angle, 5)

        
    def update(self, model):
        if random.random() < 0.5:
            changex = (random.random()-0.5) *200
            changey = (random.random()-0.5) *200
            self.set_location(self._x + changex, self._y + changey)
        self.move()
        self.wall_bounce()
        
        
    def display(self, canvas):
        canvas.create_oval(self._x-Special.radius, self._y-Special.radius, self._x+Special.radius, self._y+Special.radius, fill = 'blue')
        