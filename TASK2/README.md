# 🎮 Tic-Tac-Toe AI

An intelligent Tic-Tac-Toe game developed using **Python** and the **Minimax Algorithm**. This project was created as part of the **CODSOFT AI Internship Task 2** to explore Artificial Intelligence, Game Theory, and Search Algorithms through a classic strategy game.

---

## 📖 Project Overview

Tic-Tac-Toe is a two-player strategy game played on a 3×3 grid. In this project, the human player competes against an AI opponent that uses the **Minimax Algorithm** to make optimal decisions.

The AI evaluates all possible future game states before making a move, ensuring that it never loses. This project demonstrates how AI can be applied to decision-making problems and strategic gameplay.

---

## 🎯 Objectives

- Understand the fundamentals of Artificial Intelligence.
- Learn and implement the Minimax Algorithm.
- Explore Game Theory concepts.
- Build an interactive command-line game.
- Develop problem-solving and algorithmic thinking skills.

---

## ✨ Features

### 🤖 Intelligent AI Opponent
- Uses the Minimax Algorithm.
- Evaluates all possible moves.
- Always chooses the best move.
- Impossible to beat.

### 🎮 Interactive Gameplay
- Human vs AI mode.
- Simple command-line interface.
- Easy-to-use controls.

### 🏆 Game Logic
- Win detection.
- Draw detection.
- Move validation.
- Automatic game termination.

### 🛡️ Error Handling
- Prevents invalid moves.
- Ensures smooth gameplay experience.

---

## 🏗️ Project Structure

```text
TASK 2/
│
├── tic_tac_toe_ai.py
├── README.md
```

---

## ⚙️ Technologies Used

- Python 3.x
- Minimax Algorithm
- Recursion
- Game Theory

---

## 🧠 How the AI Works

The AI uses the **Minimax Algorithm**, a recursive decision-making algorithm commonly used in turn-based games.

### Scoring System

| Outcome | Score |
|----------|---------|
| AI Wins | +1 |
| Human Wins | -1 |
| Draw | 0 |

The algorithm explores every possible move and chooses the option that maximizes the AI's chances of winning while minimizing the player's chances.

---

## 🔄 Minimax Workflow

```text
Current Board State
          │
          ▼
Generate Possible Moves
          │
          ▼
Simulate Future States
          │
          ▼
Evaluate Scores
          │
          ▼
Choose Best Move
          │
          ▼
Make Move
```

---

## ▶️ Gameplay Instructions

### Symbols

- Human Player = X
- AI Player = O

### Board Positions

```text
(0,0) | (0,1) | (0,2)
---------------------
(1,0) | (1,1) | (1,2)
---------------------
(2,0) | (2,1) | (2,2)
```

### Example Input

```text
Enter row (0-2): 1
Enter column (0-2): 1
```

---

## 📸 Sample Gameplay

```text
=== Tic-Tac-Toe AI ===

You are X
AI is O

X |   | O
---------
  | X |
---------
O |   |

Enter row (0-2): 1
Enter column (0-2): 2

AI is thinking...

X |   | O
---------
  | X | X
---------
O | O |
```

---

## 🧩 Algorithm Complexity

### Time Complexity

```text
O(b^d)
```

Where:

- b = branching factor
- d = depth of game tree

For Tic-Tac-Toe, the search space is small enough to evaluate all possible moves efficiently.

---

## 📚 Concepts Learned

- Artificial Intelligence
- Minimax Algorithm
- Recursive Programming
- Game Theory
- Decision Trees
- Search Algorithms
- Problem Solving
- Python Development

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Designing intelligent game agents
- Implementing recursive algorithms
- Evaluating game states
- Applying game theory principles
- Developing AI-powered applications

---

## 🔮 Future Enhancements

### Advanced Features

- Alpha-Beta Pruning
- Difficulty Levels
- Graphical User Interface (Tkinter/Pygame)
- Score Tracking
- Multiplayer Mode
- Sound Effects
- Online Gameplay

### AI Improvements

- Faster move evaluation
- Enhanced strategy visualization
- Performance optimization

---

## 💡 Advantages

✔️ Unbeatable AI

✔️ Efficient implementation

✔️ Beginner-friendly project

✔️ Demonstrates core AI concepts

✔️ Easy to understand and modify

---

## ⚠️ Limitations

- Command-line interface only.
- Fixed board size (3×3).
- Single-player mode.
- No difficulty settings.

---

## 👨‍💻 Author

**Sumit**

AI Intern at CODSOFT

## 📄 License

This project is developed for educational purposes as part of the **CODSOFT AI Internship Program Task 2**.

---

### 🚀 "Artificial Intelligence is not about replacing humans; it's about creating systems that can think strategically and solve problems efficiently."