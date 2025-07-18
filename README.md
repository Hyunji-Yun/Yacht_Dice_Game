# 🎲 Yacht Dice Game 🎲

A web-based implementation of the classic Yahtzee-style dice game, designed for 2–4 players. This turn-based game allows players to roll dice, select strategies, and compete for the highest score using a clean, responsive, and user-friendly interface.

---

## Features

- Up to 4 player support  
- Roll 5 dice per turn (up to 3 times)  
- Select dice to keep and reroll others  
- Choose from 13 strategy categories (e.g., Full House, Straights, Yacht)  
- Automatic score calculation and scoreboard updates  
- Game-over screen with final scores and winner announcement  
- "Start New Game" button to replay seamlessly

---

## Tech Stack

- **Backend**: Python (Flask)  
- **Frontend**: HTML5, CSS3, Jinja2  
- **Styling**: Custom CSS with Bootstrap-inspired layout  
- **Templating**: Jinja2 dynamic rendering for scoreboard and strategy mapping

---

## How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/yacht-dice-game.git
   cd yacht-dice-game
   ```

2. Install dependencies (optional virtual environment recommended)  
   ```bash
   pip install flask
   ```

3. Run the Flask app  
   ```bash
   python app.py
   ```

4. Open in browser  
   Go to: `http://localhost:5000`

---

## Scoring Rules Overview

### Upper Section

- Ones (1s) through Sixes (6s): Sum of matching dice  
- **Bonus**: +35 points if total Upper Score ≥ 63  

### Lower Section

- 3 of a Kind: Sum of all dice  
- 4 of a Kind: Sum of all dice  
- Full House: 25 points  
- Small Straight: 30 points  
- Large Straight: 40 points  
- Yacht: 50 points  
- Choice: Sum of all dice  

---

## Screenshots

### Player Setup  
![Player Setup](screenshots/setup.png)

### In-Game View  
![Gameplay](screenshots/gameplay.png)

### Game Over Screen  
![Game Over](screenshots/gameover.png)

