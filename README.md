# Shazamboni and ShazApp

 ## Summary

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

We spent time figuring out which components we could use. We figured that ultrasonic sensors would work fine enough but during testing we encountered some problems such as late detecting and non-detection of complex objects. We figured that using an ad hoc network would work best for the Shazamboni as it would solve the problem of Wi-Fi connectivity issues with the ShazApp and Shazamboni. Websockets would seemlessly send messages to the Shazamboni from the user's phone. Mjpg-streamers would work well with the camera we set up, seemlessly streaming video feed.

## Nota Bene

## Current State

## Acknowledgements
App code is in: websockets_app
Car controller is in: shaz_team
