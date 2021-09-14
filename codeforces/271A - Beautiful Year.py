years = input()

while True:
    is_distinct = True
    years = str(int(years) + 1)
    digits = list(years)
    for digit in digits:
        if digits.count(digit) > 1:
            is_distinct = False
            break
    if is_distinct:
        print(years)
        break

