'''
You are given an array A (distinct integers) of size N, and you are also given a sum. 
You need to find if two numbers in A exists that have sum equal to the given sum.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains three lines of input. 
The first line contains N denoting the size of the array A. The second line contains N elements of the array. The third line contains element sum.

Output:
For each testcase, in a new line, print  "1"(without quotes) if any pair found, othwerwise print "0"(without quotes) if not found.

Your Task:
Since this is a function problem, you don't need to take any input. Just complete the provided function sumExists.

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= Ai <= 106
1 <= sum <= 1000

Examples:
Input:
2
10
1 2 3 4 5 6 7 8 9 10
14
2
2 5
10
Output:
1
0

Explanation:
Testcase 1: arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} and sum = 14.  There is a pair {4, 10} with sum 14.
Testcase 2: arr[]  = {2, 5} and sum = 10. There is no pair with sum 10.

hints:

1)
Use hash. Hash the elements of the array. Now for two numbers to be equal to sum we should have x+y=sum. Both x and y belong to the array.
We have hashed x. Now x+y=sum can be rewritten as x=sum-y. 
So, now we just need to traverse the array and see if the hash contains sum-arr[i]. If exists then the pair exists.

2)
Take care of the condition when sum-arr[i]=arr[i] like in the case when array  is {2} and sum is 4. 
Now, we can't make 4 as we only have one element. But doing sum-arr[i] will give 4-2=2. 
And since we already have a 2 in the hash, it's going to return true which is a wrong answer.

'''

def sumExists(arr,sizeOfArray,sum):
    
    mySet = set()
    
    for i in arr:
        mySet.add(i)
        
    for i in arr:
        #Taking care of cases like 4-2=2 as two 2's cannot exist in distinct array
        if(sum - i == i):
            continue
        else:
            if(sum-i in mySet):
                return 1
    return 0


arr = [1,2,3,4,5,6,7,8,9,10]
sizeOfArray = len(arr)
sum = 14
print(sumExists(arr, sizeOfArray, sum))
