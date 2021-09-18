number_of_buttons = int(input())
buttons = list(map(int, input().split()))

fastened_right = 'YES'
count_open_buttons = 0

for i in range(number_of_buttons):
    if buttons[i] == 0:
        count_open_buttons += 1

if number_of_buttons == 1:
    if buttons[0] == 0:
        fastened_right = 'NO'
else:
    if count_open_buttons != 1:
        fastened_right = 'NO'

print(fastened_right)

