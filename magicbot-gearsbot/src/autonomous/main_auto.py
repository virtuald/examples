
from magicbot import AutonomousStateMachine, state

from automations.controller import Controller

def wait_until():
    pass

def wrap():
    pass

class MainAuto(AutonomousStateMachine):
    MODE_NAME = "Delivery"
    DEFAULT = True
    
    controller = Controller
    
    # .. problem: need to set something in motion, and be notified 
    #             when it completes
    
    # .. automations have the same problem
    def do_something(self):
        self.until(self.wrist.set_raised())
    
    # this is the meta thing..
    # .. continues calling function until it returns True?
    # .. continues calling function until enabled returns False?
    raise_wrist = wait_until(wrist.set_raised, next='lower_wrist')
    
    # the big problem here is that state machines aren't designed to be executed
    # continuously? Or rather.
    
    # the problem is that if I say "raised", I don't find out until at least 20ms
    # later that "raised has happened"
    
    @state(first=True)
    def prepare_to_pickup(self):
        if self.controller.prepare_to_pickup():
            self.next_state(self.pickup)
    
    # prepare to pickup
    # pickup
    # set distance to box (0.10)
    # drive straight 4 
    # place
    # set distance to box 0.60
    # drive straight -2
    # set wrist setpoint -45
    # close claw
    
