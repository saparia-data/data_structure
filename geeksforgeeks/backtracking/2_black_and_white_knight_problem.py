'''
Given the chessboard dimensions. Find out the number of ways we can place a black and a white Knight on this chessboard 
such that they cannot attack each other.

Note:
The knights have to be placed on different squares. 
A knight can move two squares horizontally and one square vertically (L shaped), or two squares vertically and one square horizontally (L shaped). 
The knights attack each other if one can reach the other in one move.

Example 1:
Input:
N = 2,M = 2
Output: 12 

Example 2:
Input:
N = 2,M = 3
Output: 16


'''
def solve(m,n):
    '''
    :param m: number of rows
    :param n: number of columns
    :return: total possibilities
    '''
    # specifying the directions to check in i.e 8 directions
    x_off = [-2,-2,-1, 1, 2, 2, 1, -1]
    y_off = [-1, 1, 2, 2, 1,-1, -2, -2]
    MOD = 1000000007

    # variable to maintain number of positions which are not feasible
    ret = 0

    # iterating for complete matrix
    for i in range(m):
        for j in range(n):
            for k in range(8):
                x = i + x_off[k]
                y = j + y_off[k]
                # checking if the attack position is within bounds
                if x>=0 and x<m and y>=0 and y<n :
                    # if in bounds it is not feasible, increment it
                    ret+=1

    # total possible combinations of 2 knights
    total = ((m * n) * (m * n - 1)) % MOD 
    # returning total feasible combinations
    return (total - ret) % MOD 

m = 3
n = 2
print(solve(m, n))