# python3
# Author: Anthony Silva
# Date: 1/16/2019
# Optimal Car Refueling Problem

# In this algorithm I utilize the greedy algorithm method
# to minimize the number of refuels needed for a given route
# with a length 'd', 'n' gas stops with their distance from
# the origin, and the total mileage 'L' the car can reach on a full tank, 
# assuming we start with a full tank.

def MinRefills(x,n,L):
    # intialize values
    numRefills = 0
    currentRefill = 0

    # run greedy algorithm for optimal refuel
    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n and x[currentRefill+1]-x[lastRefill] <= L):
            currentRefill += 1
        if currentRefill == lastRefill: # case impossible to reach next stop
            print(-1)
            return False
        if currentRefill <= n:
            numRefills += 1
    
    # print minimum number of refills required for route
    print(numRefills)
    return True

d = int(input()) # total length of drive from origin
L = int(input()) # max mileage on full tank
n = int(input()) # number of gas stops on the route
x = [int(x) for x in input().split()] # distance of each gas stop from origin
x.insert(0,0) # insert initial distance from origin
x.append(d) # append distance of destination from origin

MinRefills(x,n,L) # instantiate function
