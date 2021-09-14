number_of_rooms = int(input())
count = 0

for i in range(number_of_rooms):
    number_of_people, room_capacity = map(int, input().split())
    if room_capacity - number_of_people >= 2:
        count += 1

print(count)

