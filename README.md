# Hour Tower - Clock Learning Game

An educational clock learning game for children ages 4-8, built with Python Tkinter using a modular component architecture inspired by React.

## 🎨 Visual Design - Lite-Brite Aesthetic

- **Deep black background** (#000000) for the entire application
- **Bright neon colors** that "glow" against the black background:
  - Electric blue (#00FFFF), hot pink (#FF1493), lime green (#32CD32)
  - Bright yellow (#FFFF00), orange (#FF4500), purple (#8A2BE2)
- **Permanent Marker font** throughout (fallback to bold Arial)
- **Visual glow effects** using border highlights and bright colors
- **Bright white text** (#FFFFFF) or neon colors for maximum contrast

## 🏗️ Modular Component Architecture

The application is structured into modular components, similar to React components:

### 📁 Component Structure

```
hour-tower/
├── components/
│   ├── __init__.py          # Package initialization
│   ├── colors.py            # Neon color palette
│   ├── sound.py             # Sound effects management
│   ├── clock_number.py      # Draggable number component
│   ├── clock_face.py        # Main clock face with positions
│   ├── tower.py             # Clock tower building system
│   ├── ui.py                # UI components (buttons, title, score)
│   └── game_logic.py        # Game state and logic management
├── main.py                  # Main application orchestrator
└── README.md               # This file
```

### 🔧 Component Details

#### `colors.py` - Neon Color Palette
- Centralized color management
- Neon color palette with Lite-Brite aesthetic
- Utility methods for color selection

#### `sound.py` - Sound Effects
- Sound effect management
- Toggle functionality for audio
- Placeholder for future audio implementation

#### `clock_number.py` - Draggable Numbers
- Individual draggable number components
- Glow effects and visual feedback
- Drag-and-drop functionality

#### `clock_face.py` - Clock Face
- Main clock display with positions
- Number placement validation
- Clock hands animation (wiggling)

#### `tower.py` - Clock Tower
- Tower building system
- Progress tracking
- Block construction with bell

#### `ui.py` - User Interface Components
- Neon-styled buttons
- Game title with glow effects
- Score display
- Message display system

#### `game_logic.py` - Game Logic
- Game state management
- Number generation and placement
- Score tracking
- Victory conditions

#### `main.py` - Application Orchestrator
- Main application class
- Component initialization
- Event handling
- Game loop management

## 🎮 Game Features

### Current Level - Number Placement
- **Large analog clock face** (400x400) with bright white/neon outline
- **12 empty circular positions** marked around the clock
- **Numbers 1-12** floating randomly in colorful neon circles
- **Drag-and-drop functionality** for placing numbers in correct positions

### Game Mechanics
- ✅ **Correct placement**: Number disappears, appears on clock, score increases
- ✅ **Incorrect placement**: Clock hands wiggle, error message, number bounces back
- ✅ **Score tracking**: Points awarded for correct placements
- ✅ **Tower building**: Progress toward building clock tower blocks
- ✅ **Sound effects**: Success chimes and gentle error sounds
- ✅ **Visual feedback**: Glow effects, animations, and encouraging messages

### Clock Tower Building System
- Visual tower building area showing progress
- Each correct answer adds progress toward completing a "block"
- Tower becomes a clock tower with a bell at the top
- Neon colors for tower construction with glow effects

## 🚀 Installation & Running

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually included with Python)

### Running the Game
```bash
# Navigate to the project directory
cd hour-tower

# Run the main application
python main.py
```

### File Structure Requirements
Make sure all component files are in the `components/` directory and the main application file is in the root directory.

## 🎯 Game Instructions

1. **Objective**: Place all numbers 1-12 in their correct positions around the clock
2. **How to Play**: 
   - Click and drag numbers from their floating positions
   - Drop them in the correct circular positions around the clock
   - Correct placements will disappear and appear on the clock
   - Incorrect placements will bounce back with visual feedback
3. **Scoring**: 10 points for each correct number placement
4. **Tower Building**: Each set of 12 correct answers builds a tower block
5. **Controls**:
   - **Reset Game**: Start over with new random number positions
   - **Sound Toggle**: Turn sound effects on/off

## 🔧 Technical Features

- **Modular Architecture**: Easy to extend with new levels and features
- **Smooth Animations**: Clock hand wiggling, number bouncing, glow effects
- **Event Handling**: Proper mouse interaction and drag-and-drop
- **Error Handling**: Child-friendly feedback and error recovery
- **Responsive Design**: Adapts to different window sizes
- **Accessibility**: Large buttons designed for small fingers

## 🎨 Customization

### Adding New Colors
Edit `components/colors.py` to add new neon colors to the palette.

### Adding New Sound Effects
Extend `components/sound.py` to include additional audio feedback.

### Creating New Game Levels
The modular structure makes it easy to add new levels by extending the game logic in `components/game_logic.py`.

### Modifying Visual Effects
Each component can be independently modified to change visual effects, animations, or styling.

## 🐛 Troubleshooting

### Common Issues
1. **Import Errors**: Ensure all component files are in the `components/` directory
2. **Font Issues**: If "Permanent Marker" font is unavailable, the app will fall back to bold Arial
3. **Sound Issues**: Sound effects are currently simulated (print statements) - no actual audio files required

### Error Reporting
The application includes comprehensive error handling and will display user-friendly error messages if something goes wrong.

## 🎉 Future Enhancements

The modular architecture makes it easy to add:
- Additional game levels (telling time, digital clocks, etc.)
- More complex animations and visual effects
- Actual audio file integration
- Save/load game progress
- Multiple difficulty levels
- Multiplayer features

## 📝 License

This project is open source and available under the MIT License.

---

**Hour Tower** - Making clock learning fun and engaging for children! 🕐✨ 