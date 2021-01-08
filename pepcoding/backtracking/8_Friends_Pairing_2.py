'''
1. You are given an integer n, which represents n friends numbered from 1 to n.
2. Each one can remain single or can pair up with some other friend.
3. You have to print all the configurations in which friends can remain single or can be paired up.

Sample Input:

3

Sample Output:

1.(1) (2) (3) 
2.(1) (2,3) 
3.(1,2) (3) 
4.(1,3) (2) 


https://www.youtube.com/watch?v=qv_1Pstbm-w&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=10

'''
def friendPair(i, n, used, asf):
    
    if(i > n):
        print(asf)
        return
    
    if(used[i] == True):
        friendPair(i+1, n, used, asf)
        
    else:
        used[i] = True
        friendPair(i+1, n, used, asf + "(" + str(i) + ") ")
        j = i+1
        while(j <= n):
            if(used[j] == False):
                used[j] = True
                friendPair(i+1, n, used, asf + "(" + str(i) + str(j) + ") ")
                used[j] = False
            j += 1
            
        used[i] = False





n = 3
used = [False] * (n+1)
friendPair(1, n, used, "")