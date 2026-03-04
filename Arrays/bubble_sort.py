from typing import MutableSequence # mutable sequency is a list or array whose value can change 

def bubble_sort(data: MutableSequence) -> None:
     # function that sorts a  mutable sequence and returns nothing
     for sorted_partition in range(len(data)-1,0,-1):
        for i in range(sorted_partition):
            if data[i] > data[i+1]:
                data[i],data[i+1] = data[i+1],data[i] #number swap if the current number is greater than the next number 
            
        #print(f"End of pass : {sorted_partition} :'data' is now  {data}") # print the current state of the list after each pass

if __name__ == "__main__":
    from array import array
    numbers = array('i',[5,1,4,2,8]) # create an array of integers
    print(f"sorting{numbers}")
    bubble_sort(numbers)
    print(f"sorted {numbers}")