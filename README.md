# Integer Calculator

A simple desktop application built in Python for performing basic arithmetic operations with integers. This project was created as a part of my school studies, using the Tkinter library.

## ⚙️ Features

The application accepts two integer numbers as input and allows for the following operations:

* **Addition** (`+`)
* **Subtraction** (`-`)
* **Multiplication** (`*`)
* **Integer Division** (`//`)
* **Modulo** (remainder after division, `%`)
* Displays the result in a read-only field.
* Handles error inputs (such as non-numeric values or division by zero).

## 💻 How to Use

1.  Run the script from your command line (e.g., `python main.py`).
2.  The "Integer Calculator" application window will open.
3.  Enter the first number into the **"1st Number"** field.
4.  Enter the second number into the **"2nd Number"** field.
5.  Click one of the operation buttons (`+`, `-`, `*`, `//`, `%`) to perform the calculation.
6.  The result will immediately appear in the **"Result"** field.
7.  To close the application, press the **"Exit"** button.

## 📝 Notes

* The application works **only with integers**. Entering a decimal number or text will trigger an error message.
* For the `//` and `%` operations, **division by zero is not allowed**. The program will display a warning message if this is attempted.

## 🛠 Technologies Used

* **Python**
* **Tkinter** (Python's standard GUI library)
