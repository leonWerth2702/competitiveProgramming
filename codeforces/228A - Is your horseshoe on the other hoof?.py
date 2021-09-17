colors = list(map(int, input().split()))

distinct = []
for i in range(4):
    if colors[i] not in distinct:
        distinct.append(colors[i])

print(4 - len(distinct))


