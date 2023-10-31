# Gesture-Based VLC Media Controller

**Authors:** Eesh Gharat, Kingshuk Mitra

This project is a gesture-based VLC media controller that allows you to control VLC media player using hand gestures detected by a camera. It provides an interactive and innovative way to play, pause, adjust volume, and perform various media control actions using your hand movements.

## Features

- Play and pause media playback.
- Fast forward and rewind in media playback.
- Toggle full-screen mode.
- Adjust system volume.
- Mute the system.
- Control screen brightness.

## Requirements

- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI
- Screen Brightness Control (sbc)
- VLC Media Player


## Usage

1. **Install Required Dependencies:**

   Ensure you have the necessary Python libraries installed using pip:

   ```bash
   pip install opencv-python mediapipe pyautogui screen-brightness-control
   ```

2. **Install VLC Media Player:**

   If you haven't already, make sure to install VLC Media Player on your system. You can download it from the official VLC website: [VLC Download](https://www.videolan.org/vlc/download.html).

3. **Clone the Repository:**

   Clone this repository to your local machine using git:

   ```bash
   git clone https://github.com/IshGharat/BASAN-T.git
   cd BASAN-T
   ```

4. **Run the Gesture-Based VLC Media Controller:**

   Execute the `Basan-T.py` script to start the gesture-based media controller:

   ```bash
   python Basan-T.py
   ```

5. **Use Hand Gestures:**

   Follow the instructions commented in code to control VLC media player using hand gestures. The controller recognizes specific gestures to perform actions like play/pause, fast forward, rewind, full-screen mode, volume adjustment, muting, and screen brightness control.


## Gestures

- To play or pause, make a 'yo' sign using right hand (Right thumb,index and pinky).
- To fast forward, make a thumbs up using right hand and point thumb towards right (Right thumb towards right).
- To rewind, make a fist using your right hand and point only index finger towards left (Right index towards left).
- To enter full-screen mode, make a fist using your left hand and point only index and pinky finger towards top (Left index and pinky).
- To adjust volume, pinch your right thumb and index finger (Touch middle finger to index to activate).
- To mute, use a specific gesture (make a fist with your left hand).
- To adjust screen brightness, pinch your left thumb and index finger (Touch middle finger to index to activate).

## Acknowledgments

This project was developed by Eesh Gharat and Kingshuk Mitra as part of Semester 4 Software Engineering Project under the guidance of Prof. Ruchi Sharma, Mukesh Patel School of Technology Management & Engineering (Mumbai), NMIMS.

## License

This project is licensed under the MIT License. See the [MIT LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to contact us at:

- Eesh Gharat - [eesh.gharat126@nmims.edu.in](eesh.gharat126@nmims.edu.in)
- Kingshuk Mitra - [kingshuk.mitra081@nmims.edu.in](mailto:kingshuk.mitra081@nmims.edu.in)

