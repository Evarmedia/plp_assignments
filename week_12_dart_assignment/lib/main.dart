import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My App',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('My App'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text(
                'Welcome to my app!',
                style: TextStyle(fontSize: 24),
              ),
              const SizedBox(height: 20), // Add some space
              ElevatedButton(
                child: const Text('Click me!'),
                onPressed: () {
                  if (kDebugMode) {
                    print('Button clicked!');
                  }
                },
              ),
              const SizedBox(height: 20), // Add some space
          Image.network( //Displays an image from a provided URL.
            'https://tinyurl.com/bdfd544u',
          ),
            ],
          ),
        ),
      ),
    );
  }
}