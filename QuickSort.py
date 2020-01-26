# python3
# Author: Anthony Silva
# Date: 01/20/2020

# In this algorithm, I implement Randomized QuickSort with a 3-way partition
# The first partition contains all elements less than the pivot
# The second partition contains all elements equal to the pivot
# The third partition contains all elements greater than the pivot

import random

def Partition(a, l, r):
    pivot, j, k = a[l], l, r
    i = j 
    while i <= k: 
        if a[i] < pivot: 
            a[i], a[j] = a[j], a[i] # swap values
            j += 1 # shift index in left partition one right 
        elif a[i] > pivot: 
            a[i], a[k] = a[k], a[i] # swap values 
            k -= 1 # shift index in right partition one left
            i -= 1 # keep i in place
        i += 1
    return j, k # return first index and last index of middle partition with equal values to pivot

def RandomizedQuickSort(a, l, r):
    if l >= r: # solution found
        return
    k = random.randint(l,r) # select a random index from subarray
    a[l], a[k] = a[k], a[l] # swap left most value in array and random value
    m1, m2 = Partition(a, l, r) # get equal values in their final position and return indexes
    RandomizedQuickSort(a, l, m1-1); # sort left partition subarray
    RandomizedQuickSort(a, m2+1, r); # sort right partition subarray

n = int(input()) # total number of values in original array
values = [int(x) for x in input().split()] # elements in original array
RandomizedQuickSort(values,0,n-1) # run randomized quicksort algorithm for array
for x in values: # print results
    print(x, end=' ')

