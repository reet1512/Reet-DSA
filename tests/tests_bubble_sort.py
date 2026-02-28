import unittest # 1-3 import tools unnitest
from array import array # we want to create array
from Arrays.bubble_sort import bubble_sort as sort_function #sorting function


class TestSort(unittest.TestCase): #inheritance 
    def test_array(self): # test function to test the sorting function , unnitest tests everything starting with test
        test_data = array('i',[5,1,4,2,8])
        result = array('i',[1,2,4,5,8])
        sort_function(test_data) # call function
        self.assertEqual(test_data,result) #Check if test_data equals result.
        
if __name__ == "__main__":
 unittest.main() #This runs all test methods when file is executed directly.