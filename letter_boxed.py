# Solver for Letter Boxes on NYT Games

def is_possible(word, letters):
    word += ' '
    
    for i in range(len(word) - 1):
        one = word[i]
        two = word[i + 1]
        
        if one not in letters:
            return False
        elif letters.find(one) // 3 == letters.find(two) // 3:
            return False

    return True


def has_all(string, letters):
    for letter in letters:
        if letter not in string:
            return False

    return True


def solve(words, letters):
    words = [word for word in words if is_possible(word, letters)]
          
    for word1 in words:
        last = word1[-1]

        for word2 in words:
            first = word2[0]

            if last == first:
                combo = word1 + word2
                
                if has_all(combo, letters):
                    print(word1, word2)


# Go!
puzzle = 'matdlbeunrix'

with open('all_words.txt') as f:
    words = f.read().splitlines()
    
solve(words, puzzle)

