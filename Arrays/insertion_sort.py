from typing import MutableSequence

def insertion_sort(data: MutableSequence) -> None:
    """Sorts a mutable sequence in place using the insertion sort algorithm."""
    
    for first_unsorted_index in range(1, len(data)):
        new_element = data[first_unsorted_index]

        i = first_unsorted_index
        while i>0 and data[i-1] > new_element:
            data[i+1]=data[i]
            i -= 1