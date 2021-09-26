def process_input():
    n, m = map(int, input().split())
    return n, m


def process_input2():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    return arr1, arr2


def solve():
    number_of_problems, number_of_problems_by_george = process_input()
    complexity_problems, complexity_problems_by_george = process_input2()

    problems_need_prepare = number_of_problems
    i = number_of_problems - 1
    j = number_of_problems_by_george - 1

    while i >= 0 and j >= 0:
        if complexity_problems[i] <= complexity_problems_by_george[j]:
            problems_need_prepare -= 1
            j -= 1
        i -= 1

    print(problems_need_prepare)


solve()


