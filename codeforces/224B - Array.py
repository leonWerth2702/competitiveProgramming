n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr_count = [0 for _ in range(10**5 + 5)]
unique_number = 0

ll = -1
rr = -1
j = 0

for index in range(len(arr)):
    if arr_count[arr[index]] == 0:
        unique_number += 1

    arr_count[arr[index]] += 1

    if unique_number == k:
        while True:
            arr_count[arr[j]] -= 1

            if arr_count[arr[j]] == 0:
                ll = j + 1
                rr = index + 1
                break
            j += 1

    if ll != -1 and rr != -1:
        break

print(ll, rr, end=' ')

