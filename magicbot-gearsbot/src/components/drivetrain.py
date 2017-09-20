
import wpilib

from magicbot import will_reset_to

class DriveTrain:
    '''The DriveTrain subsystem incorporates the sensors and actuators attached to
       the robots chassis. These include four drive motors, a left and right encoder
       and a gyro.
    '''
    
    drive = wpilib.RobotDrive
    
    left = will_reset_to(0)
    right = will_reset_to(0)
    
    def driveManual(self, left, right):
        ''' Tank style driving for the DriveTrain. 
            
            :param left: Speed in range [-1, 1]
            :param right: Speed in range [-1, 1]
        '''
        self.left = left
        self.right = right
        
    def driveJoystick(self, joy):
        ''':param joy: The ps3 style joystick to use to drive tank style'''
        self.left = -joy.getY()
        self.right = -joy.getAxis(wpilib.Joystick.AxisType.kThrottle)
        
    def getHeading(self):
        ''' :returns: The robots heading in degrees'''
        return self.gyro.getAngle()
        
    def reset(self):
        '''Reset the robots sensors to the zero states'''
        self.gyro.reset()
        self.left_encoder.reset()
        self.right_encoder.reset()
        
    def getDistance(self):
        ''' :returns: The distance driven (average of left and right encoders)'''
        return (self.left_encoder.getDistance() + self.right_encoder.getDistance()) / 2.0

    def getDistanceToObstacle(self):
        ''' :returns: The distance to the obstacle detected by the rangefinder'''
        
        # Really meters in simulation since it's a rangefinder...
        return self.rangefinder.getAverageVoltage()
        
    def execute(self):
        self.drive.tankDrive(self.left, self.right)
        