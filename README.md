# Hangman
A classic letter guessing game, attempting to uncover the hidden word within a certain number of guesses.

## Requirements
We are implementing a simple API that encapsulates the **game logic** and **state**. 
Each call to the game engine represents a player turn. 
The game engine must retain state between calls and track the game state, determine if the player has won or lost, etc.

## Hints/Guidelines
1. Work backwards from the test to discover what the behavior of the game engine is supposed to be. 
2. The tests expect very specific formats, values, and/or exceptions be raised for specific game conditions.
3. The goal is to have as many test functions PASS as possible. 
4. Pay attention to the test method names.
5. The `Hangman` game engine class does not define all required methods. You will discover more methods in the tests that need to be created.
6. Determining reasonable data structure(s) that supports the required operations is the key to this exercise.
7. Please do not alter the test code in `test.py` (except temporarily to comment out test methods, please do not alter the actual code).
8. Type annotations are recommended but not required.
9. Please describe your approach/thinking as you go (as you might for pair programming). Please ask questions for anything that is unclear.
10. Please do not use ChatGPT, etc. or Stack Overflow. Python docs[https://docs.python.org/3.11/] are available for Python language reference.
11. It is not necessary to complete the exercise, work at a reasonable pace and complete as much as possible in the available time.
12. The unit tests may be run in the terminal with this command: `python -m unittest`
```
