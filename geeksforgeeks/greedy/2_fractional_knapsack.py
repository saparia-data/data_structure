'''
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 

Example 1:
Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output: 240.00
Explanation: Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 

Example 2:
Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output: 160.00
Explanation: Total maximum value of item
we can have is 160.00 from the given
capacity of sack.

https://www.geeksforgeeks.org/fractional-knapsack-problem/

'''

def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    '''

    curr_weight = 0 # initialize current weight put in
    curr_value = 0  # total value achieved till now

    # sort the Items according to value/weight, in descending order
    Items = sorted(Items, key = lambda x: (x.value/x.weight), reverse= True)

    # iterate through Items and update result, break when sack is full'
    for i in range(n):
        if curr_weight+Items[i].weight <= W: # this can be completely accommodated in sack.
            curr_weight += Items[i].weight
            curr_value += Items[i].value # update value
        else:
            # partial can be accommodated , after which sack will be full
            accomodate = W-curr_weight # weight which can be taken
            value_added = Items[i].value *(accomodate/Items[i].weight) # partial value added in knapsack
            curr_value += value_added
            break # sack is full

    return curr_value