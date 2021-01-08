'''
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a gold mine.
4. You are allowed to take one step left, right, up or down from your current position.
5. You can't visit a cell with 0 gold and the same cell more than once. 
6. Each cell has a value that is the amount of gold available in the cell.
7. You are required to identify the maximum amount of gold that can be dug out from the mine if 
   you start and stop collecting gold from any position in the grid that has some gold.
   
   
Sample Input:

6
6

0 1 4 2 8 2
4 3 6 5 0 4
1 2 4 1 4 6
2 0 7 3 2 2
3 1 5 9 2 4
2 7 0 8 5 1

Sample Output:

120

https://www.youtube.com/watch?v=lNwXq3Ki32I&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=7


'''

def travelAndCollect(arr, i, j, visited, bag):
    
    if(i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]) or arr[i][j] == 0 or visited[i][j] == True):
        return
    
    visited[i][j] = True
    bag.append(arr[i][j])
    travelAndCollect(arr, i-1, j, visited, bag) # call for north
    travelAndCollect(arr, i, j+1, visited, bag) # call for east
    travelAndCollect(arr, i+1, j, visited, bag) # call for south
    travelAndCollect(arr, i, j-1, visited, bag) # call for west
    
    
def getMaxGold(arr):
    
    maxx = 0
    
    visited = [[False for j in range(len(arr))] for i in range(len(arr))]
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(visited[i][j] == False and arr[i][j] != 0):
                bag = []
                travelAndCollect(arr, i, j, visited, bag)
            
                # take count of all visited cells
                summ = 0
                for val in bag:
                    summ += val

                if(summ > maxx):
                    maxx = summ
                    
    return maxx

arr = [                
        [0, 1, 4, 2, 8, 2],
        [4, 3, 6, 5, 0, 4],
        [1, 2, 4, 1, 4, 6],
        [2, 0, 7, 3, 2, 2],
        [3, 1, 5, 9, 2, 4],
        [2, 7, 0, 8, 5, 1]
    ]

print(getMaxGold(arr))