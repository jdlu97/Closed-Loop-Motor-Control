'''!    @file       main.py
        
        @brief      Main script for execution of Lab 02: Closed-Loop Motor Control.
        @details    Imports modules responsible for executing tasks implementing
                    closed-loop position control on a DC motor. Cooperative
                    multi-tasking is used to run tasks sequentially and share
                    resources. 

        @author     Juan Luna
        @author     Cade Liberty
        @author     Marcus Monroe
        
        @date       Febraury 03, 2022
'''

import task_controller
import task_encoder
import task_motor
import shares

if __name__ == '__main__':
    
    # Define share variables to link data among tasks
    motor_share = shares.Share(0)
    encoder_share = shares.Share(0)
    gain_share = shares.Share(0)
    
    # Tasks to run the controller, motor, and encoder scripts
    task_ctrl = task_controller.TaskController(encoder_share, motor_share, gain_share)
    task_mot  = task_motor.task_motor(motor_share)
    task_enc  = task_encoder.task_encoder(encoder_share)
    
    # Define a Boolean variable that tells when an input has been given
    key_press = True
    
    # Define a counter variable to counts the how many times code has looped.
    count = 0
    
    # Define a Boolean variable that tells if the user has inputed a Kp value.
    serial_input = False
    
    while(True):

        if serial_input == False:
            # Defines an intermediate variable for the serial info to come into.
            x = input()
            # Update value of the share variable
            gain_share.write(x)
            print('The gain you entered is ', gain_share.read())
            serial_input = True

        elif serial_input == True:
            try:
                # Execute tasks for closed-loop control
                task_mot.run()
                task_enc.run()
                task_ctrl.run()
                count +=1

                if count >= 5000:
                    if  16057 >=  encoder_share.read() <= 16711:
                        motor_share.write(0)
                        serial_input = False
                        count = 0
                        task_ctrl.prints()
                        task_enc.zero()
                            
                    elif count > 1000:
                        motor_share.write(0)
                        serial_input = False
                        count = 0
                        task_ctrl.prints()
                        task_enc.zero()

            # Break out of loop on Ctrl+C
            except KeyboardInterrupt:
                break
