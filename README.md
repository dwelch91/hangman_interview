# Hangman
A classic letter guessing game, attempting to uncover the hidden word within a certain number of guesses.

## Requirements

We are implementing a simple API that encapsulates the **game logic** and **state**. 


## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. 

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" a `ValueError` when the game has ended but the player tries to continue playing. The tests will only pass if you both `raise` the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# when player tries to play, but the game is already over.
raise ValueError("The game has already ended.")
```
