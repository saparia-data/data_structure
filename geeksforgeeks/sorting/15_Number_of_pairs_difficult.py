'''
Given two arrays X and Y of positive integers, find number of pairs such that xy > yx (raised to power of) 
where x is an element from X and y is an element from Y.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. 
Each test consists of three lines. The first line of each test case consists of two space separated M and N denoting size of arrays X and Y respectively. 
The second line of each test case contains M space separated integers denoting the elements of array X. 
The third line of each test case contains N space separated integers denoting elements of array Y.

Output:
Corresponding to each test case, print in a new line, the number of pairs such that xy > yx.

Your Task:
This is a function problem. You only need to complete the function countPairs() that takes X, Y, M, N as parameters and returns the total number of pairs.

Constraints:
1 ≤ T ≤ 100
1 ≤ M, N ≤ 105
1 ≤ X[i], Y[i] ≤ 103

Example:
Input:
2
3 2
2 1 6
1 5
4 3 
2 3 4 5
1 2 3
Output:
3
5

Explanation:
Testcase 1: The pairs which follow xy > yx are as such: 2(1) > 1(2),  2(5) > 5(2) and 6(1) > 1(6) .
Testcase 2: The pairs for the given input are 2(1) > 1(2) , 3(2) > 2(3) , 4(1) > 1(4) , 4(3) > 3(4) , 5(1) > 1(5) .


hints:

1)
The trick to this question is if y > x, then then x^y > y^x with some exceptions.

Simply sort the array Y[], and for every element x in X[], find the index idx of smallest number just greater than x in Y[]. 
All the elements after, this index idx satisfy the above relation. So add (n - idx) to the ans.

But as we mentioned there are some exceptions. Try to think of these exceptions.


2)
Following are the exceptions :

if x = 0, then count for this is 0.
 if x = 1, then count is total no of 0s in Y[] only.
if x = 2, for y = 3, y = 4, the above property does not hold, and the count should be decreased
if x = 3, for x = 2, the count need to be increased
This is the complete solution.
The overall time complexity is O(nlogn + mlogm)

'''
from _bisect import bisect_right

#Big O(n3) solution
import bisect
def NumberPairs(X, Y, m, n):
    
    ans = 0
    for i in range(m):
        for j in range(n):
            if (pow(X[i], Y[j]) > pow(Y[j], X[i])):
                ans+=1
    return ans

#Big O(nlogn + mlogm) Solution

def count(x,b,n,NoOfb):
    '''
    If x is 0, then there cannot be any value in Y such that 
     x^Y[i] > Y[i]^x 
    '''
    if(not x):
        return x
    '''
    If x is 1, then the number of pais is equal to number of 
    zeroes in Y[]
    '''
    if(x==1):
        return NoOfb[0]
    
    '''
    Find number of elements in Y[] with values greater than x 
    upper_bound() gets address of first greater element in Y[0..n-1]
    '''
    index=bisect.bisect_right(b,x)
    ans=0
    if(index<n and b[index]>x):
        ans+=n-index
    '''
    If we have reached here, then x must be greater than 1, 
    increase number of pairs for y=0 and y=1 '''
    ans+=(NoOfb[0]+NoOfb[1])
    
    #Decrease number of pairs for x=2 and (y=4 or y=3) 
    if(x==2):
        ans-= NoOfb[3]+NoOfb[4]
    # Increase number of pairs for x=3 and y=2 
    if(x==3):
        ans+=NoOfb[2]

    return ans

''' Function to count total no. of pairs in arrays a and b
    such that x^y > y^x , where x is in a and y is in b'''

def countPairs(a,b,m,n):
    # To store counts of 0, 1, 2, 3 and 4 in array Y 
    NoOfb=[0,0,0,0,0]
    for i in range(n):
        if(b[i]<5):
            NoOfb[b[i]]+=1
            
    # Sort Y[] so that we can do binary search in it 
    b.sort()

    total_pairs=0
    
    # Take every element of X and count pairs with it
    for i in range(m):
        total_pairs+=count(a[i],b,n,NoOfb)
    return total_pairs
        
    
    



X = [2,1,6]
Y = [1,5]
m = len(X)
n = len(Y)
print(NumberPairs(X, Y, m, n))


a = [2,1,6]
b = [1,5]
m = len(X)
n = len(Y)
print(countPairs(a, b, m, n))