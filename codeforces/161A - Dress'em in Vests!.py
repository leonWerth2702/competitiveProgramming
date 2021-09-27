def process_input():
    n, m, x, y = map(int, input().split())
    return n, m, x, y


def process_input2():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    return arr1, arr2


def solve():
    number_of_soldiers, number_of_vests, x, y = process_input()
    desired_sizes_of_vests, sizes_available_of_vests = process_input2()
    i = 0
    k = 0

    soldiers_equipped_bulletproof = 0
    array_result = []

    while i < number_of_soldiers and k < number_of_vests:
        min_size_desired = desired_sizes_of_vests[i] - x
        max_size_desired = desired_sizes_of_vests[i] + y

        size_available = sizes_available_of_vests[k]

        if min_size_desired <= size_available <= max_size_desired:
            soldiers_equipped_bulletproof += 1
            array_result.append(f'{i + 1} {k + 1}')
            i += 1
            k += 1
        elif size_available < min_size_desired:
            k += 1
        elif size_available > max_size_desired:
            i += 1

    print(soldiers_equipped_bulletproof)
    for result in array_result:
        print(result)


solve()


