# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 

    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.count = 0
        
    
    def update(self, model):
        self.count += 1
        set1 = Black_Hole.update(self, model)
        size = len(set1)
        if size:
            self.count = 0
            self.change_dimension(size, size)
        elif self.count == 30:
            self.change_dimension(-1, -1)
            self.count = 0
            if self.get_dimension() == (0,0):
                model.remove(self)
        
        return set1
            
        
