from array import *

array1 = array('i',[1,2,3,4,5,6])

def searchInArray(array, number):
    for i in array:                                 # O(n)
        if i == number:                             # O(1)
            return array.index(number)              # O(1)
    return "The element is not in an array"         # O(1)

print(searchInArray(array1,3))

print(searchInArray(array1,9))


# Time Complecity O(n)
# Space Complecity O(1)
