'''
1. You are given a number n and a number m representing number of rows and columns in a maze.
2. You are standing in the top-left corner and have to reach the bottom-right corner. 
   Only two moves are allowed 'h' (1-step horizontal) and 'v' (1-step vertical).
   
Sample Input
3
3

Sample Output
[hhvv, hvhv, hvvh, vhhv, vhvh, vvhh]

https://www.youtube.com/watch?v=7i41gZLXe5k&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=31

'''

def getmazePaths(sr, sc, dr, dc):
    
    if(sr == dr and sc == dc):
        bres = []
        bres.append("")
        return bres
    
    vpaths = []
    hpaths = []
    
    # if source row is less than destination row, then we can move in vertical direction
    if(sr < dr):
        vpaths = getmazePaths(sr+1, sc, dr, dc)
    
    # if source column is less than destination column, then we can move in horizontal direction    
    if(sc < dc):
        hpaths = getmazePaths(sr, sc+1, dr, dc)
        
    paths = []
    
    for path in hpaths:
        paths.append("h" + path)
    
    for path in vpaths:
        paths.append("v" + path)
        
        
    return paths


print(getmazePaths(1, 1, 3, 3))
        