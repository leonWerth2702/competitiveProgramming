def process_input():
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    return n, t, arr


def solve():
    number_of_books, number_of_free_time, time_read_each_books = process_input()

    max_books_can_reads = current_books_can_read = 0
    k = 0

    for index in range(number_of_books):
        while number_of_free_time < time_read_each_books[index]:
            number_of_free_time += time_read_each_books[k]
            current_books_can_read -= 1
            k += 1

        number_of_free_time -= time_read_each_books[index]
        current_books_can_read += 1
        max_books_can_reads = max(current_books_can_read, max_books_can_reads)

    print(max_books_can_reads)


solve()


