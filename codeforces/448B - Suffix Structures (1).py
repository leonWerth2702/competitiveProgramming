def get_char(letter):
    return chr(letter + ord('a'))


def process_input():
    s = input()
    t = input()
    return s, t


def solve():
    word1, word2 = process_input()
    need_tree = array = automaton = False

    for index in range(26):
        word1_count = word1.count(get_char(index))
        word2_count = word2.count(get_char(index))

        if word2_count > word1_count:
            need_tree = True
        elif word2_count < word1_count:
            automaton = True

    match = -1

    for index in range(len(word2)):
        index_found = word1.find(word2[index], match + 1)
        if index_found > match:
            match = index_found
        else:
            array = True
            break

    if need_tree:
        print('need tree')
    elif automaton and array:
        print('both')
    elif array:
        print('array')
    else:
        print('automaton')


solve()


