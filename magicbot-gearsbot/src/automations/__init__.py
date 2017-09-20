
from magicbot import StateMachine, state

class Pickup(StateMachine):
    pass
    
    # close claw and set wrist setpoint to -45
    # set elevator to 0.25
    
    
class Place(StateMachine):
    pass
    
    # set elevator to 0.25
    # set wrist to 0
    # open claw

class PrepareToPickup:
    pass
    
    # open claw and set write to 0
    # set elevator to 0