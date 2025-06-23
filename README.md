# Hour Tower - Clock Learning Game 🕐✨

**Hour Tower** is an interactive and educational game built with Python Tkinter, designed to help children ages 4-8 learn to tell time in a fun and engaging way. 
---

## 🎮 Game Features

### Core Gameplay: Number Placement

The primary objective is for children to **drag and drop** numbers 1-12 onto their correct positions on a large analog clock face.

* **Interactive Clock:** A vibrant 400x400 analog clock with 12 empty circular positions.
* **Draggable Numbers:** Numbers 1-12 float randomly in colorful neon circles, ready to be placed.
* **Instant Feedback:**
    * **Correct Placement:** The number "snaps" into place, the score increases, and progress is made on the tower.
    * **Incorrect Placement:** The clock hands gently wiggle, an error message appears, and the number bounces back.
* **Sound Effects:** Engaging chimes for correct answers and subtle sounds for incorrect attempts provide immediate audio feedback.

### The Clock Tower Building System

As children correctly place numbers, they contribute to building a **neon-lit clock tower**.

* **Visual Progress:** A dedicated area shows the tower's construction.
* **Block by Block:** Each set of 12 correct answers completes a tower "block."
* **Grand Finale:** Once all blocks are complete, the tower transforms into a magnificent clock tower, topped with a bell!

---

## 🏗️ Modular Component Architecture

**Hour Tower** is built with a modular component architecture.

### 📁 Project Structure
hour-tower/
    ├── components/
    │   ├── __init__.py         # Package initialization
    │   ├── colors.py           # Neon color palette
    │   ├── clock_number.py     # Draggable number component
    │   ├── clock_face.py       # Main clock face with positions
    │   ├── tower.py            # Clock tower building system
    │   ├── ui.py               # UI components (buttons, title, score)
    ├── sound.py                # Sound effects management
    ├── game_logic.py           # Game state and logic management
    ├── main.py                 # Main application orchestrator
    └── README.md               # This file
### 🔧 Key Components

Each component handles a specific aspect of the game, promoting code reusability and clarity:

* **`colors.py`**: Manages the centralized neon color palette.
* **`sound.py`**: Controls sound effects.
* **`clock_number.py`**: Defines draggable number behavior.
* **`clock_face.py`**: Manages the main clock display.
* **`tower.py`**: Implements the tower building system.
* **`ui.py`**: Contains all user interface elements.
* **`game_logic.py`**: Oversees game state and core logic.
* **`main.py`**: The central application orchestrator.

---

## 🚀 Installation & Running

### Prerequisites

* Python 3.7 or higher
* Tkinter (typically included with Python installations)

### Running the Game

1.  **Navigate** to the `hour-tower` project directory:
    ```bash
    cd hour-tower
    ```
2.  **Run** the main application:
    ```bash
    python main.py
    ```

**Note:** Ensure all component files are located in the `components/` directory.

---

## 🎯 How to Play

The goal is simple: **place all numbers 1-12 in their correct positions around the clock!**

1.  **Click and drag** the colorful neon numbers.
2.  **Drop them** into the corresponding circular positions on the clock face.
3.  **Score 10 points** for each correct placement.
4.  Watch your **clock tower grow** with every successful set of 12 numbers!

### Controls

* **Reset Game:** Start a new game.
* **Sound Toggle:** Turn sound effects on or off.

---

## 🔧 Technical Features

* **Modular & Extensible:** Designed for easy addition of new levels and features.
* **Smooth Animations:** Engaging visual feedback with wiggling clock hands, bouncing numbers, and glow effects.
* **Robust Event Handling:** Seamless mouse interaction and drag-and-drop functionality.
* **Child-Friendly Error Handling:** Provides clear, gentle feedback for incorrect actions.
* **Responsive Design:** Adapts gracefully to different window sizes.
* **Accessibility Minded:** Features large, easy-to-click buttons for small hands.

---

## 🐛 Troubleshooting

### Common Issues

1.  **Import Errors:** Verify that all component files are correctly placed within the `components/` directory.
2.  **Font Issues:** If the "Permanent Marker" font is unavailable, the game will fall back to bold Arial.
3.  **Sound Issues:** Current sound effects are simulated through print statements; no external audio files are required.

---

## 🎉 Future Enhancements

The modular architecture paves the way for exciting future developments:

* Additional game levels (e.g., telling time, digital clock challenges).
* More complex animations and visual effects.
* Full integration of actual audio files.
* Save/load game progress functionality.
* Multiple difficulty levels.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
