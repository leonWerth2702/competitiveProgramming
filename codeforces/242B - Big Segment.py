number_of_segments = int(input())

Left, Right = [], []

for _ in range(number_of_segments):
    a, b = map(int, input().split())

    Left.append(a)
    Right.append(b)

left = min(Left)
right = max(Right)
result = -1

for index in range(number_of_segments):
    if left == Left[index] and right == Right[index]:
        result = index + 1
        break

print(result)

