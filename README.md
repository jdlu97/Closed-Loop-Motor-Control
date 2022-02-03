# Lab 02: Closed-Loop Control
 This repository contains the source code and documentation for Lab 2 of ME 405 (Mechatronics) course at California Polytechnic State University.
 
 In this laboratory exercise, we performed closed-loop position control on a DC motor using proportional control and code that interfaced the functionality of the controller, encoder, and motor drivers using cooperative multi-tasking. The code, as a whole, runs a closed-loop step response in which the setpoint (desired) value is changed in order to rotate the motor by about one revolution and stop it at the final position. 
 
 The "corrective" action of the controller to achieve one revolution is accomplished through a controller. The controller receives the error signal, calculated from the difference between the setpoint and measured encoder readings, and multiplied it by a proportional gain value to obtain the actuation signal in the form of a percent duty cycle to be sent to the motor.
 
 After running several tests and tuning our system with an appropriate proportional gain Kp, we determined that gain values of 0.3 and 0.03 resulted in fast and accurate step response plots. This is shown below.
 
