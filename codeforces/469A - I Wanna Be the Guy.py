n = int(input())

little_x = list(map(int, input().split()))
little_y = list(map(int, input().split()))
del little_x[0]
del little_y[0]

result = 'I become the guy.'
for i in range(1, n + 1):
    if i not in little_x and i not in little_y:
        result = 'Oh, my keyboard!'
        break

print(result)

