# ParkingSystem

In this mechatronic project, My team is required to develop a machine that has a specific function by integrates various sensors and actuation systems using Raspberry Pi microcontroller. For this project, we are integrating infrared sensor and servo motor. This code will show an available number of parking spot in real time and to control all the sequences involved.

The flow of work:
when the sensor detecting a car, it will trigger the servo motor to open the gate, and the counter will count down to indicate how many parking spot available. When the sensor detected a car coming out, it will trigger the servo motor to open, and the counter will counting up.

If you are using Raspberry Pi, please consider this first!
1. install WiringPi using " sudo pip3 install wiringpi "
2. Open Thonny IDE using sudo because the code will unable run is using /dev/gpiomem. Try " sudo thonny ".


Simulation Video:
[![Simulation Video](https://i.imgur.com/cTf6CoT.jpg)](https://youtu.be/ag3LEOfiki8?t=127 "Simulation Video")
