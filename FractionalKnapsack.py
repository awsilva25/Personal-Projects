# python3
# Author: Anthony Silva
# Date: 1/12/2020
# Fractional Knapsack Problem

# Import NumPy
import numpy as np

# Input: The first line of the input contains 
# the number of items, and the capacity of a knapsack.
# The next lines contain the value and weight of items.
Input = [int(x) for x in input().split()] 
    
def FractionalKnapsack(Input):
    
    # Numer of items for input
    Count = Input[0]

    # Max capacity
    MaxWeight = Input[1]

    # Initialize Container to store input
    Container = [[0,0]]*Count

    # Initialize array for value per unit
    ValuePerUnit = [0]*Count

    # Initialize array to store weights of each item
    Weights = [0]*Count

    # Initialize array for sorted ValuePerUnit
    SortedValues = [0]*Count

    # Grab input and calculate ValuePerUnit
    for i in range(Count):
        Input = input()
        Container[i] = [int(x) for x in Input.split()]
        ValuePerUnit[i] = Container[i][0]/Container[i][1] # value per unit
        Weights[i] = Container[i][1]

    # Sort values in ValuePerUnit by index in descending order
    SortedValues = sorted(ValuePerUnit,reverse=True)

    # Argsort ValuePerUnit and sort Weights according to the descending values
    ArgSortedWeight = list(np.array(ValuePerUnit).argsort())[::-1]
    Weights = [Weights[i] for i in ArgSortedWeight]

    # Initialize values
    TotalWeight = 0
    TotalValue = 0
    TempSum = 0
    idx = 0

    # Apply greedy algorithm to data
    while TotalWeight < MaxWeight:    
        if TempSum < Weights[idx]:
            TotalWeight += 1
            TempSum += 1
            TotalValue += SortedValues[idx]
            continue
        TempSum = 0
        if idx==Count-1:
            break
        idx += 1
        
    # Max possible value    
    print(TotalValue)

FractionalKnapsack(Input)
