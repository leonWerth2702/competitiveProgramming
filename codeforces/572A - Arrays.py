n_a, n_b = map(int, input().split())
k, m = map(int, input().split())

m *= -1
k -= 1
result = 'YES'

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a[k] >= b[m]:
    result = 'NO'

print(result)

