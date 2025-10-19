# 🎮 Rock Paper Scissors Game

A collection of stylish and modern Rock Paper Scissors games built with Python and Tkinter, featuring beautiful UI designs and smooth animations.

## 🌟 Features

- **Two Unique Designs**: Choose between Neon Cyberpunk and Modern Gradient themes
- **5-Round Tournament**: Complete gameplay with score tracking
- **Smooth Animations**: Engaging visual effects and transitions
- **Interactive UI**: Hover effects and responsive buttons
- **Real-time Scoring**: Live score updates and round tracking
- **Game Over Screen**: Final results with play again option

## 🎨 Game Versions

### 1. Neon Cyberpunk Version (`rock_paper_scissors.py`)

- **Theme**: Dark cyberpunk with neon colors
- **Colors**: Electric blue, hot pink, neon green, bright yellow
- **Effects**:
  - Animated title with cycling rainbow colors
  - Pulsing VS label
  - Glowing button borders
  - Gradient background layers
  - Rainbow reset button animation

### 2. Modern Gradient Version (`modern_rock_paper_scissors.py`)

- **Theme**: Clean modern design with gradients
- **Colors**: Purple-blue gradients (#667eea to #764ba2)
- **Effects**:
  - Smooth gradient backgrounds
  - Clean white container design
  - Hover effects on buttons
  - Battle area with pink gradient
  - Game over screen with orange gradient

## 🚀 How to Run

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually comes with Python)
- PIL (Pillow) for the modern version

### Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install required dependencies (if needed):

   ```bash
   pip install pillow
   ```

### Running the Games

**Neon Cyberpunk Version:**

```bash
python rock_paper_scissors.py
```

**Modern Gradient Version:**

```bash
python modern_rock_paper_scissors.py
```

## 🎯 How to Play

1. **Start the Game**: Run either version of the game
2. **Choose Your Weapon**: Click on Rock (🪨), Paper (📄), or Scissors (✂️)
3. **Battle**: Watch the animated battle sequence
4. **Score Tracking**: See your score update in real-time
5. **Complete 5 Rounds**: Play through all 5 rounds
6. **Final Results**: View the winner and final scores
7. **Play Again**: Click "Play Again" or "New Game" to restart

## 🎮 Game Rules

- **Rock** beats **Scissors** ✂️
- **Scissors** beats **Paper** 📄
- **Paper** beats **Rock** 🪨
- Same choices result in a **Tie** 🤝

## 🖼️ Screenshots

### Neon Cyberpunk Version

- Dark theme with electric neon colors
- Animated glowing effects
- Cyberpunk aesthetic with space-like background

### Modern Gradient Version

- Clean, professional design
- Beautiful gradient backgrounds
- Smooth hover animations
- Modern typography

## 🛠️ Technical Details

### Built With

- **Python 3.x**
- **Tkinter** - GUI framework
- **PIL (Pillow)** - Image processing (modern version)
- **Random** - Computer choice generation

### Key Components

- **Game Logic**: Standard Rock Paper Scissors rules
- **UI Framework**: Custom Tkinter styling
- **Animation System**: Timer-based color cycling and effects
- **State Management**: Round tracking and score management

## 📁 Project Structure

```text
Rock_Paper_Scissors_game/
│
├── rock_paper_scissors.py          # Neon cyberpunk version
├── modern_rock_paper_scissors.py   # Modern gradient version
└── README.md                       # This file
```

## 🎨 Customization

### Colors

Both versions use customizable color schemes defined in the `colors` dictionary. You can easily modify:
- Background gradients
- Button colors
- Text colors
- Glow effects

### Animations

Animation speeds and effects can be adjusted by modifying the timer values in the `root.after()` calls.

### Game Settings

- **Rounds**: Change `max_rounds` variable (default: 5)
- **Window Size**: Modify `geometry()` parameters
- **Fonts**: Update font families and sizes

## 🔧 Troubleshooting

### Common Issues

**Game doesn't start:**

- Ensure Python 3.6+ is installed
- Check if Tkinter is available: `python -c "import tkinter"`

**Modern version crashes:**

- Install Pillow: `pip install pillow`
- Verify PIL import: `python -c "from PIL import Image"`

**Display issues:**

- Update your graphics drivers
- Try running with different Python versions

## 🤝 Contributing

Feel free to contribute to this project by:

- Adding new themes
- Improving animations
- Fixing bugs
- Adding new features

## 📄 License

This project is open source and available under the MIT License.

## 🎉 Acknowledgments

- Inspired by the classic Rock Paper Scissors game
- Modern web design principles
- Cyberpunk aesthetic trends
- Python Tkinter community

---

## Enjoy playing! 🎮✨

*Choose your style: Go cyberpunk with neon effects or keep it clean with modern gradients!*
