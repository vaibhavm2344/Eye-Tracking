# Eye-Controlled Wheel Chair Movement Using Gaze Tracking

This project uses gaze detection to control motor movement. It detects eye directions (left, right, center) and blinking using the webcam, and then sends signals to an Arduino board to control a motor accordingly.

## 💡 Features

- Real-time eye tracking using webcam
- Detects gaze direction and blink
- Sends control signals to Arduino using pyFirmata
- Motors move in the desired direction (left, right, forward, stop)

## 🖥️ Technologies Used

- Python
- OpenCV
- GazeTracking Library
- pyFirmata
- Arduino Uno (or compatible)

## 🛠️ Hardware Required

- Arduino Uno
- Motor Driver (e.g., L298N)
- 2 DC motors
- Jumper wires
- Webcam

## ▶️ How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/vaibhavm2344/eye-controlled-wheelchair.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Upload Arduino StandardFirmata sketch (from Arduino IDE: **File > Examples > Firmata > StandardFirmata**) to your board.

4. Connect your hardware correctly (COM port, motor driver, etc.)

5. Run the project:
    ```bash
    python main.py
    ```

## ⚠️ Notes

- Update the `port` in `controller.py` to match your Arduino's COM port (e.g., `'COM8'`)
- Make sure your webcam is working

