number_of_friends = int(input())
friends_give_gifts = list(map(int, input().split()))

for i in range(1, number_of_friends + 1):
    print(friends_give_gifts.index(i) + 1, end=' ')

