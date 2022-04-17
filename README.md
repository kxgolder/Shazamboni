# Engineering Addendum

 ## Summary: Shazamboni and ShazApp

This GitHub details and features all the code for the project, backyard Zamboni or Shazamboni, a device and smartphone application. The main project features a remote-controlled ice surfacer that efficiently scrapes the ice of a backyard ice rink without requiring significant labor. The Shaz App controls the Shazamboni device. Katharina Golder, Bryan Jaimes, Robert Ling, & Yanni Pang, members of team 10, started and maintained this project. We created this GitHub repository for the course EC463/464 ECE Senior Design at Boston University.This specific Readme will outline the general information of the project, technologies we used, setup, our gotchas of this project,  types of things to look out for, and finally the current state of the project. 

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Gotchas](#gotchas)
* [Nota Bene](#nota-bene)
* [Current State](#current-state)
* [Acknowledgements](#acknowledgements)

## General Info

This repository includes the code for the Shaz App and the motor/sensor controls. It also features the past attempts we have made in updating and reconfiguring our code to work with our final product. LIST HERE THE CODE WE CURRENTLY USE.

**Other Readme files:** Hardware and Software reports are filed under README_HARDWARE.md and README_SOFTWARE.md list more complete information about all the aspects of our project

**Previous Reports:** These include our User’s Manual, Test Plans, and Test Reports.

**Past Code:** ultrasonic_distance.py and its variants are our atttempts at working on integrating the HC-SR04 ultrasonic sensors with our DC motors and Shaz App. l298n_dc.py controls the L298N motor driver and also are our atttempts at working on integrating the motor driver with the DC motors and Shaz App. Other files such as motor.py, robot.py, sender.py and so on are the final attempts of integrating all the pieces with Ad-Hoc networking, video streaming, and of course the motors and ultrasonic sensors.

## Technologies

We created this project with Flutter and Dart language, python scripts, websockets and an mjpg-streamer.  

The Shaz App uses Flutter for controlling the Shazamboni. The Flutter Framework is a software development kit created by Google to help users develop UI software to create mobile applications. The programming language used to utilize Flutter Framework is Dart. Dart is a typed object-oriented language. 

Python Scripts as we mentioned earlier make up the bulk of the actual command executions. Most of the commands use python as we found python the easiest language for writing the commands.

Through the WiFi ad hoc network connection, the Raspberry Pi and the cross-platform application use websockets to communicate. Socket communication is used to send JSON packets containing information about the user’s movements from the joystick. These packets are decoded on the Raspberry Pi and are used to drive the two motors present on the vehicle.

The camera live stream uses mjpg-streamer on the Raspberry Pi along with the ArduCam camera module.

## Setup

For normal operation, the user will do the following:

1. The user will use the ShazApp to login and communicate with the Shazamboni

2. The user will use the joystick controls to pilot the Shazamboni to clean the ice

3. If the user encounters a wall, the user should be able to back up after a period of five seconds has elapsed.

The user will have access to the livestream and joystick controls when logged in.

## Gotchas

We spent time figuring out which components we could use. We figured that ultrasonic sensors would work fine enough. We figured that using an ad hoc network would work best for the Shazamboni as it would solve the problem of Wi-Fi connectivity issues with the ShazApp and Shazamboni. Websockets would seemlessly send messages to the Shazamboni from the user's phone. Mjpg-streamers would work well with the camera we set up, seemlessly streaming video feed.

## Nota Bene

During testing with the ultrasonic sensors, we encountered some problems such as late detecting and non-detection of complex objects. We advise people in the future to use LIDAR for better detection of objects. While we were successful in implementing an ad hoc network for our device and app, we found the task difficult in implementing. We advise thus to follow the reference featured in the Hardware Report by the letter for successful implementation of ad hoc networking. ASK TEAM FOR PROBLEMS THEY ENCOUNTERED.

## Current State

We have successfully completed all testing requirements and are in the process of installing the finishing touches and integrations with the ME team for our client. The Shazamboni and Shaz App work well together. ASK TEAM FOR THE CURRENT STATUS.

## Acknowledgements
We express thanks to all the staff and TAs in the ECE and ME department, as well as our client. We personally thank professors Alan Pisano, Michael Hirsh, Osama Alshaykh, and William Hauser as well as our graduate senior member Shashwath Bharadwaj for their continued support and guidance. We also thank all the sources we used for developing this project. We thank Marianna Natale, Mei Singer, and Beau Walsh for their work on the ME team portion of the project. Finally, we thank our client, Alan D. Pisano Jr. for reaching out to us and supporting us throughout the project!

Katharina Golder, Bryan Jaimes, Robert Ling, and Yanni Pang make the ECE team of Team 10 Shazamboni. Katharina and Robert are the electrical engineers, and Bryan and Yanni are the computer engineers on the team. In addition to the ECE team, there is also a mechanical engineering team working on the Shazamboni: Marianna Natale, Mei Singer, and Beau Walsh.
