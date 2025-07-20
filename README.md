# Tattletale
Tattletale is a Python-based real-time application that helps users stay focused by detecting their eyes through the webcam. If the system detects that the user's eyes are not visible or may be distracted or not looking at the screen, a popup reminder appears to gently prompt them to refocus. Built as a group project, this tool combines computer vision, GUI design, and threading to create an interactive and practical productivity aid.

## Purpose
In a world full of distractions, Tattletale helps users stay on task by monitoring eye presence using a webcam. The goal is not just to track eye movement but to detect when someone has stopped paying attention and remind them to get back on track in real time.

## Features
-  Real-time iris and eye detection using Viola-Jones algorithm
-  Utilizes Haar Cascade Classifiers for detecting eye regions
-  GUI pop-ups using Tkinter for event-based messages
- Multithreading to maintain responsiveness
- Webcam-based live input using OpenCV

## Tech Stack
- Language: Python
- Libraries Used:
   - cv2 or OpenCV
      - Image processing and webcam input.
  - tkinter
    - GUI message display
  - threading
     -  real-time event handling
  - time
     - delay control for timed events

## How It Works
- The webcam captures frames continuously.
- Each frame is scanned for eye regions using a Haar Cascade Classifier trained to recognize eye features.
- If no eyes are detected for a set duration, the app triggers a Tkinter popup reminding the user to stay focused.
- A separate thread runs the popup so that it doesn't freeze the tracking loop.

## Eye Detection Logic (Explained Without Code)
The core of the system uses a Haar Cascade Classifier, a tool based on the Viola-Jones algorithm. It loads a pre-trained model from OpenCV's built-in library that is specifically designed to detect eyes. This classifier scans each frame for patterns that resemble eye-like features. If it doesn't find those features in a given frame, the system interprets it as a loss of focus and reacts by displaying a popup.
