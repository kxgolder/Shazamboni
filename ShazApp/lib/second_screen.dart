import 'package:flutter/material.dart';
import 'package:control_pad/control_pad.dart';

class SecondScreen extends StatelessWidget {
  const SecondScreen({Key? key}) : super(key: key);

  @override
  Widget build (BuildContext context) {
    double degrees = 1;
    double distance = 0;
    int battery = 69;
    int tankCapacity = 24;

    return Scaffold(
      backgroundColor: const Color.fromRGBO(214, 255, 250, 1),
      body: Container(
        padding: const EdgeInsets.fromLTRB(20, 25, 20, 5),
        child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Expanded(
              child:
              Image.asset('assets/images/fakeLiveStream.jpg'),
              flex: 6,
            ),
            Expanded(
              child:
                Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      Expanded(
                        child:
                        JoystickView(
                          onDirectionChanged: (double varDegrees, double varDistance)
                          {
                            degrees = varDegrees;
                            distance = varDistance;
                          },
                        ),
                        flex: 10,
                      ),
                      Expanded(
                        child:
                        TextButton(onPressed: () {}, child: const Text("Blade"), style: ButtonStyle(backgroundColor: MaterialStateProperty.all(const Color.fromRGBO(255, 255, 255, 1)))),
                        flex: 4,
                      ),
                      Expanded(
                        child:
                        TextButton(onPressed: () {}, child: const Text("Water"), style: ButtonStyle(backgroundColor: MaterialStateProperty.all(const Color.fromRGBO(255, 255, 255, 1)))),
                        flex: 4,
                      ),
                    ]
                ),
              flex: 4,
            ),
            TextButton(onPressed: () {}, child: const Text("On/Off"), style: ButtonStyle(backgroundColor: MaterialStateProperty.all(const Color.fromRGBO(255, 255, 255, 1)))),
            Text("Degrees: $degrees"),
            Text("Distance: $distance")
          ]
        )
      ),
    );
  }
}


