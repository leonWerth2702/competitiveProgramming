number_of_passwords, number_of_failed_tries = map(int, input().split())

cnt = [0] * 101

for _ in range(number_of_passwords):
    current_password = input()
    cnt[len(current_password)] += 1

correct_password = input()

best_time = worst_time = 0

for i in range(len(correct_password)):
    best_time += cnt[i]

worst_time = best_time + cnt[len(correct_password)] - 1

best_time += (best_time // number_of_failed_tries * 5) + 1
worst_time += (worst_time // number_of_failed_tries * 5) + 1

print(f'{best_time} {worst_time}')

