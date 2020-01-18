# python3
# Author: Anthony Silva
# Date: 1/17/2020
# Binary search algorithm

# In this program, I devise a simple binary search algorithm.
# The input, A, is list of integers inputted by the user in 
# monotonic, non-decreasing order.
# The input, B, is also a list of integers provided by the user
# in any order.
# Each element in the list B is searched for in the list A,
# returning the index of the value in A if found.
# If the value in B is NOT found in A, return -1.


# Function takes A, first and last index of A, and value to search for as args
def BinarySearch(A,low,high,key):
   
    # case value is not found in A
    if high < low:
        return -1

    # calculate middle index of list, take int()
    mid = int(low+((high-low)/2))

    # case value is found in list
    if key==A[mid]:
        return mid # return index
    
    # case key value is less than middle element of list, ignore upper half
    elif key<A[mid]:
        return BinarySearch(A,low,mid-1,key)
    
    # case key value is greater than middle element of list, ignore lower half
    else: 
        return BinarySearch(A,mid+1,high,key)

A = [int(x) for x in input().split()] # sorted input list
B = [int(x) for x in input().split()] # input list of values to search for in A
results = [0]*(len(B)) # initialize results array

# run BinarySearch function for each element in B
for i in range(len(B)):
    results[i] = BinarySearch(A,0,len(A)-1,B[i]) 

# print results    
print(" ".join(map(str,results)))
