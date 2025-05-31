# 🎮 Games

This repository contains a collection of beginner-friendly terminal-based Python games built as part of my learning journey.

*Author:* Abinash Prasana

Each game explores different Python concepts like loops, conditionals, functions, input validation, and more.

---

## 🧠 Quiz Game

### 📌 Description:
A terminal-based multiple-choice quiz game that:
- Asks five general knowledge questions
- Lets users input their guesses
- Tracks and displays the score at the end

### 🧠 Features:
- Multiple-choice format  
- Input validation  
- Score tracking and percentage display  

### ▶ Sample Output:
bash
---------------------------
1. What is the capital of Canada?
a) Toronto
b) Vancouver
c) Ottawa
d) Montreal
Enter your option (a/b/c/d): c
Correct!
...
---------------------------
Result
---------------------------
Answers: c d c a c
Guesses: c d c b c
Your score is 80%


---

## 🎰 Slot Machine

### 📌 Description:
A simple betting-based slot machine game built in Python that:
- Randomly spins symbols like 🍒, 🍉, 🍋, 🔔, ⭐  
- Lets users place bets and win based on matching rows  

### 🧠 Features:
- Randomized outcomes  
- Bet handling and balance tracking  
- Payouts based on matched symbols  

### ▶ Sample Output:
bash
Current balance: $100
Place your bet amount: $10

Spinning.....
**************
🍒 | 🍒 | 🍒
**************
You won $30

Would you like to play again? (Y/N): N
Game over! Your final balance is $120


---

## 🎯 Hangman Game

### 📌 Description:
A classic word-guessing game where the player tries to uncover a hidden word letter-by-letter before the hangman drawing completes.

### 🧠 Features:
- ASCII-art hangman display  
- Random word selection from a word list  
- Letter tracking and guess validation  
- Win/lose messages  

### ▶ Sample Output:
bash
****************************
 o
 | 

****************************
_ _ _ _ _ _ _ 
Enter a letter: e
Correct!

...

****************************
 o
/|\
/  \
****************************
a p p l e
🏆 You win! 🏆
