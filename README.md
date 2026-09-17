# Number Guessing Game

A Python based number guessing game where the player tries to guess a randomly generated number.

## About the Project

This project was created as part of my Python learning journey.

The game generates a random number within a predefined range. The player enters guesses until they find the correct number.

The game uses a ratio based approach to compare the player's guess with the randomly generated number. Based on the ratio, the game provides feedback on whether the guess is too high, too low, or close to the target number.

## How the Game Works

1. The computer generates a random number.
2. The player enters a guess.
3. The program compares the guess with the randomly generated number.
4. A ratio between the generated number and the player's guess is calculated.
5. Based on the ratio, the game indicates whether the guess is too high, too low, or close enough to the target number.
6. The player continues guessing until the correct number is found.
7. The game displays a success message when the correct number is guessed.

## Game Logic

The game does not only check whether the player's guess is higher or lower than the generated number.

Instead, it calculates a ratio between the generated number and the player's guess. This ratio is used to determine how close the player's guess is to the target number.

The game provides three types of feedback:

* **Too Low**: The player's guess is significantly lower than the target number.
* **Too High**: The player's guess is significantly higher than the target number.
* **Close Enough**: The player's guess is within the defined range of the target number.

This approach makes the feedback more informative and gives the player an indication of how close the guess is to the target number.

## Features

* Random number generation
* Ratio based guess evaluation
* Feedback based on the closeness of the guess
* User input handling
* Comparison operators
* Conditional statements
* While loop
* Random module
* Interactive console based gameplay

## Technologies Used

* Python 3
* VS Code

## Python Concepts Practiced

This project helped me practice fundamental Python concepts, including:

* Variables
* User input
* Type conversion
* If, elif, and else statements
* While loops
* Comparison operators
* Arithmetic operations
* Random number generation
* The `random` module
* Basic program flow

## How to Run

Make sure Python is installed on your computer.

Clone the repository or download the project files.

Run the following command in the terminal:

```bash
python Nnumber_guessing_game.py
```

## Project Structure

```text
number-guessing-game/
│
├── Nnumber_guessing_game.py
└── README.md
```

## Example Gameplay

```text
I have selected a number between 1 and 100.

Enter your guess: 50

Your guess is too high.

Enter your guess: 25

Your guess is too low.

Enter your guess: 37

Your guess is close enough!

Enter your guess: 40

Congratulations! You guessed the correct number.
```

## Future Improvements

Possible improvements for future versions:

* Add difficulty levels
* Add a limited number of attempts
* Add a scoring system
* Add a replay option
* Track the number of attempts
* Add a high score system
* Add a graphical user interface

## Author

Kalpesh Baviskar
