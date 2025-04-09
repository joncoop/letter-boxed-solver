
# NYT Letter Boxed Solver

Every [New York Times Letter Boxed](https://www.nytimes.com/puzzles/letter-boxed) game has a two-word solution. This is a Python solver for the game. It reads a list of dictionary words and finds all possible two-word solutions from the dictionary. The included dictionary file contains many obscure words, so you may have to test several possible solutions before finding one that the game will accept.

## Requirements

- Python 3.6 or higher

## Usage

1. **Edit the solver code.**

    Open `letterbox_solver.py` and edit the `PUZZLE_LETTERS` constant in the `main()` function. The letters should be ordered so that each set of three consecutive letters represents a side. They can be in uppercase or lowercase.

    ```python
    PUZZLE_LETTERS = 'xlbocuimqayt'  # replace with today's letters
    ```

2. **Run the solver.**

    After editing the letters, simply run the solver.

## Customization

- Change the dictionary file name or location by editing the `DICTIONARY` constant in the `main()` function. The dictionary needs to be a plaintext file with one word per line. The case of the words in the dictionary does not matter. Words with invalid characters are automatically filtered out by the solver, so there is no need to edit the dictionary unless you want to remove obscure words.
- You can also use `solve(dictionary, puzzle_letters)` directly in your own scripts to integrate this logic elsewhere.

## Example Output

```
Today's letters: XLBOCUIMQAYT

Found 7 possible two-word solution(s):
 - QUIXOTIC, CYMBAL
 - QUIXOTIC, CYMBALO
 - QUIXOTIC, CYMBALOM
 - QUIXOTICAL, LAMBOY
 - QUIXOTICAL, LAMBY
 - QUIXOTICAL, LOBOTOMY
 - QUIXOTICAL, LOMBOY
```
