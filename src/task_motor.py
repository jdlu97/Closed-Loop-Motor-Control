'''!    @file       task_motor.py
        @brief      This module implements a motor task for Lab 02.
        @details    Implements functionality of motor driver to set the percent
                    duty cycle of the motor given by the output of the controller.
        @author     Cade Liberty
        @author     Juan Luna
        @author     Marcus Monroe
        @date       Febraury 03, 2022
'''

import utime
import pyb
import motor

class task_motor:
    '''! @brief     Task implementing functionality of motor driver.
    '''
    def __init__(self, motor_share):
        '''! @brief  Sets relevant pin variables for the motor.
             @param  motor_share    Shared variable communicating duty cycle value
             @param  ENA            Enable pin object for the motor.
             @param  IN1A_pin       Control pin 1 associated with motor.
             @param  IN2A_pin       Control pin 2 associated with motor.
             @param  tim_MOT_A      Timer object for motor.
             @param  motor          Motor object from the motor driver class.
             @param  period         Period for task execution, in milliseconds.
             @param  next_time      Timing variable for tracking current time.
             @param  start_time     Timing variable tracking starting time.
        '''
        # Motor share variable
        self.motor_share = motor_share
        # Define enable pin objects
        ENA = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
        # Define control pin objects associated with first motor.
        IN1A_pin = pyb.Pin.cpu.B4
        IN2A_pin = pyb.Pin.cpu.B5
        # Define timer object for motor with 20-kHz frequency.
        tim_MOT_A = pyb.Timer(3, freq=20000)
        # Motor object
        self.motor = motor.MotorDriver(ENA, IN1A_pin, IN2A_pin, tim_MOT_A)
        # Timing variables
        self.period = 5
        self.next_time = 0
        self.start_time = utime.ticks_ms()
        
    def run(self):
        '''! @brief Runs motor driver with shared dutycycle from controller
        '''
        self.current_time = utime.ticks_diff(utime.ticks_ms(), self.start_time)
        
        if utime.ticks_diff(self.current_time,self.next_time) >=0:
            
            # Read duty cycle from shared variable
            x = self.motor_share.read()
            # Set duty cycle
            self.motor.set_duty_cycle(float(x))
            
            self.next_time = utime.ticks_add(self.current_time, self.period)