# Wordle in Python

A command-line version of Wordle written in Python. A random 5-letter word is chosen from a word list, and you have 5 lives to guess it. After each guess, the letters are coloured in your terminal to show how close you were.

## How to play

1. The game picks a secret 5-letter word.
2. Type a 5-letter guess and press Enter.
3. Each letter of your guess is coloured:

| Colour | Meaning |
|--------|---------|
| Green | The letter is in the word and in the correct position |
| Yellow | The letter is in the word but in the wrong position |
| Default (white/grey) | The letter is not in the word, or there are no more copies of it left to match |

4. Every valid guess costs one life. Guess the word before you run out of lives to win.
5. Guesses that are not exactly 5 letters are rejected and do not cost a life.

Duplicate letters are handled the way the real Wordle does it. Green matches are counted first, then yellows, so a letter is never coloured more times than it appears in the secret word.

## Requirements

- Python 3
- [colorama](https://pypi.org/project/colorama/)

Install colorama with:

```bash
pip install colorama
```

## Setup

Keep these two files in the same folder:

```
Wordle/
├── wordle.py     # the game
└── wordle.txt    # the word list
```

`wordle.txt` must contain one 5-letter word per line, all in lowercase. For example:

```
adieu
elope
leads
leaky
leave
```

## Running the game

From inside the project folder:

```bash
python3 wordle.py
```

## Example

```
Guess a 5 letter word:adieu
adieu              <- letters shown in colour in the terminal
Lives left: 4
Guess a 5 letter word:leave
leave
Lives left: 3
```

If you win, you will see a congratulations message. If you run out of lives, the game ends and reveals the word.

## Quitting

Press `Ctrl+C` at any time to exit the game.

## How it works

- The word list is loaded from `wordle.txt` and one word is chosen at random.
- On each guess, the game makes two passes over the letters:
  1. **First pass:** finds exact matches (green) and marks those letters as used.
  2. **Second pass:** colours each letter green, yellow (if an unused copy remains in the word), or default.
- Colours are applied with `colorama`'s `Fore` constants and reset after each printed result so the terminal colour doesn't carry over.

## Troubleshooting

- **`FileNotFoundError: wordle.txt`:** Run the game from the folder that contains `wordle.txt`.
- **Error message about restarting the game:** The word picked from `wordle.txt` was not 5 letters long. Check that every line in the file is exactly 5 letters, with no blank lines.
- **No colours showing:** Try a different terminal. Some terminals or IDE output panes do not support colour codes.
