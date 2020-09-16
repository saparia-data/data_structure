'''
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a fixed direction.​
The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the circle, 
you are the last one remaining and survive.

Input Format:
The first line of input contains an integer T denoting the number of test cases . Then T test cases follow. Each test case contains 2 integers n and k .

Output Format:
For each test case, in a new line, output will be the safe position which satisfies the above condition.

Your Task:
This is a function problem. You are required to complete the function josephus that takes two parameters n and k and returns an integer denoting safe position .

Constraints:
1 <= T <= 100
1 <= k, n <= 20

Example:
Input:
2
3 2
5 3
Output
3
4

Explanation:
Testcase 1: There are 3 persons so skipping 1 person i.e 1st person 2nd person will be killed. Thus the safe position is 3.

Hints:
1) The problem has following recursive structure.

  josephus(n, k) = (josephus(n - 1, k) + k-1) % n + 1
  josephus(1, k) = 1
  
After the first person (kth from begining) is killed, n-1 persons are left. So we call josephus(n – 1, k) 
to get the position with n-1 persons. But the position returned by josephus(n – 1, k) will consider the position starting from k%n + 1. 
So, we must make adjustments to the position returned by josephus(n – 1, k).

def josephus(n,k):
'''
def josephus(n,k):
    
    if(n == 1):
        return 1
    else:
        jos_ans = josephus(n - 1, k)
        jj = (jos_ans+ k - 1) % n + 1
        #print(jj)
        return jj
    
print(josephus(7, 3))
    
    
    
    
    
    
    
    
    
    
