'''
1. You are given a number n and a number k in separate lines, representing the number of fences and number of colors.
2. You are required to calculate and print the number of ways in which the fences could be painted 
   so that not more than two CONSECUTIVE fences have same colors.
   
Input Format:

A number n
A number k


Sample Input:

8
3

Sample Output:

3672


https://www.youtube.com/watch?v=ju8vrEAsa3Q&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=25


'''

def paintFences(n, k):
    
    #calculate upto 2 fences
    same = k * 1
    diff = k * (k - 1)
    total = same + diff
    
    for i in range(3, n + 1): # start calculating from 3rd fence
        
        same = diff * 1
        diff = total * (k - 1)
        total = same + diff
        
    return total


if __name__ == "__main__":
    
    n = 8 # number of fences
    k = 3 # number of colours (blue, green, red)
    
    print(paintFences(n, k))