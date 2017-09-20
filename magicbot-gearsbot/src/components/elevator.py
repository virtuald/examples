
import wpilib
from magicbot import tunable

class Elevator:
    '''
    The elevator subsystem uses PID to go to a given height. Unfortunately,
    in it's current state PID values for simulation are different than in
    the real world due to minor differences.
    '''
    
    motor = wpilib.Victor
    pot = wpilib.AnalogPotentiometer
    
    if wpilib.RobotBase.isSimulation():
        kP = 18
        kI = 0.2
        kD = 0.0
    else:
        kP = 4
        kI = 0.07
        kD = 0.0
    
    top_setpoint = tunable(0.5)
    platform_setpoint = tunable(0.25)
    bottom_setpoint = tunable(0.0)
    
    def setup(self):
        self.pid = wpilib.PIDController(self.kP, self.kI, self.kD,
                                        self.pot.get, self.motor.set)
        self.pid.setAbsoluteTolerance(0.005)
    
    
    def on_enable(self):
        '''Called when autonomous/teleop is enabled'''
        self.enabled = False
        self.pid.disable()
        self.motor.set(0)
    
    def set_bottom(self):
        if not self.enabled:
            self.pid.enable()
            self.enabled = True
        
        self.pid.setSetpoint(self.bottom_setpoint)
        
        # self.setSetpoint(x)
        # return self.onTarget()
        
    def set_platform(self):
        if not self.enabled:
            self.pid.enable()
            self.enabled = True
        
        self.pid.setSetpoint(self.platform_setpoint)
        
        # self.setSetpoint(x)
        # return self.onTarget()
        
    def set_top(self):
        if not self.enabled:
            self.pid.enable()
            self.enabled = True
        
        self.pid.setSetpoint(self.top_setpoint)
        
        # self.setSetpoint(x)
        # return self.onTarget()
    
    def execute(self):
        pass
    