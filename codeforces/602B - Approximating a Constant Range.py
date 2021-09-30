number_of_data_points = int(input())
data_points = list(map(int, input().split()))

count_seq = [0 for _ in range(10**5 + 5)]
k = 0
unique = 0
max_constant_range = 1

for i in range(number_of_data_points):
    if count_seq[data_points[i]] == 0:
        unique += 1

    count_seq[data_points[i]] += 1

    while unique > 2:
        if count_seq[data_points[k]] == 1:
            unique -= 1

        count_seq[data_points[k]] -= 1
        k += 1

    max_constant_range = max(max_constant_range, i - k + 1)

print(max_constant_range)

