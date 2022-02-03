'''! @file    task_controller.py
     @brief   Runs controller driver implementing proportional closed-loop control.  
     @details Takes encoder values and passes it through the controller driver
              to get new duty cycle.
     @author  Cade Liberty
     @author  Juan Luna
     @author  Marcus Monroe
     @date    January 31, 2022
'''
import utime
import controller
import array

class TaskController:
     '''! @brief    Task implementing controller functionality to perform
                    closed loop control on motor.
     '''
     def __init__(self, encoder_share, motor_share, gain_share):
         '''! @brief Sets
              @param  encoder_share  Shared variable for the encoder.
              @param  motor_share    Shared variable to set new duty cycle.
              @param  gain_share     Shared variable for the Kp gain.
              @param  controller     Controller driver object to be used in task.
              @param  period         Period for task execution, in milliseconds.
              @param  record_period  Period for data recording, in milliseconds.
              @param  next_time      Timing variable for tracking current time.
              @param  start_time     Timing variable tracking starting time.
              @param  previous_time  Timing variable tracking last recorded time.
              @param  record_time    Timing variable for data recording.
              @param  time_list      Array for time stamps, in milliseconds.
              @param  position_list  Array for encoder position values. 
         '''
         # Share variables
         self.encoder_share = encoder_share
         self.motor_share = motor_share
         self.gain_share = gain_share
        
         # Controller object
         self.controller = controller.controller(16384, gain_share)
        
         # Timing variables
         self.period = 5
         self.record_period = 5
         self.next_time = 0
         self.start_time = utime.ticks_ms()
         self.previous_time = self.start_time
         self.record_time = 0
         
         # Arrays for time and position data values
         self.time_list = array.array( 'i', [600]*0)
         self.position_list = array.array( 'f', [600]*0)
        
     def run(self):
         '''! @brief Runs the controller task and sets new duty cycle 
         '''
         self.current_time = utime.ticks_diff(utime.ticks_ms(), self.start_time)
        
         if utime.ticks_diff(self.current_time,self.next_time) >=0:
            
            true_position = float(self.encoder_share.read())
            
            self.calc_error = self.controller.run(true_position, self.gain_share)
            #print(self.calc_error)
       
            self.motor_share.write(float(self.calc_error))

            self.next_time = utime.ticks_add(self.current_time, self.period)
            self.previous_time = self.current_time
           
            if utime.ticks_diff(self.current_time,self.record_time) >=0: 
                self.time_list.append(self.current_time)
                self.position_list.append(true_position)
                self.record_time = utime.ticks_add(self.current_time, self.record_period)
        
            
     def prints(self):
            '''! @brief Runs the controller task and sets new duty cycle 
            '''
            print('start')
            
            for k in range(299):
                self.time = utime.ticks_diff(self.time_list[k], self.time_list[0])
                print(self.time  ,',', self.position_list[k])
            print('stop')
                
            #self.time_list = []
            #self.position_list = []
        

                    