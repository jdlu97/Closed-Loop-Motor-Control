# Lab 02: Closed-Loop Control
 This repository contains the source code and documentation for Lab 2 of ME 405 (Mechatronics) course at California Polytechnic State University.
 
 In this laboratory exercise, we performed *closed-loop position control* on a DC motor using proportional control and code that interfaced the functionality of the controller, encoder, and motor drivers using cooperative multi-tasking. The code, as a whole, runs a closed-loop step response in which the setpoint (desired) value is changed in order to rotate the motor by about one revolution and stop it at the final position. 
 
 The "corrective" action of the controller to achieve one revolution is accomplished through a controller. The controller receives the error signal, calculated from the difference between the setpoint and measured encoder readings, and multiplied it by a proportional gain value to obtain the actuation signal in the form of a percent duty cycle to be sent to the motor.
 
 In our code, the user is initially prompted to enter a proportional gain value. This value is sent over serial 
to the STM32 Nucleo microcontroller and the step response is initiated. During the step response, the user interface task reads the data generated for later printing. In our trials, the motor takes less than a second to accomplish this task. Once the step response is finalized, the user task prints the data in the form of a plot.
 
 After running several tests and tuning our system with an appropriate proportional gains, we determined that gain values of 0.3 and 0.03 resulted in fast and accurate step response plots. This is shown below (**Figure 1-2**).
 
 ![Step response with Kp = 0.3](https://github.com/jdlu97/Lab-2/blob/main/src/response_Kp_0.3.png?raw=true)
 
 **Figure 1:** Motor step response with a proportional gain value of **Kp = 0.3**.
 
 ![Step response with Kp = 0.03](https://github.com/jdlu97/Lab-2/blob/main/src/response_Kp_0.03.png?raw=true)
 
 **Figure 2:** Motor step response with a proportional gain value of **Kp = 0.03**.
 
 As we can see from the plots, it takes less than one second for the response to approach steady state. For a gain value of 0.3, we can see some oscillation in the response as it settles at around 600 ms. In the second plot, a gain value 10 times smaller produces a faster response and no oscilation. For a gain value of 0.03, we can see that steady state is reached at around 400 ms.
 
 