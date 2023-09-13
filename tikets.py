import itertools
import multiprocessing


def is_lucky(ticket):
    first_half = ticket[:3]
    second_half = ticket[3:]
    return sum(map(int, first_half)) == sum(map(int, second_half))


def generate_tickets(length):
    digits = '0123456789'
    return [''.join(p) for p in itertools.product(digits, repeat=length)]


def count_lucky_tickets(start, end, tickets):
    count = 0
    for i in range(start, end):
        if is_lucky(tickets[i]):
            count += 1
    return count


def main():
    ticket_length = 6
    num_processes = 4

    tickets = generate_tickets(ticket_length)
    chunk_size = len(tickets) // num_processes

    pool = multiprocessing.Pool(processes=num_processes)
    results = []

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else len(tickets)
        result = pool.apply_async(count_lucky_tickets, (start, end, tickets))
        results.append(result)

    pool.close()
    pool.join()

    total_lucky_tickets = sum(result.get() for result in results)
    print(f"Загальна кількість щасливих білетів: {total_lucky_tickets}")


if __name__ == '__main__':
    main()
