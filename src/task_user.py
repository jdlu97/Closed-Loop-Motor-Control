'''!    @file       task_user.py
        @brief      Implements a user interface for Lab 02.
        @details    The user interface runs on the PC and sends the proportional
                    gain value to the STM32 Nucleo microcontroller to initiate
                    the step response. Once the step response is finished, this
                    script reads and plots the resulting data, saving the 
                    current plot as a PNG image file.
        @author     Juan Luna
        @author     Marcus Monroe
        @author     Cade Liberty
        @date       January 30, 2022
'''
import serial
import matplotlib.pyplot as plt
import time

## String variable holding the name of the serial port 
COM_num = "COM5"       
        
def send(command):
    '''!    @brief  Sends the proportional gain value over serial.
    '''
    port.write((command+"\r\n").encode('utf-8'))
        
def read():
    '''!    @brief  Reads data from the serial port sent by the Nucleo.
    '''
    data = port.readline().decode('utf-8')
                
if __name__ == '__main__':
    ## Boolean variable for triggering plotting of the data.
    print_flag = False
    ## Boolean variable that tells program whether Kp is already sent over serial.
    Kp_flag = False
    ## List of time stamps for each encoder reading value.
    time_list = []
    ## List of encoder position values in step response.
    position = []

    with serial.Serial(str(COM_num), 115200) as port:
    
        while True:
            # The following code always runs at startup when the code is run.
            if print_flag == False:
                # User is asked to enter proportional gain value.
                if Kp_flag == False:
                    print('Please, enter a Kp value: ')
                    send(input())
                    Kp_flag = True
                    start_time = time.time()
                # When the Kp value was already given, the following code reads
                # from the serial port.
                else:

                    try:
                        data = port.readline().decode('utf-8')
                        current_data = [idx for idx in data.replace('r\n', '').split(',')]
                        # Append data read from the serial port to lists 
                        time_list.append(float(current_data[0]))
                        position.append(float(current_data[1]))
                    except:
                        pass
                    
                    # Print variable flag is raised when the step response is over.
                    if (time.time() - start_time) > 2:
                        print_flag = True
                
            elif print_flag == True:
                print('Printing plot...\nAn image will be saved.')
                time_list.pop(-1)
                # Printing plot code
                fig, ax = plt.subplots()

                # Scatter plot of time and position data.
                ax.scatter(time_list, position)

                # Plot labels: title, x-label, and y-label
                ax.set_title("Response Plot")
                ax.set_xlabel("Time, ms")
                ax.set_ylabel("Position, ticks")
                    
                # Display the figure
                plt.show()
                # Save a copy of the figure
                plt.savefig("step_response.png")
                # Clear flag
                print_flag = False