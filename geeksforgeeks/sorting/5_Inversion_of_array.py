'''
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted. 
If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The first line of each test case is N, the size of array. 
The second line of each test case contains N space seperated values of the array arr[].

Output:
Print the inversion count of array.

Your Task:
You don't need to read input or print anything. Your task is to complete the function inversionCount() 
which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.

Expected Time Complexity: O(nLogn).
Expected Auxiliary Space: O(n).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ C ≤ 1018

Example:
Input:
3
5
2 4 1 3 5
5
2 3 4 5 6
3
10 10 10
Output:
3
0
0

Explanation:
Testcase 1: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Testcase 2: As the sequence is already sorted so there is no inversion count.
Testcase 3: As all the elements of array are same, so there is no inversion count.

hints:

1)
A naive solution to this would be to use 2 nested for-loops and for every index i, 
find the count of elements greater than arr[i] to the right of it. Finally, return the sum of such counts for every value of 0 <= i < n. 
But the time complexity of this will be O(n2). Can we make it better? 

2)
We basically need to make the comparisons in the existing array and while doing any comparison, 
we need to know that how would the two numbers being compared would be ordered in the sorted version of this array.
So, how about running a sorting algorithm itself?
The algorithms like Bubble Sort, Insertion Sort and Selection sort are O(n2). 
We can achieve this complexity even via the naive approach discussed in the previous hint, so no use of it.
What about getting to this via merge sort?

3)
Use Merge sort algorithm, and sort the array.

In merge function for merge sort, while comparing the elements, if element in right array is smaller, then it is an inversion (Why..??)

This means that this smaller element in the original array, is behind larger elements. 
So add the number of larger elements or elements left in the left-array, to the value of counter.

This process is repeated again and again for complete Merge Sort

Finally output counter variable. This is the answer.


'''
def merge(a, start, mid, end):
    global inv_cnt
    temp = [0 for i in range(end - start + 1)]
    i, j, k = start, mid + 1, 0  # indexes of left,right and temp arrays
    
    # merge while conditions are valid
    while (i <= mid and j <= end):
        
        # compare the elements and merge
        if (a[i] <= a[j]):
            temp[k] = a[i]
            k += 1
            i += 1
        else:
            temp[k] = a[j]
            k += 1
            j += 1
            inv_cnt += (mid - i + 1) # inversion occurs here as right moved ahead of left

    # storing the rest elements
    while (i <= mid):
        temp[k] = a[i]
        k += 1
        i += 1

    # storing the rest elements 
    while (j <= end):
        temp[k] = a[j]
        k += 1
        j += 1

    for i in range(start, end + 1):
        a[i] = temp[i - start]

def merge_sort(a, start, end):
    if(start < end):
        mid = (start + end) // 2
        merge_sort(a, start, mid)
        merge_sort(a, mid + 1, end)
        merge(a, start, mid, end)

inv_cnt = 0
def Inversion_Count(a,n):
    
    global inv_cnt
    merge_sort(a,0, n - 1)
    return inv_cnt


a = [1, 20, 6, 4, 5] 
n = len(a) 
print(Inversion_Count(a, n))