from array import array
int_array = array('l',[0]*7)
print(len(int_array))

int_array[0] = 1
int_array[1] = 2
int_array[2] = 3
int_array[3] = 4
int_array[4] = 5
int_array[5] = 6

print(int_array)

print('-'*80)  # horizontal line seperator

found_index = -1 # deafult value before finding an elemt 

for index in range(len(int_array)): # for loop to print
     if int_array[index]==1: # if the element is found 
      found_index = index 
      break 
print(f'the 1 was found at index {found_index}')

print()
print(int_array.itemsize) # size of each item in the array