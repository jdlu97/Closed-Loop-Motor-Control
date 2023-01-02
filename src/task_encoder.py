'''!    @file       task_encoder.py
        
        @brief      Runs the encoder driver to receive current encoder position
        @details    Establishes encoder pin values and runs encoder frequently 
                    to provide measured values to closed loop gain.
        
        @author     Juan Luna
        @date       2022-01-31 Original file
        @date       2022-12-30 Modified for portfolio update
'''
import utime
import pyb
import encoder

class Task_Encoder:
    '''! @brief     Task implementing functionality of encoder driver.
    '''
    def __init__(self, encoder_share):
        '''! @brief     Initializes objects of the EncoderDriver class.
             @param  encoder_share  Shared variable storing encoder value.
             @param  ENC1A_pin    First pin object for encoder channel.
             @param  ENC1B_pin    Second pin object for encoder channel.
             @param  tim_ENC_A   Timer object for encoder.
             @param  encoder     Encoder object from the motor driver class.
             @param  period      Period for task execution, in milliseconds.
             @param  next_time      Timing variable for tracking current time.
             @param  start_time     Timing variable tracking starting time. 
        '''  
        self.encoder_share = encoder_share
        
        # ENCODER SETUP VARIABLES
        
        # Define pin objects for encoder channels for encoder
        ENC1A_pin = pyb.Pin.cpu.B6
        ENC1B_pin = pyb.Pin.cpu.B7
        # Define timer objects of specified prescaler and frequency.
        tim_ENC_1 = pyb.Timer(4, prescaler = 0, period = 2**16 - 1)
        # Encoder object
        self.encoder = encoder.Encoder_Driver(ENC1A_pin, ENC1B_pin, tim_ENC_1)
        
        # Timing variables
        self.period = 1
        self.next_time = 0
        self.start_time = utime.ticks_ms()
        
    def run(self):
        '''! @brief Runs the encoder driver and position to shared variable
        '''
        # Calculate current time as the difference between now and last stamp
        self.current_time = utime.ticks_diff(utime.ticks_ms(), self.start_time)
        
        if utime.ticks_diff(self.current_time, self.next_time) >= 0:
            
            # Write encoder reading data value into encoder shared variable
            self.encoder_share.write(self.encoder.read())

            self.next_time = utime.ticks_add(self.current_time, self.period)
            
    def zero(self):
        '''! @brief Zeros the encoder reading.
        '''
        self.encoder.zero()
        