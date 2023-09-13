import itertools
import multiprocessing
import threading


def is_lucky(ticket):
    first_half = ticket[:3]
    second_half = ticket[3:]
    return sum(map(int, first_half)) == sum(map(int, second_half))


def count_lucky_tickets(ticket_length, num_threads):
    total_tickets = 10 ** ticket_length
    tickets_per_thread = total_tickets // num_threads

    def worker(start, end):
        count = 0
        for ticket in range(start, end):
            ticket_str = str(ticket).zfill(ticket_length)
            if is_lucky(ticket_str):
                count += 1
        return count

    results = []
    threads = []

    for i in range(num_threads):
        start = i * tickets_per_thread
        end = (i + 1) * tickets_per_thread if i < num_threads - 1 else total_tickets
        thread = threading.Thread(target=lambda: results.append(worker(start, end)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)


if __name__ == "__main__":
    ticket_length = 6
    num_threads = 4

    if ticket_length % 2 != 0:
        print("Довжина білета повинна бути парним числом (6, 8 або 10).")
    else:
        result = count_lucky_tickets(ticket_length, num_threads)
        print(f"Кількість щасливих білетів з {ticket_length} цифрами: {result}")
