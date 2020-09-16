'''
You are in a party of N people, where only one person is known to everyone. Such a person may be present in the party, 
if yes, (s)he doesn't know anyone in the party. Your task is to find the stranger (celebrity) in party.

Input:
The first line of input contains an element T denoting the number of test cases. Then T test cases follow. 
Each test case consist of 2 lines. The first line of each test case contains a number denoting the size of the matrix M. 
Then in the next line are space separated values of the matrix M.

Output:
For each test case output will be the id of the celebrity if present (0 based index). Else -1 will be printed.

User Task:
You will be given a square matrix M[][] where if an element of row i and column j  is set to 1 it means ith person knows jth person. 
You need to complete the function getId() which finds the id of the celebrity if present else return -1. 
The function getId() takes two arguments, the square matrix M and its size N.

Note: 
M[i][i] will be equal to zero always.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 50
2 <= N <= 501
0 <= M[][] <= 1

Example:
Input :
2
3
0 1 0 0 0 0 0 1 0
2
0 1 1 0
Output :
1
-1

Explanation :

Testcase 1:
For the above test case the matrix will look like
0 1 0 
0 0 0
0 1 0
Here,  the celebrity is the person with index 1 ie id 1

Testcase 2:
The matrix will look like
0 1
1 0
Here, there is no such person who is a celebrity (a celebrity should know no one).

hints:

1)
Use the following observation based on elimination technique 
-If A knows B, then A can't be celebrity. Discard A, and B may be celebrity.
-If A doesn't know B, then B can't be celebrity. Discard B, and A may be celebrity.
-Repeat above two steps till we left with only one person.
-Ensure the remained person is celebrity.

2)
Use stack to verity celebrity.
-Push all the celebrities into a stack.
-Pop off top two persons from the stack, discard one person based on return status of Mat(A, B).
-Push the remained person onto stack.
-Repeat step 2 and 3 until only one person remains in the stack.
-Check the remained person in stack doesn't have acquaintance with anyone else or not.

https://www.youtube.com/watch?v=LtGnA5L6LIk

https://www.youtube.com/watch?v=LZJBZEnoYLQ

'''

def getId(m,n):
    
    # assume all the indexes can be celebrities
    stack = [i for i in range(n)]
    
    # while more than one person is left in the stack
    while(len(stack) > 1):
        
        # get two persons from the stack
        person_A = stack.pop()
        person_B = stack.pop()
        
        # if A knows B and B knows A.. Both can't be celebs.
        if (m[person_A][person_B] == 1 and m[person_B][person_A] == 1) :
            continue

        # if A knows B .. A can't be celeb
        elif m[person_A][person_B] == 1:
            # discard A and put B again in stack.
            stack.append(person_B)

        # if B knows A .. B can't be celeb
        elif m[person_B][person_A] == 1:
            # discard A and put B again in stack.
            stack.append(person_A)

        # 4th case is not possible as only one celebrity is there
    if len(stack) == 0:
        # no celebrity is there
        return -1
    else:
        possible_celeb = stack.pop()
        # we have to verify if the given element in actually a celeb
        for i in range(n):
            # if celeb knows someone or other doesn't know celeb
            if i != possible_celeb and (m[possible_celeb][i] or m[i][possible_celeb] == 0): 
                return -1  # return -1 as no celeb is there

        return possible_celeb
    
m = [[0,0,1,0],
     [0,0,1,0],
     [0,0,0,0],
     [0,0,1,0]
    ]

n = 4
print(getId(m, n))
        
        
        