from typing import MutableSequence
def selection_sort(data: MutableSequence) -> None:
  """Sorts a mutable sequence in place using the selection sort algorithm."""
    
  for last_unsorted_index in range(len(data) - 1, 0, -1):
       largest = 0
       for i in range(1, last_unsorted_index + 1):
           if data[i] > data[largest]:
               largest = i
       data[largest],data[last_unsorted_index] = data[last_unsorted_index],data[largest] # swap the largest number with the last unsorted number
       #print(f"End of pass: {last_unsorted_index} :'data' is now  {data}") # print the current state of the list after each pass

if __name__ == "__main__":
    from array import array
    numbers = array('i',[5,1,4,2,8]) # create an array of integers
    #print(f"sorting{numbers}")
    #selection_sort(numbers)
    #print(f"sorted {numbers}")