name_of_exhibit = input()

minimum_rotate = 0
current_letter = 'a'

for letter in name_of_exhibit:
    current_rotate = abs(ord(current_letter) - ord(letter))

    if current_rotate < 13:
        minimum_rotate += current_rotate
    else:
        minimum_rotate += 26 - current_rotate

    current_letter = letter

print(minimum_rotate)

