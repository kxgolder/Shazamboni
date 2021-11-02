// Copyright 2018 The Flutter team. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome to Flutter',
      home: FirstScreen(),
    );
  }
}

class FirstScreen extends StatelessWidget {
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
            "Next Page",
            style: TextStyle(fontSize: 20.0),
            )
    )
    )
    );
  }
}
