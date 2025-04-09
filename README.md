# NYT Letter Boxed Solver
Every [New York Times Letter Boxed](https://www.nytimes.com/puzzles/letter-boxed) game has a two-word solution. This is a Python solver for the game. It reads a list of dictionary words and finds all possible two-word solutions from the dictionary. The included dictionary file contains many obscure words, so you may have to test several possible solutions before you find one that the game will accept.

## Requirements

- Python 3.6 or higher

## Usage

1. **Edit the solver code** (Optional).

    Open `letterbox_solver.py` and edit the `DEFAULT_PUZZLE_LETTERS` constant at the top of the program. The puzzle letters should be ordered so that each set of three consecutive letters represents a side. They can be upper or lowercase. Optionally, you can edit the ```DEFAULT_DICTIONARY``` constant. The dictionary should be a plaintext file with one word per line.

    ```python
    DEFAULT_PUZZLE_LETTERS = 'xlbocuimqayt'
    DEFAULT_DICTIONARY = 'dictionary.txt'
    ```

2. **Run the solver**:

    You can run the solver in two ways:

    - **From your IDE**: Simply open `python letter_boxed_solver.py` in your Python IDE and run the script.

    - **From the terminal**:
      - To run the solver with the default dictionary and puzzle letters, execute:

      ```bash
      python letter_boxed_solver.py
      ```

      - To specify a puzzle letters or a custom dictionary file, use either or both of the optional command-line arguments `-p` for the puzzle letters and `-d` for the dictionary file:

      ```bash
      python letter_boxed_solver.py -p 'abcdeghijklm' -d custom_dictionary.txt 
      ```

    - **From an import**:
      - Import letter_boxed_solver and call the solve function with the dictionary and puzzle letters of your choice.

      ```bash
      import letter_boxed_solver
      
      solutions = letter_boxed_solver.solve('abcdeghijklm') # will use default dictionary
      solutions = letter_boxed_solver.solve('abcdeghijklm', 'custom_dictionary.txt')
      ```

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

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
