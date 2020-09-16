'''
You are given an array A[] of size N, and you are also given a sum. 
You need to find if two numbers in A exists that have sum equal to the given sum.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains three lines of input. 
The first line contains N denoting the size of the array A. The second line contains N elements of the array. The third line contains element sum.

Output:
For each testcase, in a new line, print the required output.

Your Task:
Since this is a function problem, you don't need to take any input. Just complete the provided function sumExists().

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
4
4 3 5 6
12
Output:
1
0

Explanation:
Testcase 1: there exists a pair which gives sum as 14 example (4,10), (5,9) etc.
Testcase 2: there does not exist any such pair which gives sum as 12.

hints:

1)
In this questions, the elements of the array are not distinct. So, hashing the elements in the beginning would not be a wise move. 
Instead check if sum-arr[i] exists in the hash and if not then hash the element.

2)
temp=sum-arr[i];
if(temp>=0 && hash.contains(temp))
return 1;
hash.insert(arr[i]);

'''
def sumExists(arr,sizeOfArray,sum):
    
    mySet = set()
    
    for i in arr:
        temp = sum - i
        if(temp > 0 and temp in mySet):
            return 1
        mySet.add(i)
        
    return 0
    
arr = [1,2,3,4,5,6,7,8,9,10]
sizeOfArray = len(arr)
sum = 14
print(sumExists(arr, sizeOfArray, sum))