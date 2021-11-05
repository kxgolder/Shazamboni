import 'package:flutter/material.dart';

void main() {
  runApp(
    new MaterialApp(
      home: new WaterButton()
    )
  );
}

class WaterButton extends StatefulWidget {
  @override
  WaterButtonState createState() => new WaterButtonState();
}

class WaterButtonState extends State<WaterButton> {

  String message = "";
  void onPressed() {
    setState(() {
      message = "Water Button Pressed!";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: new AppBar(title: Text("Shazamboni"), backgroundColor: Colors.lightBlue,),
        body: new Container(
          child: new Center(
            child: new Column(
            mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                new Text(message),
                new RaisedButton(
                child: new Text("Water"),
                color: Colors.blue,
                onPressed: onPressed
                )
           ]
         )
        )
      )
    );
  }
}
