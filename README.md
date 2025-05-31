# Guess the Number Game

A simple Python program that allows users to play a game of Guess the Number against the computer.

## Overview

The Guess the Number Game is a command-line program that provides a simple way to play a game of Guess the Number against the computer. The program uses a menu-driven interface to handle user input and display the game results.

## Usage

1. Run the program using `python main.py`
2. Enter a minimal and maximum number when prompted
3. Take a guess by entering a number within the given range
4. The program will display whether your guess is higher or lower than the target number
5. Keep guessing until you correctly guess the target number
6. Type 'yes' to play again or 'no' to quit

## Features

* Allows users to play a game of Guess the Number against the computer
* Handles invalid input and displays error messages
* Displays the game results and number of attempts taken
* Allows users to play again or quit
* Simple command-line interface

## Code Structure

The program consists of a single function, `start_game()`, which controls the program flow and handles user input.

## Requirements

* Python 3.10.12 (tested on Python 3.10.12)
* `random` library (built-in)

## Notes

* This program uses a simple and efficient algorithm to generate a random target number.
* The program does not store any user data and is for educational purposes only.