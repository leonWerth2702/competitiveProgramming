number_of_cards = int(input())
cards = list(map(int, input().split()))

i = 0
j = number_of_cards - 1
k = 0

points_of_two_player = [0, 0]

while i <= j:
    if cards[i] > cards[j]:
        points_of_two_player[k % 2] += cards[i]
        i += 1
    else:
        points_of_two_player[k % 2] += cards[j]
        j -= 1
    k += 1

print(points_of_two_player[0], points_of_two_player[1], end=' ')

