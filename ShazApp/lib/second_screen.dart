import 'package:flutter/material.dart';
import 'package:control_pad/control_pad.dart';
import 'package:untitled/main.dart';
import 'dart:io';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:web_socket_channel/status.dart' as status;
import 'home_screen.dart';
import 'package:flutter_vlc_player/flutter_vlc_player.dart';
//import 'package:flutter_vlc_player/vlc_player_controller.dart';
import 'package:flutter_mjpeg/flutter_mjpeg.dart';

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
    String ip_add = "10.0.6.1";

    // VlcPlayerController _vlcViewController = VlcPlayerController.network(
    //   'http://10.0.4.150:8080/?action=stream',
    //   hwAcc: HwAcc.FULL,
    //   autoPlay: true,
    //   options: VlcPlayerOptions(),
    // );
    final channel = WebSocketChannel.connect(
      Uri.parse("ws://${ip_add}:8001/"),
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
                  Mjpeg(
                    isLive: true,
                    error: (context, error, stack) {
                      print(error);
                      print(stack);
                      return Text(error.toString(), style: TextStyle(color: Colors.red));
                    },
                    stream:
                    'http://${ip_add}:8080/?action=stream', //'http://192.168.1.37:8081',
                  ),
                  // VlcPlayer(
                  //   controller: _vlcViewController,
                  //   aspectRatio: 2.1,
                  //   placeholder: Center(child: CircularProgressIndicator()),
                  // ),
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
