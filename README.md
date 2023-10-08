# Motion Detection Alarm System

## Overview

This project implements a simple motion detection alarm system using Python and OpenCV. The system captures video from a webcam, detects motion, and triggers an alarm if motion is detected.

## Features

- **Motion Detection:** Utilizes computer vision techniques to detect motion in the video stream.
- **Alarm System:** Sounds an alarm (beep) when motion is detected for a sustained period.
- **Toggle Mode:** Allows the user to toggle between normal and alarm modes using the 'f' key.
- **Quit Application:** Exits the application using the 'q' key.

## Requirements

- Python 3.x
- OpenCV
- Winsound (for Windows)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/unprricedlace/motion-detection-alarm.git
    cd motion-detection-alarm
    ```

2. Install the required dependencies:

    ```bash
    pip install opencv-python
    ```

    Note: For Windows, winsound is a built-in library, and no additional installation is needed.

## Usage

- Press 'f' to toggle between normal and alarm modes.
- Press 'q' to quit the application.

## Customization

You can customize the project by adjusting parameters in the code, such as the threshold for motion detection or the alarm duration.



