'''
Given an array A[] of integers, sort the array according to frequency of elements. That is elements that have higher frequency come first.
If frequencies of two elements are same, then smaller number comes first.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
For each testcase, in a new line, print each sorted array in a seperate line. For each array its numbers should be seperated by space.

Your Task:
This is a function problem. You only need to complete the function sortByFreq that takes arr, and n as parameters and prints the sorted elements.
Endline is provided by the driver code.

Constraints:
1 ≤ T ≤ 300
1 ≤ N ≤ 105
1 ≤ Ai ≤ 105 

Example:
Input:
2
5
5 5 4 6 4
5
9 9 9 2 5
Output:
4 4 5 5 6
9 9 9 2 5

Explanation:
Testcase1: The highest frequency here is 2. Both 5 and 4 have that frequency. Now since the frequencies are same then smaller element comes first. 
So 4 4 comes first then comes 5 5. Finally comes 6.
The output is 4 4 5 5 6.

Testcase2: The highest frequency here is 3. The element 9 has the highest frequency. So 9 9 9 comes first. Now both 2 and 5 have same frequency.
So we print smaller element first.
The output is 9 9 9 2 5.

hints:

1)
The idea is to use hashing.

-We insert all elements and their counts into a hash. This step takes O(n) time where n is number of elements.

-We copy contents of hash to an array (or vector) and sort them by counts. 
This step takes O(m Log m) time where m is total number of distinct elements.

-For maintaining the order of elements if the frequency is same, we use another hash which has the key as elements of the array and value as the index.
If the frequency is same for two elements then sort elements according to the index.

'''
#time complexity is Big O(n3)
def sortByFreq(a,n):
    freq=[0 for i in range(max(a)+1)]
    print(freq)
    
    hash_for_freq=[ [] for i in range(n+1) ]
    #print(hash_for_freq)
    
    for num in a:
        freq[num]+=1
    #print(freq)
    
    for i in range(max(a)+1):
        if(freq[i]):
            hash_for_freq[freq[i]].append(i)
    #print(hash_for_freq)
    
    l = []
    for i in range(n,0,-1):
        for num in hash_for_freq[i]:
            for j in range(i):
                l.append(num)
    return l
    
a = [9,9,9,5,2]
n = len(a)
print(sortByFreq(a, n))