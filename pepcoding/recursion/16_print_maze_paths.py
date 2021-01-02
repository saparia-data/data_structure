'''
1. You are given a number n and a number m representing number of rows and columns in a maze.
2. You are standing in the top-left corner and have to reach the bottom-right corner. 
   Only two moves are allowed 'h' (1-step horizontal) and 'v' (1-step vertical).
   
Sample Input
2
2

Sample Output
hv
vh

https://www.youtube.com/watch?v=MHtAA5UE-6Y&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=39

'''

def printMazePath(sr, sc, dr, dc, psf):
    
    if(sr > dr or sc > dc):
        return
    
    if(sr == dr and sc == dc):
        #print path so far
        print(psf)
        return
    
    # horizontal move
    printMazePath(sr, sc+1, dr, dc, psf + "h")
    
    # vertical move
    printMazePath(sr+1, sc, dr, dc, psf + "v")
    
printMazePath(1, 1, 2, 2, "")
    