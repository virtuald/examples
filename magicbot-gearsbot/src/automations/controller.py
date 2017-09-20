
from components.claw import Claw
from components.elevator import Elevator
from components.wrist import Wrist

class GearsbotController:
    '''
        Component that controls high level actions of the gearsbot
    '''
    
    claw = Claw
    elevator = Elevator
    wrist = Wrist
    
    def prepare_to_pickup(self):
        '''
            Make sure the robot is in a state to pickup soda cans.
            
            :returns: True when ready
        '''
        opened = self.claw.open()
        horizontal = self.wrist.set_horizontal()
        lowered = self.elevator.set_bottom()
        
        return opened and horizontal and lowered
        
    def pickup(self):
        '''
            Picks up a can
            
            :returns: True when pickup is complete
        '''
        
        if self.claw.close():
            raised = self.wrist.set_raised()
            at_platform = self.elevator.set_platform()
            return raised and at_platform
        
    def place(self):
        '''
            Place a held soda can onto the platform.
            
            :returns: True when can has been placed
        '''
        return self.elevator.set_platform() and \
               self.wrist.set_horizontal() and \
               self.claw.open()
    
    def execute(self):
        pass