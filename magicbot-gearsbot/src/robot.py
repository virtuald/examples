#!/usr/bin/env python3

import wpilib
from magicbot import MagicRobot

from components.claw import Claw
from components.drivetrain import DriveTrain
from components.elevator import Elevator
from components.wrist import Wrist

from automations.controller import GearsbotController

class MyRobot(MagicRobot):
    '''
        GearsBot demo robot code written using the Magicbot framework
    '''
    
    claw = Claw
    elevator = Elevator
    wrist = Wrist
    drivetrain = DriveTrain
    
    controller = GearsbotController
    
    def createObjects(self):
        
        #
        # DriveTrain
        #
        
        self.front_left_motor = wpilib.Talon(1)
        self.back_left_motor = wpilib.Talon(2)
        self.front_right_motor = wpilib.Talon(3)
        self.back_right_motor = wpilib.Talon(4)

        self.drive = wpilib.RobotDrive(self.front_left_motor,
                                       self.back_left_motor,
                                       self.front_right_motor,
                                       self.back_right_motor)

        self.left_encoder = wpilib.Encoder(1, 2)
        self.right_encoder = wpilib.Encoder(3, 4)
        
        self.rangefinder = wpilib.AnalogInput(6)
        self.gyro = wpilib.AnalogGyro(1)
        
        #
        # Claw
        #
        
        self.motor = wpilib.Victor(7)
        self.contact = wpilib.DigitalInput(5)
        
        #
        # Elevator
        #
        
        self.elevator_motor = wpilib.Victor(5)
        
        # Conversion value of potentiometer varies between the real world and simulation
        if self.isReal():
            self.elevator_pot = wpilib.AnalogPotentiometer(2, -2.0/5)
        else:
            self.elevator_pot = wpilib.AnalogPotentiometer(2)    # defaults to meters
    
        #
        # Wrist
        #
        
        self.wrist_motor = wpilib.Victor(6)
        
        # Conversion value of potentiometer varies between the real world and simulation
        if self.isReal():
            self.wrist_pot = wpilib.AnalogPotentiometer(3, -270/5)
        else:
            self.wrist_pot = wpilib.AnalogPotentiometer(3)    # defaults to degrees
    
        #
        # Joysticks
        #
        
        self.joy = wpilib.Joystick(0)
        
    
    def teleopPeriodic(self):
        
        
        if self.joy.getRawButton(5):
            self.elevator.set_platform()
        
        elif self.joy.getRawButton(7):
            self.elevator.set_bottom()
            
        if self.joy.getRawButton(6):
            self.claw.close()
            
        elif self.joy.getRawButton(8):
            self.claw.open()
        
        if self.joy.getRawButton(12):
            self.controller.prepare_to_pickup()
        
        if self.joy.getRawButton(10):
            self.controller.pickup()
            
        if self.joy.getRawButton(11):
            self.controller.place()
            
        if self.joy.getRawButton(9):
            pass # run autonomous

if __name__ == '__main__':
    wpilib.run(MyRobot)
