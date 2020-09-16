'''
Given an array of integers. Check whether it contains a triplet that sums up to zero. 

Input:
The first line of input contains an integer T, denoting the number of test cases. 
Then T test cases follow. The first line of each test case contains an integer N, denoting the number of elements in array. 
The second line of each test case contains N space separated values of the array.

Output:
For each test case, output will be 1 if triplet exists else 0.

Your Task:
You don't need to read input or print anything. Your task is to complete the boolean function findTriplets() 
which takes the array arr[] and the size of the array (n) as inputs 
and returns True if the given array has a triplet with zero sum and False otherwise. 

Expected Auxiliary Space: O(1)
Expected Time Complexity: O(n2)

Constrains:
1 <= T <= 100
1 <= N <= 104
-106 <= Ai <= 106

Example:
Input:
2
5
0 -1 2 -3 1
3
1 2 3
Output:
1
0

Explanation:
Testcase 1: 0, -1 and 1 forms a triplet with sum equal to 0.
Testcase 2: No triplet exists which sum to 0.

hints:

1)
A naive approach would be to consider all the triplets present in the array and check if any of them sums up to zero.
But, for considering all the triplets, you'll need 3 nested loops and thus, the time complexity would be O(n3).
Do you really need to check all the triplets present? Can you make it better? How about sorting the array?

2)
Once the array is sorted, how about using a two-pointer approach for this?
You can iterate through the array and for each element arr[i],
check if the pair sum of -arr[i] exists in the remaining array. Try maitaining two pointers for the latter. 

'''
def findTriplets(arr,n):
    
    found = False
    arr.sort()
    #print(arr)
    #print(n)
    for i in range(n):
        
        l = i + 1
        r = n - 1
        x = arr[i]
        
        while(l < r):
            
            if(arr[l] + arr[r] + x == 0):
                found = True
                print(arr[l], arr[r], x)
                l += 1
                r -+ 1
                
            elif(arr[l] + arr[r] + x < 0):
                l += 1
                
            elif(arr[l] + arr[r] + x > 0):
                r -= 1
                
        if(found == False):
            print("Not found")
            
            
arr = [0, -1, 2, -3, 1] 
n = len(arr) 
findTriplets(arr, n) 