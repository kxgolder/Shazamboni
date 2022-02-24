import 'package:flutter/material.dart';
import 'package:control_pad/control_pad.dart';

void main() {
  runApp(ExampleApp());
}

class ExampleApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Control Pad Example',
      home: HomePage(),
    );
  }
}

double varDegress = 0;
double varDistance = 0;

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(

        child: JoystickView(
          onDirectionChanged: (double degress, double distanceFromCenter) {
            varDegress = degress;
            varDistance = distanceFromCenter;
          },
        ),
      ),
    );
  }
}