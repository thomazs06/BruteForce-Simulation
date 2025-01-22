# BruteForce-Simulation

Welcome, **BruteForce-Simulation**, is a simple Python-based project that demonstrates the fundamentals of brute-force password cracking against a simulated login system. This project is designed for educational purposes only to help learners understand the concept of security testing and how attackers might attempt to gain unauthorized access.

> ⚠**Disclaimer**: This project is for **educational purposes only**. It simulates a brute-force attack on a fake login system to demonstrate how password security might be compromised. Please **do not** use this script on any systems without explicit authorization. Unauthorized access is illegal and unethical.

## Features

- A **simulated login page** built with Flask that mimics a real-world authentication form.
- A **brute-force password cracker** written in Python that attempts to break into the login system by trying a list of common passwords.
- A **password file** containing a set of popular passwords for testing the script's effectiveness.

## Project Structure

Here’s a breakdown of the files and their purposes:

---

## 🧑‍💻 **Fake Login Website**

In this section, we simulate a basic website that mimics a login page. This fake website is built using Flask, a lightweight Python web framework. The website has a simple HTML form with two fields for username and password. The following steps occur when you visit the page:

1. **Login Attempt**: The user is presented with a login form where they can enter a username and password.
2. **Validation**: The website checks if the entered username and password match the predefined credentials. If they match, a success message is shown. If they don’t, an "Invalid credentials" error message is returned.

### **Code Details**:
- **Flask Web App (`app.py`)**: This script sets up the server and handles the user’s login attempts.
- **Login Form Template (`login.html`)**: The HTML template for displaying the login page.

---

## 💻 **Password Cracking Script**

This Python script demonstrates a brute-force attack to guess the correct password by trying every possible password from a list. The script iterates through a text file (`passwords.txt`), which contains common passwords. For each password in the file, it sends a POST request to the fake login website to check if the password is correct.

### **How it Works**:
1. **Password List**: The script reads a list of passwords stored in the `passwords.txt` file.
2. **Brute Force**: For each password in the list, the script attempts to log into the fake website by submitting the username and password via a POST request.
3. **Login Validation**: The script checks the server’s response to determine if the login was successful. If the login is successful, the script prints the correct password to the terminal and exits.

---

## 🔑 **Password List (`passwords.txt`)**

The `passwords.txt` file contains a list of common passwords that will be used in the brute-force attack. These passwords are typically weak and easy to guess, which makes them useful for testing and educational demonstrations. Some example passwords include:



