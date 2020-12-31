'''
1. You are given a number n representing number of stairs in a staircase.
2. You are standing at the bottom of staircase. You are allowed to climb 1 step, 2 steps or 3 steps in one move.
3. Complete the body of getStairPaths function - without changing signature - 
   to get the list of all paths that can be used to climb the staircase up.


Sample Input
3

Sample Output
[111, 12, 21, 3]

https://www.youtube.com/watch?v=hMJAlbJIS7E&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=29

'''

def getStairsPath(n):
    
    if(n == 0):
        bres = []
        bres.append("")
        return bres
    
    elif(n < 0):
        bres = []
        return bres

    paths1 = getStairsPath(n-1)
    paths2 = getStairsPath(n-2)
    paths3 = getStairsPath(n-3)
    
    paths = []
    
    for p in paths1:
        paths.append("1" + str(p))
        
    for p in paths2:
        paths.append("2" + str(p))
        
    for p in paths3:
        paths.append("3" + str(p))
        
    return paths


print(getStairsPath(4))
        