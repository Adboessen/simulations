def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
# Driver code to test above
arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [63,34,25,12,22,11]
arr3 = [-64,34,25]
arr4 = []
 
bubbleSort(arr1)
bubbleSort(arr2)
bubbleSort(arr3)
bubbleSort(arr4)
print ("Sorted array is:")
for i in range(len(arr1)):
    print ("%d" %arr1[i]), 

print ("Sorted array is:")
for i in range(len(arr2)):
    print ("%d" %arr2[i]),

print ("Sorted array is:")
for i in range(len(arr3)):
    print ("%d" %arr3[i]),

print ("Sorted array is:")
for i in range(len(arr4)):
    print ("%d" %arr4[i]), 
