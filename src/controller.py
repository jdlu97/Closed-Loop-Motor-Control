'''! @file      controller.py
     @brief     A driver implementing proportional closed-loop control.
     @details   Computes the actuation value by multiplying the signal by the
                proportional controller gain, Kp. The error is found by
                calculating the difference between the setpoint (desired) value
                and measured value.
     @author    Cade Liberty
     @author    Juan Luna
     @author    Marcus Monroe
     @date      February 03, 2022
'''

class controller:
    '''! @brief     Driver class implementing proportional control.
        @details    Methods of this class set up attributes and methods
                    responsible for calculating the actuation value to be
                    sent to the motor for closed-loop control.
    '''

    def __init__(self, setpoint, gain_share):
        '''! @brief  Initializes objects of the EncoderDriver class.
             @param  setpoint  Chosen motor position value.
             @param  gain      Proportional gain value, Kp.
        '''  
        self.setpoint = setpoint
        self.gain = gain_share
    
    def run(self, measured, gain_share):
        '''! @brief Runs closed loop control calculation.
             @param error       Difference between setpoint and measured values.
             @param measured    Measured position value from encoder.
        '''
        self.error = float(self.setpoint) - float(measured)
        self.gain = float(gain_share.read())
        return (self.error*self.gain)
    
    def setpoint(self, setpoint):        
        '''! @brief  Establishes new reference value.
             @param setpoint  Reference value selected by user.
        '''
        self.setpoint = setpoint
        
    def set_gain(self, gain):
        '''! @brief Establishes new proportional gain value.
             @param gain  Kp value, the proportional gain.
        '''
        self.gain = gain
    