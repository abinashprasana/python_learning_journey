# 🛠 Utility Tools

This folder contains beginner-friendly, terminal-based Python tools designed to simulate useful everyday utilities. Each script focuses on real-world tasks while reinforcing Python fundamentals like loops, functions, and user input handling.

---

## 📜 Included Programs

### 1. ⏳ Countdown Timer
**File:** `Python_Countdown Timer/main.py`  
Prompts the user to enter a duration in seconds, then displays a real-time countdown in HH:MM:SS format.

**How to Run:**
```bash
python main.py
```

**Sample Output:**
```
⏳ Enter the countdown time in seconds: 10
Time left: 00:00:10
Time left: 00:00:09
...
Time's up!
```

---

### 2. 🛒 Shopping Cart Calculator  
**File:** `Python_Shopping Cart Calculator/main.py`  
Allows users to add items and prices to a virtual cart and calculates the total.

**How to Run:**
```bash
python main.py
```

**Sample Output:**
```
Enter item name (or 'done' to finish): Apple
Enter price for Apple: 30
Enter item name (or 'done' to finish): Banana
Enter price for Banana: 20
Enter item name (or 'done' to finish): done

🛍️ Items in cart:
- Apple: ₹30
- Banana: ₹20
Total: ₹50
```

---

### 3. 🍽️ Menu-Based Order System  
**File:** `Python_Menu-Based Order System/main.py`  
Displays a fixed menu, lets users select items, and calculates the total bill.

**How to Run:**
```bash
python main.py
```

**Sample Output:**
```
Menu:
1. Pizza - ₹100
2. Burger - ₹50
3. Juice - ₹30
Enter item number to order (0 to finish): 1
Enter item number to order (0 to finish): 2
Enter item number to order (0 to finish): 0

Your total bill: ₹150
```

---

### 4. ⏰ Alarm Clock  
**File:** `Alarm clock/main.py`  
Takes an alarm time from the user and plays an alarm sound when the time matches the system clock.

**How to Run:**
```bash
python main.py
```

**Sample Output:**
```
Enter the alarm time (HH:MM:SS): 07:00:00
Alarm set for 07:00:00
...
WAKE UP 😩
```

---

### 5. 🔄 Simulated File Downloader with Multithreading  
**File:** `Python_Simulated File Downloader with Multithreading/main.py`  
Simulates downloading multiple files concurrently using multithreading.

**How to Run:**
```bash
python main.py
```

**Sample Output:**
```
---- Starting downloads ----

Starting downloading Document.pdf...
Starting downloading Photo.png...
...
Finished downloading Photo.png in 3 seconds
...
---- All downloads completed ----
```

---

## 🧠 Key Concepts Used
- Loops and conditionals
- Functions and user input
- Dictionaries, lists, and formatting
- `time.sleep()`, `datetime`, `pygame`
- Python multithreading with `threading.Thread`

---

These tools are part of my Python learning journey — helping me brush up on key language features through hands-on mini projects.
