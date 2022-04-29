# Software Report

## Summary

This is a documentation that describes how all of our software works. The markdown file details Shazamboni and Shaz App use the code we wrote as well as how each script depends on or works with each other. It features an overview of each software module, flow charts of the code, dev/build tool information and finally how to install the product from scratch.

## Table of Contents

* [Overview of Each Software Module](#overview-of-each-software-module)
* [Flow Charts](#flow-charts)
* [Dev and Build Tool Information](#dev-and-build-tool-information)
* [Installation from Scratch](#installation-from-scratch)

## Overview of Each Software Module

Our project uses a cross-platform mobile application and a controller python script that runs on our Raspberry Pi 4B. We made the application using Flutter, which uses the Dart programming language. The main program, **main.dart**, initializes the app which contains the home screen, **home_screen.dart** , where the user can tap on “Start” to get to the controller screen, **second_screen.dart**. The controller screen contains a virtual joystick and a live video stream of the camera on the Shazamboni. 

When the user opens the controller page, the program creates a web socket channel that connects to and communicates with the socket running on the Raspberry Pi 4B. The Shazamboni houses the Pi in a “black box. The app listens for any packets sent by the Pi that indicate the ultrasonic sensors have detected an obstacle.  When the user moves the joystick on the controller screen, a JSON packet containing degrees and distance values gets sent to the Pi, unless an obstacle is detected. The controller python , **controller,py**, uses these sent values, creates a websocket based on the sent values, and finally controls the motors on the Shazamboni. 

## Flow Charts

![Overall Flow Chart](https://user-images.githubusercontent.com/82286857/166062249-edcc6353-cb81-4313-8180-a1ced2b73083.jpeg)


*Figure 1. The system overview diagram of the Shazamboni. The blocks shaded in blue are the software components, and the blocks shaded in orange are the hardware components of the system.*

![Software Code Flow Chart](https://user-images.githubusercontent.com/82286857/166061958-175dbc2e-eeb2-4764-9a0d-2a966ae04983.jpeg)

*Figure 2. Ditto, with a focus on the software components overall.*

![Software Code Flow Chart With Code](https://user-images.githubusercontent.com/82286857/166061844-7120dfae-7ec8-495d-b934-1534567cd084.jpeg)

*Figure 3. Ditto, with the specific code and function for each software module.*

## Dev and Build Tool Information

**Shaz App and the python scripts for the Shazamboni use the following builds below:**

* *Flutter SDK >= 2.12.0 < 3.0/.0 using several plug-ins: Flutter_mjpeg 2.0.1, control_pad 1.1.1, web_socket_channel 2.1.0*

* *Python 3.10 for the running the python scripts*

## Installation from Scratch

To install the ShazApp component of our project software stack from scratch, open an IDE or integrated development environment compatible with Flutter (i.e. IntelliJ) and clone the project from our github repository,  https://github.com/kxgolder/Shazamboni. Then, connect your phone to the computer and run the app on the smartphone. After a few seconds, the app should start on your phone. To connect the phone to the Shazamboni, connect to the Shazamboni network. To start the controller script on the Pi, ssh or secure shell network into the Pi using SSH pi@10.0.6.1. Then, go into the Shazamboni folder (*cd Shazamboni*) and run the script (*python3 controller.py*). The app is now connected to the Shazamboni, and ready to resurface your ice! 

**The steps are abbreviated below:**

1. Open an IDE on your computer, like terminal

2. On the same IDE as in step 1, type and run ***git clone  https://github.com/kxgolder/Shazamboni***

3. Connect phone to your computer and run the app

4. Wait a few seconds

5. Connect to network titled **Shazamboni** via phone

6. On the same IDE as in step 1 and 2, type and start the controller script on the Pi via ssh with ***SSH pi@10.0.6.1.***

7. On the same IDE as in step 1, 2, and 6, type and run ***cd Shazamboni***

8. On the same IDE as in step 1, 2, 6, and 7, type and run ***python3 controller.py***

9. Get ready to resurface your ice!

