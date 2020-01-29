# python3
# Author: Anthony Silva
# Date: 1/28/2020
# Majority Element

# In this algorithm I check whether a list contains a majority element.
# that is more than n/2 repeated elements, where n is the length of the list.
# Total time used is O(nlog(n))+O(n)

import random

# check whether a list contains a majority element
def MajorityElement(a,n):
    if n==1:
        return 1
    a = sorted(a)
    count = 1
    idx = 0
    for i in range(1,n):
        if a[idx] == a[i]:
            count+=1
            if count > n/2:
                return 1
            continue
        else:
            idx += count
            count = 1
    return 0

# test the MajorityElement function for random input
def StressTest():
    n = random.randint(1,10)
    randoms = []
    for i in range(n):
        randoms.append(random.randint(-1,1))
    print(n)
    print(sorted(randoms))
    print(MajorityElement(randoms))

if __name__=='__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    print(MajorityElement(a,n))
