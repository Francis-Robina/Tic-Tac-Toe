#  Tic-Tac-Toe AI – Unbeatable Player with Minimax Algorithm

##  Overview
This project implements an **unbeatable Tic-Tac-Toe AI** using the **Minimax algorithm** (with optional Alpha-Beta Pruning).  
The AI evaluates all possible moves and always plays optimally — it will **win if possible** and **draw otherwise**, never losing to a human player.

##  How It Works
The **Minimax Algorithm** is a recursive decision-making method used in two-player games.  
It assumes that:
- The AI tries to **maximize** its score.
- The opponent tries to **minimize** the AI’s score.

**Scoring system:**
- AI Win → `+1`
- Human Win → `-1`
- Draw → `0`

### Algorithm Steps:
1. **Check for Terminal State** (win, loss, or draw).
2. If it’s the **AI’s turn** → choose the move with the **highest score**.
3. If it’s the **human’s turn** → choose the move with the **lowest score**.
4. Repeat recursively until the game is over.

##  Alpha-Beta Pruning (Optional)
To improve efficiency, Alpha-Beta Pruning skips exploring branches that can’t affect the outcome.  
This optimization **reduces computation time** without changing the AI’s decision.

##  Technologies Used
- **Python** (Core Logic)
- **Minimax Algorithm**
- Optional: Tkinter/Pygame for GUI

##  How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe-ai.git
