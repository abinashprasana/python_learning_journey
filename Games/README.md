# 🎮 Games

*Program Folder:* Python Quiz Game & Slot Machine  
*Author:* Abinash Prasana

---

## 📌 Description

This folder contains beginner-friendly terminal-based games written in Python.  
They were created as part of my Python relearning journey — to reinforce fundamentals while keeping it interactive and fun.

Games included:

- ✅ A general knowledge *Quiz Game* that evaluates answers and scores you
- 🎰 A *Slot Machine* that lets you spin emoji reels and win based on lucky matches

---

## 🧠 Features

- Multiple-choice question logic  
- Emoji reel spinning and reward system  
- Score and balance tracking  
- Input validation  
- Use of random, loops, and conditionals

---

## 🛠 How It Works

### python_quiz_game.py  
- Asks 5 general knowledge questions  
- Accepts user input (a/b/c/d) and compares it with the correct answer  
- Tracks guesses and calculates the final score as a percentage  

### python_slot_machine.py  
- Starts with a default balance ($100)  
- Accepts bet input from the user  
- Spins 3 emoji slots (🍒, 🍋, 🔔, ⭐, etc.)  
- Rewards multiplier based on matching symbols  
- Balance updates each round — continues until the user quits or balance is 0  

---

## ▶ Sample Output

### 🎲 Quiz Game
```bash
1. What is the capital of Canada?
a) Toronto
b) Vancouver
c) Ottawa
d) Montreal
Enter your option (a/b/c/d): c
Correct!

Result:
Answers: c d c a c  
Guesses: c d c b c  
Your score is 80%

###🎰 Slot Machine Output:
```bash
Current balance: $100
Place your bet amount: $10

Spinning.....
🍒 | 🍒 | 🍒
You won $30

Would you like to play again? (Y/N): N
Game over! Your final balance is $120
