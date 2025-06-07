# 🧾 Logger and Timer Decorator

**Program:** Python Logger and Timer Decorator  
**Author:** Abinash Prasana

---

## 📌 Description
This program demonstrates the use of Python decorators to log function calls and measure execution time. It’s a clean and practical example of functional programming where logic is abstracted using higher-order functions.

---

## 🧠 Features
- Logs function names when they are called
- Measures and prints the execution time of each function
- Supports wrapping any function using the `@log_and_timer` decorator
- Shows how decorators help track performance without modifying the function's core logic

---

## ⚙️ How It Works
1. `log_and_timer` is a decorator that wraps around any target function.
2. When a decorated function is called, it:
   - Logs the function name
   - Tracks the time before and after execution
   - Prints the time taken for execution
3. Demonstrated with:
   - A simple greeting function
   - A function that calculates the sum of a range

---

## ▶️ Sample Output
```bash
[LOG] calling function: greet
Hello, Abby!

[LOG] Function: greet executed in 0.000001 seconds

[LOG] calling function: calculate_sum
Sum of number from to 1999 is 1999000

[LOG] Function: calculate_sum executed in 0.0007 seconds
```

---

## 🧪 Concepts Covered
- Decorators
- Timing execution using `time` module
- Function introspection
- Functional programming patterns

---