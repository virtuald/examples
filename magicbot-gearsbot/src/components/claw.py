
import wpilib

from magicbot import (
    default_state,
    state,
    timed_state,
    StateMachine
)

class Claw(StateMachine):
    '''
    The claw subsystem is a simple system with a motor for opening and closing.
    If using stronger motors, you should probably use a sensor so that the
    motors don't stall. 
    '''
    
    claw_motor = wpilib.Victor
    claw_contact = wpilib.DigitalInput
    
    #
    # Control functions
    #
    
    def open(self):
        '''Set the claw motor to move in the open direction.'''
        self.engage(initial_state='do_open', force=True)
        
    def close(self):
        '''Set the claw motor to move in the close direction.'''
        self.engage(initial_state='do_close', force=True)
        return self.isGrabbing()
        
    def isGrabbing(self):
        '''Return true when the robot is grabbing an object hard enough
           to trigger the limit switch'''
        return self.contact.get()
    
    #
    # Logic.. this doesn't neatly fit into the state machine construct
    #
    
    @timed_state(duration=1, must_finish=True)
    def do_open(self):
        # TODO: if the user keeps holding this, it will keep opening :(
        self.claw_motor.set(-1)
    
    @state(must_finish=True)
    def do_close(self):
        # Once the grab switch has been triggered, stop the motor
        if self.isGrabbing():
            self.next_state_now(self.default_state)
        else:
            self.claw_motor.set(1)
    
    @default_state
    def default_state(self):
        self.claw_motor.set(0)
