number_of_interesting_minutes = int(input())
interesting_minutes = list(map(int, input().split()))

result = 15

for minutes in interesting_minutes:
    if minutes <= result:
        result = minutes + 15
    else:
        break

print(min(90, result))

