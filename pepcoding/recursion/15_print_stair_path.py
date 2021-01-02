'''
1. You are given a number n representing number of stairs in a staircase.
2. You are standing at the bottom of staircase. You are allowed to climb 1 step, 2 steps or 3 steps in one move.

Sample Input
3

Sample Output
111
12
21
3

https://www.youtube.com/watch?v=NEuYcztalew&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=37

'''

def printStairPath(n, path):
    
    if(n == 0):
        print(path)
        return
    
    if(n < 0):
        return
    
    printStairPath(n-1, path + "1")
    printStairPath(n-2, path + "2")
    printStairPath(n-3, path + "3")
    
printStairPath(4, "")