# Human-Following-Robot
A Raspberry Pi-based 2-wheeled mobile robot that detects and follows a human face using OpenCV Haarcascade. The robot adjusts its direction and speed based on face position, built on a custom-designed chassis in Fusion 360.

How to Run

1.Clone this repository:
		
  	git clone https://github.com//Human-Following-Robot.git

2.Connect your camera, motors, and hardware.

Raspberry Pi to L298N Motor Driver:
| Raspberry Pi GPIO Pin  | L298N Pin | Function             |
| ---------------------- | --------- | -------------------- |
| GPIO17 (Pin 11)        | IN1       | Left Motor Forward   |
| GPIO18 (Pin 12)        | IN2       | Left Motor Backward  |
| GPIO22 (Pin 15)        | IN3       | Right Motor Forward  |
| GPIO23 (Pin 16)        | IN4       | Right Motor Backward |
| GND (Pin 6 or any GND) | GND       | Common Ground        |

Motors to L298N:
| L298N Output | Connect To     |
| ------------ | -------------- |
| OUT1 & OUT2  | Left DC Motor  |
| OUT3 & OUT4  | Right DC Motor |

Camera:

USB Webcam: Plug into Raspberry Pi USB port (or use the Pi Camera Module via the CSI port if you're using that instead)




3.Run the Python script on Raspberry Pi
      
	python3 human_following_robot.py

	

## 3D Design Files

All 3D CAD files related to the project are located in the `3D_designs` folder.  

Formats included: Fusion 360 `.f3d`.

Feel free to download and use them for 3D printing or further modifications.


## Hardware Used

1.Raspberry Pi 

2.L298N Motor Driver

3.2-Wheel Mobile Robot Chassis (Fusion 360 designed)

4.USB Camera or Pi Camera

5.12V DC Motors & Battery Pack

6.Jumper wires, Breadboard




## Features

1.Face detection using Haar Cascade.

2.Real-time human following behavior.

3.Motor control via L298N driver.

4.Commands sent from Raspberry Pi to Arduino Uno through serial communication.

5.2-Wheeled self-balanced mobile robot chassis

6.Designed and modeled in Fusion 360.


## License

This project is licensed under the MIT License - feel free to use, modify, and share!
