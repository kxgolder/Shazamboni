import 'package:flutter/material.dart';
import 'package:control_pad/control_pad.dart';
import 'package:untitled/main.dart';
import 'dart:io';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:web_socket_channel/status.dart' as status;
import 'home_screen.dart';

class ControlScreen extends StatefulWidget {
  @override
  createState() => _SecondScreenState();
}

class _SecondScreenState extends State<ControlScreen> {

  @override
  Widget build(BuildContext context) {
    double degrees = 0;
    double distance = 0;
    int battery = 69;
    int tankCapacity = 24;
    final channel = WebSocketChannel.connect(
      Uri.parse("ws://10.0.4.61:8001/"),
    );
    channel.stream.listen((message) {
    });
    //Connect standard in to the socket

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
                            onDirectionChanged: (double varDegrees,
                                double varDistance) {
                                degrees = double.parse((varDegrees).toStringAsFixed(2));
                                distance = double.parse((varDistance).toStringAsFixed(2));
                                var packet = "{\"degrees\": $degrees, \"distance\": $distance}";
                                print(packet);
                                channel.sink.add(packet);
                            },
                          ),
                          flex: 10,
                        ),
                        Expanded(
                          child:
                          TextButton(onPressed: () {},
                              child: const Text("Blade"),
                              style: ButtonStyle(
                                  backgroundColor: MaterialStateProperty.all(
                                      const Color.fromRGBO(255, 255, 255, 1)))),
                          flex: 4,
                        ),
                        Expanded(
                          child:
                          TextButton(onPressed: () {},
                              child: const Text("Water"),
                              style: ButtonStyle(
                                  backgroundColor: MaterialStateProperty.all(
                                      const Color.fromRGBO(255, 255, 255, 1)))),
                          flex: 4,
                        ),
                      ]
                  ),
                  flex: 4,
                ),
                TextButton(onPressed: () {
                  Navigator.push(context, MaterialPageRoute(
                      builder: (context) => const FirstScreen()));
                },
                    child: const Text("On/Off"),
                    style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all(
                            const Color.fromRGBO(255, 255, 255, 1)))),
              ]
          )
      ),
    );
  }
}
