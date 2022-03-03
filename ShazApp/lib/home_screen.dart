import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:untitled/second_screen.dart';

class FirstScreen extends StatelessWidget {
  const FirstScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color.fromRGBO(214, 255, 250, 1),
        body: Container(
            padding: const EdgeInsets.fromLTRB(20, 200, 20, 5),
            child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Expanded(
                      child: Column(children: [
                    Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: const [
                          Text("Shazamboni",
                              style:
                                  TextStyle(color: Colors.blue, fontSize: 50))
                        ]),
                    Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: const [
                          Text("The Backyard Ice Resurfacer",
                              style:
                                  TextStyle(color: Colors.blue, fontSize: 20))
                        ]),
                  ])),
                  Expanded(
                      child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: const [
                            Text("My Devices",
                                style: TextStyle(
                                    decoration: TextDecoration.underline)),
                          ],
                        ),
                        Container(
                            color: Colors.grey,
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                              children: [
                                const Text("Shazamboni",
                                    style: TextStyle(fontSize: 20)),
                                ElevatedButton(
                                    onPressed: () {
                                      Navigator.push(
                                          context,
                                          MaterialPageRoute(
                                              builder: (context) =>
                                                  const SecondScreen()));
                                    },
                                    child: const Text(
                                      "Start",
                                      style: TextStyle(fontSize: 20.0),
                                    ))
                              ],
                            ))
                      ]))
                ])));
  }
}

// TextButton(
// onPressed: () {
// Navigator.push(context, MaterialPageRoute(builder: (context) => const SecondScreen()));
// },
// child: const Text(
// "Start Shazamboni-ing",
// style: TextStyle(fontSize: 20.0),
// )
// )
