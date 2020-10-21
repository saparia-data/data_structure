'''
Given a matrix of dimension RxC where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges. 
A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
If it is impossible to rot every orange then simply return -1.

Algo:

The idea is to user Breadth First Search. Below is algorithm.

1) Create an empty Q.
2) Find all rotten oranges and enqueue them to Q. Also enqueue a delimiter to indicate beginning of next time frame.
3) While Q is not empty do following
    3.a) Do following while delimiter in Q is not reached
        (i) Dequeue an orange from queue, rot all adjacent oranges. While rotting the adjacent, make sure that time frame is incremented only once. 
        And time frame is not icnremented if there are no adjacent oranges.
    3.b) Dequeue the old delimiter and enqueue a new delimiter. The oranges rotten in previous time frame lie between the two delimiters.
    
https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/

'''
import collections

def orangesRotting(grid):
    
    """
        :type grid: List[List[int]] matrix
        :rtype: int
    """ 
    
    def get_neighbors(coor):
        
        res = []
        x, y = coor
        
        for off_x, off_y in [[1,0], [0,1], [-1,0], [0,-1]]:
                if x + off_x > -1 and  x + off_x < len(grid) and \
                   y + off_y > -1 and  y + off_y < len(grid[0]) and \
                   grid[x+off_x][y+off_y]: res.append((x+off_x,y+off_y))       
        
        return res
    
    fresh_count = 0
    fringe = collections.deque([])
    rotten = set()
    
    for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_count += 1
                    
                if grid[i][j] == 2:
                    fringe.append(((i,j),0))
                    rotten.add((i,j))
                
    
    print(fringe) 
    print(rotten)
    #BFS
    day = 0
    
    while(fringe):
        
        curr, day = fringe.popleft()
        
        for adj in get_neighbors(curr):
            if adj not in rotten:
                fringe.append((adj, day + 1))
                rotten.add(adj)
                fresh_count -= 1
            
    return day if not fresh_count else -1

grid = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
print(orangesRotting(grid))