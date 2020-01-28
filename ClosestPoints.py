# python3
# Author: Anthony Silva
# Date: 1/26/2020
# Closest Points Using Divide & Conquer

# In this project I implement an optimized divide and
# conquer algorithm to find the closest pair(s) of "n" points
# in O(nlog(n)) time, given their (x, y) coordinates.

from math import sqrt

# sort points according to their x coordinate and pass to MinDistance function
def MinDistSort(x,y):
    Points = list(zip(x,y))
    Points = sorted(Points, key=lambda x: x[0])
    return sqrt(MinDistance(Points))

# calculate minimum distance using divide and conquer  
def MinDistance(Points):
    N = len(Points)

    if N <= 3:
        x, y = [list(i) for i in zip(*Points)]
        return MinDistForce(x, y)
    
    # find median index to partition points into two roughly equal parts
    m = N // 2

    # calculate min distance for left and right partitions
    d1 = MinDistance(Points[:m])
    d2 = MinDistance(Points[m:])

    # calculate minimum of minimum distance of each partition
    d12 = min(d1,d2)

    # find all points within distance d12 of the middle line
    PointsMid = [p for p in Points if abs(Points[m][0]-p[0]) < d12]

    d = CheckMidLine(PointsMid, d12)
    return d

# check if any points in middle strip have distance less than d12
def CheckMidLine(Points, d):
    MinDist = d
    N = len(Points)

    # sort points in middle strip according to their y coordinate
    Points = sorted(Points, key=lambda x: x[1])

    # calculate min distance b/w points in middle strip
    for i in range(N-1):
        p1 = Points[i]
        for j in range(i+1, min(i+9, N)):
            p2 = Points[j]
            Dist = (p1[0]-p2[0])**2 + (p1[1] - p2[1])**2

            if Dist < MinDist:
                MinDist = Dist
    return MinDist

# calculate min distance between less than 4 points
def MinDistForce(x, y):
    Points = list(zip(x,y))
    MinDist = 10**18

    # calculate min distance b/w points
    for i in range(len(Points)-1):
        p1 = Points[i]
        for j in range(i+1, len(Points)):
            p2 = Points[j]
            Dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

            if Dist < MinDist:
                MinDist = Dist
    return MinDist

# main function
n = int(input()) # total number of points to consider
Coords = [[0,0]]*n # initialize array for (x,y) coordinates of each point

# input 'n' points
for i in range(n): 
        Coord = [int(x) for x in input().split()]
        Coords[i] = Coord
x = [item[0] for item in Coords]
y = [item[1] for item in Coords]

# call function and print result
print('{0:.9f}'.format(MinDistSort(x,y)))
