# Solver for Letter Boxes on NYT Games
import os


def load_word_list(path):
    with open(path) as f:
        words = [word.lower() for word in f.read().splitlines()]

    return words


def has_only_puzzle_letters(word, puzzle_letters):
    for character in word:
        if character not in puzzle_letters:
            return False

    return True


def has_no_consecutive_letters_on_same_side(word, puzzle_letters):    
    for i in range(len(word) - 1):
        side1 = puzzle_letters.find(word[i]) // 3
        side2 = puzzle_letters.find(word[i + 1]) // 3

        if side1 == side2:
            return False

    return True

    
def filter_word_list(words, puzzle_letters):
    filtered_words = [
        word.lower() for word in words
        if has_only_puzzle_letters(word, puzzle_letters)
        and has_no_consecutive_letters_on_same_side(word, puzzle_letters)
        and word.isalpha()
        and len(word) >= 3
    ]
    
    return filtered_words


def combo_has_all_letters(word1, word2, puzzle_letters):
    combo = word1 + word2
    
    for letter in puzzle_letters:
        if letter not in combo:
            return False

    return True


def last_and_first_letters_match(word1, word2):
    return word1[-1] == word2[0]


def show_solutions(solutions):
    if not solutions:
        print("No solutions found.")
    else:
        print(f"Found {len(solutions)} possible solution(s):")
        for word1, word2 in solutions:
            print(word1, word2)


def data_is_valid(dictionary, puzzle_letters):
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
    if not data_is_valid(dictionary, puzzle_letters):
        return []
    
    all_words = load_word_list(dictionary)
    usable_words = filter_word_list(all_words, puzzle_letters)
    puzzle_letters = puzzle_letters.lower()

    solutions = []
    
    for word1 in usable_words:
        for word2 in usable_words:
            if not last_and_first_letters_match(word1, word2):
                continue

            if combo_has_all_letters(word1, word2, puzzle_letters):
                solutions.append([word1, word2])

    return solutions


def main():
    dictionary = 'dictionary.txt'
    puzzle_letters = 'xlbocuimqayt'

    solutions = solve(dictionary, puzzle_letters)
    show_solutions(solutions)


# Go!
if __name__ == '__main__':
    main()
