import 'package:flutter/material.dart';

class SecondScreen extends StatelessWidget {
  const SecondScreen({Key? key}) : super(key: key);

  @override
  Widget build (BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Shazamboni"),
        ),
        body: Center(
            child: TextButton(
                onPressed: () {},
                child: const Text(
                  "Hellofvndjfnvkd",
                  style: TextStyle(fontSize: 20.0),
                )
            )
        )
    );
  }
}