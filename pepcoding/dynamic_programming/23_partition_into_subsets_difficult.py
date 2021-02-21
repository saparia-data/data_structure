'''
1. You are given a number n, representing the number of elements.
2. You are given a number k, representing the number of subsets.
3. You are required to print the number of ways in which these elements can be partitioned in k non-empty subsets.

E.g.
For n = 4 and k = 3 total ways is 6
12-3-4
1-23-4
13-2-4
14-2-3
1-24-3
1-2-34


Sample Input:

4
3

Sample Output:

6


https://www.youtube.com/watch?v=IiAsqfjhZnY&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=29&t=5s


'''

def solution(people, teams):
    
    if(people == 0 or people < teams or teams == 0):
        return 0
    
    dp = [[0 for j in range(people+1)] for i in range(teams+1)]
    #print(dp)
    
    for t in range(1, teams+1): # t -> teams
        
        for p in range(1, people+1): # p -> people
            
            if(p < t):
                dp[t][p] = 0
            elif(p == t):
                dp[t][p] = 1
            else:
                dp[t][p] = dp[t-1][p-1] + dp[t][p-1] * t
                
    #print(dp)
    return dp[teams][people]
            
            



if __name__ == "__main__":
    
    people = 4
    teams = 3
    print(solution(people, teams))