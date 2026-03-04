from typing import MutableSequence

def bubble_sort(data: MutableSequence) -> None:

    n = len(data)

    for sorted_partition in range(n - 1, 0, -1):

        swapped = False

        for i in range(sorted_partition):

            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True

        print(f"End of pass {n - sorted_partition}: data is now {data}")

        if not swapped:
            break


if __name__ == "__main__":

    numbers = [8, 1, 2, 3, 4, 5, 6, 7]

    print("Starting data:", numbers)

    bubble_sort(numbers)

    print("The sorted data is", numbers)