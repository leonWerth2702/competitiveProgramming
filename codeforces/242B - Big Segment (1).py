number_of_segments = int(input())

smallest = float('inf')
greatest = float('-inf')
result = -1

for index in range(number_of_segments):
    small, great = map(int, input().split())

    if small <= smallest and great >= greatest:
        smallest = small
        greatest = great
        result = index + 1
    else:
        if small > smallest and great > greatest:
            greatest = great
            result = -1
        elif small < smallest and great < greatest:
            smallest = small
            result = -1

print(result)

