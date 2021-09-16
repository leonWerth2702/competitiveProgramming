number_of_layers = int(input())
result = ''

for i in range(number_of_layers):
    if i % 2 == 0:
        result += 'I hate'
    else:
        result += 'I love'
    if i == number_of_layers - 1:
        result += ' it'
    else:
        result += ' that '

print(result)

