
import wpilib
from magicbot import tunable

class Wrist:
    '''
    The wrist subsystem is like the elevator, but with a rotational joint instead
    of a linear joint. 
    '''
    
    motor = wpilib.Victor
    pot = wpilib.AnalogPotentiometer
    
    if wpilib.RobotBase.isSimulation():
        kP = 0.05
        kI = 0.0
        kD = 0.0
    else:
        kP = 1.0
        kI = 0.0
        kD = 0.0
        
    horizontal_setpoint = tunable(0)
    raised_setpoint = tunable(-45)
    
    def setup(self):
        self.pid = wpilib.PIDController(self.kP, self.kI, self.kD,
                                        self.pot.get, self.motor.set)
        self.pid.setAbsoluteTolerance(2.5)
        
    def on_enable(self):
        '''Called when autonomous/teleop is enabled'''
        
        # this nonsense should be done by the pidcontroller? maybe. Maybe not.
        self.enabled = False
        self.pid.disable()
        self.motor.set(0)

    def set_horizontal(self):
        '''Move the wrist to be horizontal'''
        if not self.enabled:
            self.pid.enable()
        
        self.pid.setSetpoint(self.bottom_setpoint)
        
        # self.setSetpoint(x)
        # return self.onTarget()
        
    def set_raised(self):
        '''Move the wrist to be raised'''
        if not self.enabled:
            self.pid.enable()
        
        self.pid.setSetpoint(self.raised_setpoint)
        
        # self.setSetpoint(x)
        # return self.onTarget()
    
    def execute(self):
        pass
