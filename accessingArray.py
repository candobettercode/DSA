from array import *

array1 = array('i',[1,2,3,4,5,6])

array2 = array('d',[1.3,1,5.1,6])

def accessElement(array, index):
    if index >= len(array):             #O(1)
        print('There is no number at this index')       #O(1)
    else:
        print(array1[index])            #O(1)

accessElement(array1,3)

accessElement(array1,7)

# Time Complexity O(1)
# Space Complexity O(1)


