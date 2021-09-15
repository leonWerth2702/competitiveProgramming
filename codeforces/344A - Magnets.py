number_of_magnets = int(input())
current_magnet = ''
number_of_groups = 0
for i in range(number_of_magnets):
    magnet = input()
    if magnet != current_magnet:
        number_of_groups += 1
        current_magnet = magnet

print(number_of_groups)

