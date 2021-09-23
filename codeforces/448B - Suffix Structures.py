def is_automaton(word1, word2):
    i = 0
    j = 0

    while i < len(word1) and j < len(word2):
        if word1[i] == word2[j]:
            j += 1
        i += 1

    return j == len(word2)


def is_array(word1, word2):
    if len(word1) == len(word2):
        list_word1 = sorted(list(word1))
        list_word2 = sorted(list(word2))
        
        for index in range(len(word1)):
            if list_word1[index] != list_word2[index]:
                return False
            
        return True
    
    return False


def is_both(word1, word2):
    list_word1 = list(word1)

    for index in range(len(word2)):
        if word2[index] not in list_word1:
            return False

        pos = list_word1.index(word2[index])
        list_word1[pos] = '0'

    return True


def process_input():
    s = input()
    t = input()
    return s, t


def solve():
    words1, words2 = process_input()
    result = ''
    if is_automaton(words1, words2):
        result = 'automaton'
    elif is_array(words1, words2):
        result = 'array'
    elif is_both(words1, words2):
        result = 'both'
    else:
        result = 'need tree'
    print(result)


solve()

