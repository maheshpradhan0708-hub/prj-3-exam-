# 💰 Bill Splitter App

A simple Python console program that splits a restaurant/group bill among multiple people, with optional tip calculation.

---

## 🎯 Objective

To build a console-based application that helps a group of people quickly and fairly split a total bill — including an optional tip — and see exactly how much each person owes.

---

## 📋 Problem Statement

Design a program that:

- Takes the **total bill amount** and the **number of people** sharing it as input.
- Asks the user whether they want to add a **tip**, and if so, takes the tip percentage.
- Calculates:
  - The **tip amount** (based on the percentage of the total bill).
  - The **final bill** (original bill + tip).
  - The **amount each person must pay** (final bill ÷ number of people).
- Displays a clean, formatted **Bill Summary**.
- Asks the user if they'd like to perform another calculation, and shows a closing thank-you message.

---

## 🗺️ Program Flow

```
┌───────────────────────────────┐
│         START PROGRAM          │
└───────────────┬─────────────────┘
                │
                ▼
     Print welcome banner
                │
                ▼
   Input: total bill amount (₹)
                │
                ▼
   Input: number of people
                │
                ▼
   Ask: "Add a tip? (yes/no)"
                │
        ┌───────┴────────┐
        ▼                ▼
      "yes"             "no"
        │                │
        ▼                │
 Input: tip percentage    │
        │                │
 tip_amount = bill × %    │
        │                │
        └───────┬────────┘
                ▼
   final_bill = bill + tip_amount
                │
                ▼
   per_person = final_bill / people
                │
                ▼
     Print Bill Summary:
     - Original Bill
     - Tip Amount
     - Final Bill
     - Each Person Pays
                │
                ▼
  Ask: "Do another calculation? (yes/no)"
                │
        ┌───────┴────────┐
        ▼                ▼
      "yes"             not "yes"
        │                │
   (program ends —        ▼
    no loop currently   Print thank-you
    implemented)          message
                │                │
                └───────┬────────┘
                        ▼
                    END PROGRAM
```

> ⚠️ **Note:** The current version calculates the bill once and does not actually loop back when the user answers "yes" to *"Do another calculation?"* — see [Known Issues](#-known-issues--suggested-fixes) below.

---

## ⚙️ Features

| Step | Description |
|---|---|
| 1 | Enter total bill amount |
| 2 | Enter number of people splitting the bill |
| 3 | Optionally add a tip (percentage-based) |
| 4 | View a formatted bill summary (original, tip, final, per-person) |
| 5 | Option to run another calculation |

---

## 🖥️ Sample Output

```
----------------------------------
Welcome To The Bill Spliter App!
----------------------------------
Enter total bill amount: ₹777
Enter number of people: 7
Do you want to add tip? (yes/no): yes
Enter tip percentage: 20
------ Bill Summary ------
Original Bill : ₹777.00
Tip Amount    : ₹155.40
Final Bill    : ₹932.40
Each Person Pays : ₹133.20

 Do another calculations? (yes/no): no
---thankyou for useing to the our bill spliter app---
```

---

## ▶️ How to Run

```bash
python p_exam.py
```

Follow the prompts to enter the bill amount, number of people, and (optionally) a tip percentage.

---

## 🐞 Known Issues & Suggested Fixes

1. **Invalid escape sequences (`\W`, `\-`)**
   Strings like `"\Welcome To The Bill Spliter App!"` and `"\------ Bill Summary ------"` trigger `SyntaxWarning: invalid escape sequence` because `\W` and `\-` aren't valid escape codes in Python.
   → Fix: remove the stray backslash, e.g. `"Welcome To The Bill Spliter App!"`.

2. **No actual repeat loop**
   The program asks *"Do another calculation?"* but isn't wrapped in a `while` loop, so answering "yes" doesn't restart it.
   → Fix: wrap the whole program body in a `while True:` loop and use `break` when the user answers "no".

3. **No input validation**
   Entering non-numeric text for the bill amount, number of people, or tip percentage will crash the program with a `ValueError`.
   → Fix: wrap inputs in `try/except` blocks.

4. **Division by zero risk**
   If the user enters `0` for the number of people, `per_person = final_bill / people` will raise a `ZeroDivisionError`.
   → Fix: validate that `people > 0` before dividing.

5. **Minor spelling**: "Spliter" → "Splitter", "useing" → "using" (cosmetic only).

---

## 🧠 Concepts Demonstrated

- Taking and converting user input (`float`, `int`)
- Conditional logic (`if / else`)
- Basic arithmetic (percentage calculation, division)
- Formatted string output (f-strings, `:.2f` for currency)
- Simple yes/no decision flow

---

## 👤 Author

**Author:** Mahesh
**Project:** Bill Splitter App
**Language:** Python 3.13
**Type:** Console Application / Beginner Assignment
