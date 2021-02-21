'''
1. You are given a number M representing length of highway(range).
2. You are given a number N representing number of bill boards.
3. You are given N space separated numbers representing (P)position of bill-boards.
4. You are given N space separated numbers representing (R)revenue corresponding to each (P)position.
5. You are given a number T such that bill-boards can only be placed after specific distance(T).
6. Find the maximum revenue that can be generated.

Input Format:

A number M(length of highway)
A number N(number of bill boards)
P1 ,P2 ,P3 ,P4 ,P5 .... Pn (placement of N bill-boards)
R1 ,R2 ,R3 ,R4 ,R5 .... Rn (revenue from each bill-board)
A number T (neccessary distance b/w two bill-board)


Sample Input:

20

5

6 7 12 14 15

5 8 5 3 1

5

Sample Output

11


https://www.youtube.com/watch?v=SiGqwJOvflE&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=36


'''

def solution(miles, nobb, pobb, robb, t):
    
    map = {}
    
    for i in range(nobb):
        map[pobb[i]] = robb[i]
        
    #print(map) {6: 5, 7: 8, 12: 5, 14: 3, 15: 1}
    
    dp = [False] * (miles+1)
    dp[0] = 0
    
    for i in range(1, miles+1):
        
        if(i not in map.keys()):
            dp[i] = dp[i-1]
        else:
            boardNotInstalled = dp[i-1]
            boardInstalled = map.get(i)
            if(i >= t+1):
                boardInstalled += dp[i-t-1]
                
            dp[i] = max(boardNotInstalled, boardInstalled)
            
    return dp[miles]



if __name__ == "__main__":
    
    miles = 20
    nobb = 5 # number of bill board
    pobb = [6, 7, 12, 14, 15] # position of bill board
    robb = [5, 8, 5, 3, 1] # revenue of bill board
    t = 5
    
    print(solution(miles, nobb, pobb, robb, t))
    