# Closed-Loop Motor Control
 
 Source code and documentation of firmware that shows closed-loop position control on a DC motor using proportional control and code that interfaces the functionality of an encoder driver, motor driver, and a controller using cooperative multi-tasking. Specifically, the source code as a whole runs a closed-loop step response in which the setpoint or desired value is one complete revolution of the motor. See details in the following sections.
 
 The encoder and motor driver base files were adapted from the [Drivers-for-Motor-Control](https://github.com/jdlu97/Drivers-for-Motor-Control) repository.
 
 ## Background
 
 DC motors with closed-loop control systems provide some of the fastest, most efficient, and most accurate systems available for moving things to specified positions. A motor with closed-loop control is often referred to as a servo system. If you have a motor, motor driver and position sensor just lying around, you can write code to operate the motor in closed-loop position servo mode. One algorithm is the proportional controller.

 - Supply as an input the setpoint, the desired location of the motor.
 - Subtract the measured location of the motor from the setpoint; the difference is the error signal, a signed number indicating which way the motor is off and how far.
 - Multiply the error signal by a control gain called KP to produce a result called the actuation signal. The larger the error, the larger the actuation, so the harder the controller will push.
 - Send the actuation signal to the motor driver which you have already written to control the magnitude and direction of motor torque.
	
 The controller can be enhanced, although this is case specific, by adding other terms based on the time integral and time derivative of the error, or even full state feedback using the position and velocity to compute the actuation, but those methods were not considered at this time due to the scope of the project.
 
 An often challenging task is tuning the controller. This involves adjusting operating parameters such as the proportional gain so that the controller pushes the motor hard enough to get the load to the correct place quickly and accurately, but not so hard as to cause excessive overshoot or instability. To assist with controller tuning, we often perform step response tests in which the setpoint is instantly changed from zero to some nonzero value and the response of the system is recorded. The response is usually plotted on a graph of motor position as a function of time.
 
 ## The Project

 Using code, a class that perform closed-loop controlled was developed. This controller provides the "corrective" action needed to achieve the desired step response, which, in this case, is one full revolution of the motor at a relatively quick time lapse. The controller determines the error signal, calculated from the difference between the setpoint and measured encoder readings, and multiplied it by a proportional gain value to obtain the actuation signal in the form of a percent duty cycle to be sent to the motor. All this takes place in the `run()` method. Additional methods like `setpoint()` and `set_gain()` simply receive and store the reference value and proportional gain, respectively, defined outside of the controller.
 
 By design, the code requires a user to interact with the program in order to set the proportional gain value. As such, part of the firmware design also included writing a user interface. This task is encapsulated in `task_user.py`.
 
 During program execution, the user is initially prompted to enter a proportional gain value. This value is sent over serial to the STM32 Nucleo microcontroller and the step response is initiated. During the step response, the user interface task stores the time and motor position data generated for later printing. Once the step response is finalized, the user task prints the data in the form of a plot.
 
 ## Testing and Results
 
 In the trials, after adjusting the controller gain value, the motor took less than a second to do one complete revolution. For clarification, a small disk with markings was mounted on the shaft of the motor to visually monitor the rotation of the motor.
 
 After running several tests and tuning the system with an appropriate proportional gains, gain values of 0.3 and 0.03 resulted in fast and fairly accurate step response plots. This is shown below:
 
 <p align="center">
    <img src="https://github.com/jdlu97/Closed-Loop-Motor-Control/blob/main/img/step_response_kp_0.3.png?raw=true" alt="Step response with Kp = 0.3"/>
 </p>
 
 <p align="center">Motor step response with a proportional gain value of <b>Kp = 0.3</b>.</p><br/>

 <p align="center">
    <img src="https://github.com/jdlu97/Closed-Loop-Motor-Control/blob/main/img/step_response_kp_0.03.png?raw=true" alt="Step response with Kp = 0.03"/>
 </p>
 
 <p align="center"> Motor step response with a proportional gain value of <b>Kp = 0.03</b>.</p>
 
 As we see from the plots, it takes less than one second for the response to approach steady state. For a gain value of 0.3, some oscillation in the response is observed as it settles at around 600 ms. In the second plot, a gain value 10 times smaller produces a faster response and no oscilation. For a gain value of 0.03, we can see that steady state is reached at around 400 ms.