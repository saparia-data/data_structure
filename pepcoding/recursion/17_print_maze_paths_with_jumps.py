'''
1. You are given a number n and a number m representing number of rows and columns in a maze.
2. You are standing in the top-left corner and have to reach the bottom-right corner. 
3. In a single move you are allowed to jump 1 or more steps horizontally (as h1, h2, .. ), 
   or 1 or more steps vertically (as v1, v2, ..) or 1 or more steps diagonally (as d1, d2, ..).
   
   
Sample Input

3
3

Sample Output

h1h1v1v1
h1h1v2
h1v1h1v1
h1v1v1h1
h1v1d1
h1v2h1
h1d1v1
h2v1v1
h2v2
v1h1h1v1
v1h1v1h1
v1h1d1
v1h2v1
v1v1h1h1
v1v1h2
v1d1h1
v2h1h1
v2h2
d1h1v1
d1v1h1
d1d1
d2
 

https://www.youtube.com/watch?v=zri_tftYphE&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=41

'''

def printMazePathsWithJump(sr, sc, dr, dc, psf):
    
    if(sr == dr and sc == dc):
        print(psf)
        return
    
    # horizontal move
    hm = 1
    while(hm <= dc - sc):
        printMazePathsWithJump(sr, sc + hm, dr, dc, psf + "h" + str(hm))
        hm += 1

    # vertical move
    vm = 1
    while(vm <= dr - sr):
        printMazePathsWithJump(sr + vm, sc, dr, dc, psf + "v" + str(vm))
        vm += 1
        
    # diagonal move
    dm = 1
    while(dm <= dr - sr and dm <= dc - sc):
        printMazePathsWithJump(sr + dm, sc + dm, dr, dc, psf + "d" + str(dm))
        dm += 1
        
        
printMazePathsWithJump(1, 1, 3, 3, "")