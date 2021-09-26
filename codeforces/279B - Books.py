def process_input():
    n, t = map(int, input().split())
    time_for_reads = list(map(int, input().split()))

    return n, t, time_for_reads


def solve():
    number_of_books, number_of_times, time_for_reads = process_input()

    max_books_can_read = 0
    k = 0
    current_books_can_read = 0
    time_read_books = 0

    for index in range(number_of_books):
        time_read_books += time_for_reads[index]
        current_books_can_read += 1

        while time_read_books > number_of_times:
            current_books_can_read -= 1

            if k >= number_of_books:
                break

            time_read_books -= time_for_reads[k]
            k += 1

        max_books_can_read = max(current_books_can_read, max_books_can_read)

    print(max_books_can_read)


solve()

