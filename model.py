import controller, sys
import model   # Pass a reference to this model module to update calls in update_all


from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
things = set()
cycle = 0
one_cycle = False
type1 = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count, things, type1
    running     = False
    things       = set()
    cycle = 0 
    type1 = None


#start running the simulation
def start ():
    global running, one_cycle
    one_cycle = False
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global one_cycle, running
    one_cycle = True
    running = True
    
#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global type1
    type1 = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if type1 == None:
        pass
    elif type1 == 'Remove':
        for i in find(lambda a : a.contains((x, y))):
            remove(i)
    else:
        things.add(eval(type1+'('+str(x)+','+str(y)+')'))


#add simulton s to the simulation
def add(s):
    global things
    things.add(s)

# remove simulton s from the simulation    
def remove(s):
    global things
    things.remove(s)
    
#find/return a set of simultons that each satisfy predicate p    
def find(p):
    a = set()
    for i in things:
        if p(i):
            a.add(i)
    return a 


#call update \(pass model as its argument\) for every simulton in the simulation
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global running,cycle, things, type1
    if running:
        cycle += 1
        b = [x for x in things]
        for i in b:
            i.update(model)
        if one_cycle:
            running = False


#delete every simulton from the canvas in the simulation; then call display on each
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in things:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(things))+" Simulton/"+str(cycle)+" cycles")
    
