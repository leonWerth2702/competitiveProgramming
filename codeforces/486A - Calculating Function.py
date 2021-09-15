n = int(input())
number_of_odd = 0
number_of_even = 0
num = n // 2
if n % 2 == 0:
    number_of_odd = 0 - num ** 2
else:
    number_of_odd = 0 - (num + 1) ** 2
number_of_even = num * (num + 1)
total = number_of_even + number_of_odd
print(total)


