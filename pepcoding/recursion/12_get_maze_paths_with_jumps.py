'''
1. You are given a number n and a number m representing number of rows and columns in a maze.
2. You are standing in the top-left corner and have to reach the bottom-right corner. 
3. In a single move you are allowed to jump 1 or more steps horizontally (as h1, h2, .. ), 
   or 1 or more steps vertically (as v1, v2, ..) or 1 or more steps diagonally (as d1, d2, ..).
   
   
Sample Input
2
2

Sample Output
[h1v1, v1h1, d1]

https://www.youtube.com/watch?v=VaGBRiSdtFI&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=33

'''
def getMazePathWithJump(sr, sc, dr, dc):
    
    if(sr == dr and dc == sc):
        bres = []
        bres.append("")
        return bres
    
    if(sr > dr or dr > dc):
        bres = []
        return []
    
    paths = []
    
    # horizontal moves        
    hm = 1
    while(hm <= dc - sc):
        hpaths = getMazePathWithJump(sr, sc + hm, dr, dc)
        for p in hpaths:
            paths.append("h" + str(hm) + p)
            
        hm += 1
    
    
    # vertical moves
    vm = 1
    while(vm <= dr - sr):
        vpaths = getMazePathWithJump(sr+vm, sc, dr, dc)
        for p in vpaths:
            paths.append("v" + str(vm) + p)
            
        vm += 1

        
    #diagonal moves
    dm = 1
    while(dm <= dr-sr and dm <= dc-sc):
        dpaths = getMazePathWithJump(sr+dm, sc+dm, dr, dc)
        for p in dpaths:
            paths.append("d" + str(dm) + p)
        
        dm += 1 
    
    
       
    return paths
    
    
print(getMazePathWithJump(1, 1, 2, 2))