# 🐍 Snake Game with OpenCV + DroidCam

A fun, interactive Snake Game you control by moving a green object in front of your camera! This project leverages real-time computer vision via OpenCV to track a green color object, allowing you to guide the snake, eat apples, and grow your score. Play using your PC webcam or your phone camera via DroidCam.

---

## 🎮 Project Description

- **Real-Time Control:** Move a green object (e.g., cap, paper) to control the snake's direction.
- **Flexible Camera Input:** Use your computer's webcam or the DroidCam app to use your phone as an IP camera.
- **Game Mechanics:** The snake grows whenever the green object (snake head) touches the apple. The goal is to reach the maximum score.
- **Easy Controls:** Press `ENTER` to restart after a game over, and `Q` or `ESC` to quit the game.

---

## 🛠️ Tech Stack

- Python 3
- OpenCV (cv2)
- Imutils
- Numpy
- DroidCam (optional for phone camera input)

---

## ✨ Key Features

- **Real-Time Object Tracking:** Uses color detection to follow a green object as the snake's head.
- **Dynamic Snake Body:** Snake grows dynamically, following your movements.
- **Random Apple Generation:** Apples appear at random locations on the screen.
- **Score Counter:** Real-time score display and Game Over screen.
- **Flexible Input:** Supports both PC webcam and DroidCam IP stream for camera feed.

---

## ⚙️ Requirements

- Python 3.x
- opencv-python
- imutils
- numpy
- DroidCam (optional, for phone camera input)

---

## 🚀 Setup Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/snake-game-opencv-droidcam.git
   cd snake-game-opencv-droidcam
   ```

2. **Install dependencies:**
   ```bash
   pip install opencv-python imutils numpy
   ```

3. **(Optional) Using DroidCam:**
   - Download and install the [DroidCam app](https://www.dev47apps.com/) on your phone and PC.
   - Ensure both devices are connected to the same Wi-Fi network.
   - Start DroidCam on your phone and get the IP/PORT.
   - In `snake_game.py`, update the `IP` and `PORT` variables to match your device.

---

## 🕹️ How to Play

1. **Run the game:**
   ```bash
   python snake_game.py
   ```

2. **Show a green object** (like a green cap or pen) in front of your camera.
3. **Move the object** to control the snake’s direction.
4. **Eat apples** by moving the snake (green object) onto them. The snake grows and your score increases!
5. **Reach the max score** to win, or press `ENTER` to restart after game over.

---

## 🎯 Controls

- **ENTER** → Restart after Game Over
- **Q** or **ESC** → Quit the game

---

## 📸 Demo

| Gameplay Example |
|:----------------:|
| ![Snake Game Demo](./assets/snake_game_demo.gif) |

*Make sure to add your own screenshot or GIF in the `assets/` folder!*

---

## 🛠️ Troubleshooting

- **DroidCam Not Working?**
  - Ensure DroidCam is running on both your phone and computer.
  - Both phone and PC **must be on the same Wi-Fi/network**.
  - Double-check the `IP` and `PORT` values in the script.
- **Green Object Not Detected?**
  - Use a brightly colored, solid green object.
  - Adjust lighting to improve detection.
  - Tune HSV color range in the code if needed.

---

## 📦 License

This project is licensed under the [MIT License](LICENSE).

---

**Enjoy playing and feel free to contribute or report issues!**
