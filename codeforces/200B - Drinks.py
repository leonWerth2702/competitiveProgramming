number_of_oranges = int(input())
orange_juice_in_percent = list(map(int, input().split()))

result = 0

for i in range(number_of_oranges):
    result += orange_juice_in_percent[i] / 100

print(result / number_of_oranges * 100)

