'''
1. You are given a number.
2. You have to print all the numbers from 1 to n in lexicographical order.

Sample Input:

14

Sample Output:

1
10
11
12
13
14
2
3
4
5
6
7
8
9


https://www.youtube.com/watch?v=gRo86WqFYSE&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=6


'''

def lexicographicalOrder(curr, n):
    
    if(curr > n):
        return
    
    print(curr)
    
    for j in range(n+1):
        lexicographicalOrder(10 * curr + j, n)
        
for i in range(1, 10):
    lexicographicalOrder(i, 14)