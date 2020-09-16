'''
You are given N number of books. Every ith book has Pi number of pages. 

You have to allocate books to M number of students. There can be many ways or permutations to do so. 

In each permutation one of the M students will be allocated the maximum number of pages. 

Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated 
to a student is minimum of those in all the other permutations, and print this minimum value. 

Each book will be allocated to exactly one student. Each student has to be allocated atleast one book.
Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see explanation for better understanding).

Input:
The first line contains 'T' denoting the number of testcases. 
Then follows description of T testcases:Each case begins with a single positive integer N denoting the number of books.
The second line contains N space separated positive integers denoting the pages of each book.
And the third line contains another integer M, denoting the number of students.

Output:
For each test case, output a single line containing minimum number of pages each student has to read for corresponding test case.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A [ i ] <= 106
1 <= M <= 106

Example:
Input:
2
4
12 34 67 90
2
3
15 17 20
2
Output:
113
32

Explaination:
Testcase 1:Allocation can be done in following ways:
{12} and {34, 67, 90}     Maximum Pages = 191
{12, 34} and {67, 90}     Maximum Pages = 157
{12, 34, 67} and {90}        Maximum Pages = 113

Therefore, the minimum of these cases is 113, which is selected as output.

Testcase 2: Allocation can be done in following ways:
{15} and {17,20} Maximum pages = 37
{17} and {15,20} Maximum Pages = 35
{20} and {15,17} maximum pages = 32.

So, the output will be 32.

https://www.youtube.com/watch?v=Ss9ta1zmiZo

https://www.geeksforgeeks.org/allocate-minimum-number-pages/


'''
def isPossibe(arr, n, m, curr_min):
    
    curr_sum = 0
    studentRequired = 1
    
    for i in range(n):
        
        if(arr[i] > curr_min):
            return False
        
        if(curr_sum + arr[i] > curr_min):
            
            studentRequired += 1
            
            curr_sum = arr[i]
            
            if(studentRequired > m):
                return False
            
        else:
            curr_sum += arr[i]
            
    return True

def findPages(arr, n, m):
    
    sum = 0
    
    if(n < m):
        return -1
    
    for i in range(n):
        sum += arr[i]
        
    start, end = 0, sum
    result = 10**9
    
    while(start <= end):
        
        mid = (start + end) // 2
        
        if(isPossibe(arr, n, m, mid)):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1  
            
    return result
    

arr = [12, 34, 67, 90] 
n = len(arr)
m = 2
print(findPages(arr, n, m))

arr1 = [12,34,67,90]
n1 = len(arr1)
m1 = 2
print(findPages(arr1, n1, m1))






