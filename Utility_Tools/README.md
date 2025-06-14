# 🛠 Utility Tools

This folder contains beginner-to-intermediate level Python scripts that simulate practical utilities like timers, downloaders, cart calculators, and alarm clocks. These are built as part of my hands-on Python learning journey.

---

## 🔧 Programs Included

### 🕒 Countdown Timer
A real-time timer that counts down from the number of seconds entered by the user.

**Features:**
- Accepts input in seconds and converts to HH:MM:SS format
- Real-time countdown display using time.sleep()
- Clean and simple CLI format

**How to run:**
```bash
python main.py
```

**Sample Output:**
```
⏳ Timer Set: 00:01:10
Time left: 00:01:09
...
⏰ Time's up!
```

---

### 🛒 Shopping Cart Calculator
Calculates the total cost based on user input of item names and prices.

**Features:**
- User can add multiple items
- Totals are automatically calculated
- Handles float price values with formatting

**How to run:**
```bash
python main.py
```

**Sample Output:**
```
Enter item name: Book
Enter price: 250
Add more? (y/n): y
Enter item name: Pen
Enter price: 20
Add more? (y/n): n
Total: ₹270.00
```

---

### 📋 Menu-Based Order System
Simulates a fixed menu where the user selects items and the program calculates the total.

**Features:**
- Pre-defined menu
- Accepts multiple items
- Calculates subtotal and total

**How to run:**
```bash
python main.py
```

**Sample Output:**
```
1. Burger - ₹100
2. Fries - ₹60
Enter item number to order: 1
Add more? y/n: y
Enter item number to order: 2
Total bill: ₹160
```

---

### ⏰ Alarm Clock
Simple alarm clock that plays an alarm tone at the specified time.

**Features:**
- User sets HH:MM:SS time
- Alarm triggers in real time
- Plays audio using `pygame`

**How to run:**
```bash
python main.py
```

**Sample Output:**
```
Enter alarm time (HH:MM:SS): 07:00:00
Alarm set for 07:00:00
...
WAKE UP 😩
```

---

### 📁 Simulated File Downloader (with Multithreading)
Simulates file downloads using threads and random download durations.

**Features:**
- Demonstrates Python `threading`
- Shows simultaneous download simulation
- Random delay per file download

**How to run:**
```bash
python main.py
```

**Sample Output:**
```
Starting download Document.pdf...
Starting download Photo.png...
Finished download Photo.png in 3s
...
All downloads complete.
```

---

## ✅ Summary

These utility tools cover:
- Loops and conditions
- Real-time input/output
- Threading and time manipulation
- List handling and formatted display

They are built to demonstrate real-world utility programs with simple logic, and strengthen Python fundamentals.

---