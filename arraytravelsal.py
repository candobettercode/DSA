from array import *

array1 = array('i',[1,2,3,4,5,6])

array2 = array('d',[1.3,1,5.1,6])


def traverseArray(array):
    for i in array:         # O(n)
        print(i)            # O(1)

traverseArray(array1)

print('Second Array')

traverseArray(array2)

# Time Complexity - O(n)
# Space Complexity - O(1)
