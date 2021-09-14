n, h = map(int, input().split())
minimum_widths = 0
height_of_friends = list(map(int, input().split()))

for i in range(n):
    if height_of_friends[i] > h:
        minimum_widths += 2
    else:
        minimum_widths += 1

print(minimum_widths)

