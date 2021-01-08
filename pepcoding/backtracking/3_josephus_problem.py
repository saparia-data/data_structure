'''
1. You are given two numbers N and K.
2. N represents the total number of soldiers standing in a circle having position marked from 0 
   to N-1.
3. A cruel king wants to execute them but in a different way.
4. He starts executing soldiers from 0th position and proceeds around the circle in clockwise 
   direction.
5. In each step, k-1 soldiers are skipped and the k-th soldier is executed.
6. The elimination proceeds around the circle (which is becoming smaller and smaller as the 
   executed soldiers are removed), until only the last soldier remains, who is given freedom.
7. You have to find the position of that lucky soldier.

Sample Input:

4
2

Sample Output:

0

https://www.youtube.com/watch?v=dzYq5VEMZIg&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=5


'''

def josephus(n, k):
    
    if(n == 1):
        return 0
    
    x = josephus(n - 1, k)
    y = (x + k) % n
    return y

print(josephus(4, 2))