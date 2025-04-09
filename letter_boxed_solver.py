# Solver for Letter Boxes on NYT Games
import os


def load_word_list(path):
    """
    Loads a list of words from a file, converting each to lowercase.
    
    Args:
        path (str): The file path to the dictionary.

    Returns:
        list: A list of words in lowercase.
    """
    with open(path) as f:
        words = [word.lower() for word in f.read().splitlines()]

    return words


def only_contains_puzzle_letters(word, puzzle_letters):
    """
    Check if the word contains only letters from puzzle_letters.
    
    Args:
        word (str): The word to check.
        puzzle_letters (str): The valid letters for the puzzle.

    Returns:
        bool: True if the word only contains valid letters, False otherwise.
    """
    for character in word:
        if character not in puzzle_letters:
            return False

    return True


def no_consecutive_letters_on_same_side(word, puzzle_letters):    
    """
    Check if no consecutive letters in the word are on the same side.
    
    Args:
        word (str): The word to check.
        puzzle_letters (str): The valid letters for the puzzle.

    Returns:
        bool: True if no consecutive letters are on the same side, False otherwise.
    """
    for i in range(len(word) - 1):
        side1 = puzzle_letters.find(word[i]) // 3
        side2 = puzzle_letters.find(word[i + 1]) // 3

        if side1 == side2:
            return False

    return True

    
def filter_word_list(words, puzzle_letters):
    """
    Filters a list of words based on game rules.
    
    Args:
        words (list): List of words to filter.
        puzzle_letters (str): The valid letters for the puzzle.

    Returns:
        list: A list of words that meet the puzzle constraints.
    """
    filtered_words = [
        word.lower() for word in words
        if only_contains_puzzle_letters(word, puzzle_letters)
        and no_consecutive_letters_on_same_side(word, puzzle_letters)
        and word.isalpha()
        and len(word) >= 3
    ]
    
    return filtered_words


def combo_has_all_letters(word1, word2, puzzle_letters):
    """
    Check if the combined letters of word1 and word2 include all puzzle letters.
    
    Args:
        word1 (str): The first word.
        word2 (str): The second word.
        puzzle_letters (str): The valid letters for the puzzle.

    Returns:
        bool: True if the combined words include all puzzle letters, False otherwise.
    """
    combo = word1 + word2
    
    for letter in puzzle_letters:
        if letter not in combo:
            return False

    return True


def words_connect(word1, word2):
    """
    Check if the last letter of word1 matches the first letter of word2.
    
    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        bool: True if the last letter of word1 matches the first letter of word2, False otherwise.
    """
    return word1[-1] == word2[0]


def show_solutions(solutions):
    """
    Display the solutions found.
    
    Args:
        solutions (list): A list of word pairs.
    """
    if not solutions:
        print("No solutions found.")
    else:
        print(f"Found {len(solutions)} possible solution(s):")
        for word1, word2 in solutions:
            print(word1, word2)


def data_is_valid(dictionary, puzzle_letters):
    """
    Validate the dictionary and puzzle letter constraints.
    
    Args:
        dictionary (str): The dictionary file path.
        puzzle_letters (str): The puzzle letters.

    Returns:
        bool: True if the data is valid, False otherwise.
    """
    valid = True
    
    if not os.path.exists(dictionary):
        print(f"The dictionary file '{dictionary}' does not exist.")
        valid = False
    elif len(puzzle_letters) != 12:
        print("The puzzle must contain exactly 12 letters.")
        valid = False
    elif len(puzzle_letters) != len(set(puzzle_letters)):
        print("All puzzle letters must be unique.")
        valid = False

    return valid


def solve(dictionary, puzzle_letters):
    """
    Solve the Letter Boxes puzzle using the provided dictionary and puzzle letters.
    
    Args:
        dictionary (str): The dictionary file path.
        puzzle_letters (str): The puzzle letters.

    Returns:
        list: A list of word pairs that meet the puzzle constraints.
    """
    if not data_is_valid(dictionary, puzzle_letters):
        return []
    
    all_words = load_word_list(dictionary)
    usable_words = filter_word_list(all_words, puzzle_letters)
    puzzle_letters = puzzle_letters.lower()

    solutions = []
    
    for word1 in usable_words:
        for word2 in usable_words:
            if not words_connect(word1, word2):
                continue

            if combo_has_all_letters(word1, word2, puzzle_letters):
                solutions.append([word1, word2])

    return solutions


def main():
    """
    Main function to run the solver.
    """
    DICTIONARY = 'dictionary.txt'
    PUZZLE_LETTERS = 'xlbocuimqayt'

    solutions = solve(DICTIONARY, PUZZLE_LETTERS)
    show_solutions(solutions)


# Go!
if __name__ == '__main__':
    main()
