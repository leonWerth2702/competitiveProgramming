number_of_peoples = int(input())
response_of_peoples = list(map(int, input().split()))
if response_of_peoples.count(1) > 0:
    print('hard')
else:
    print('easy')

