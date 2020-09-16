'''
Given two sorted arrays arr[] and brr[] of sizes N and M respectively. 
The task is to find the median of the two arrays when they get merged.

Input:
First line of input contains number of testcases T. 
First line of input contains number of elements in both arrays N and M respectively. 
Next two lines contains the array elements.

Output:
For each testcase, print the median of two sorted arrays. 
If there are total even elements, we need to print floor of average of middle two elements.

Constraints:
1 <= T <= 100
1 <= N, M <= 106
1 <= arr[i], brr[i] <= 107

Example:
Input:
4
5 6
1 2 3 4 5
3 4 5 6 7 8
2 3
1 2
2 3 4
4 4
1 2 3 4
11 12 13 14
4 3
1 2 3 4
2 3 4

Output:
4
2
7
3

Explanation:
Testcase 1: After merging two arrays, elements will be as 1 2 3 3 4 4 5 5 6 7 8. So, median is 4.
Testcase 2: After merging two arrays , elements will be 1 2 2 3 4. So, the median is 2.
Testcase 3: After merging two arrays , elemenst will be 1 2 3 4 11 12 13 14 . 
            So the median will be floor of average of middle terms i.e, 7.
Testcase 4: After merging two arrays, elements will be 1 2 2 3 3 4 4. So, the median will be 3.

https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/

https://www.youtube.com/watch?v=LPFhl65R7ww

'''
median = 0
i = 0 
j = 0
   
# def to find max 
def maximum(a, b) : 
    return a if a > b else b 
   
# def to find minimum 
def minimum(a, b) : 
    return a if a < b else b 
   
# def to find median 
# of two sorted arrays 
def findMedianSortedArrays(a, n, b, m) : 
  
    global median, i, j 
    min_index = 0 
    max_index = n  
       
    while (min_index <= max_index) : 
      
        i = int((min_index + max_index) / 2) 
        print(i)
        j = int(((n + m + 1) / 2) - i) 
        print(j)
        # if i = n, it means that  
        # Elements from a[] in the 
        # second half is an empty  
        # set. and if j = 0, it  
        # means that Elements from  
        # b[] in the first half is  
        # an empty set. so it is  
        # necessary to check that,  
        # because we compare elements  
        # from these two groups.  
        # Searching on right 
        if (i < n and j > 0 and b[j - 1] > a[i]) : 
            min_index = i + 1
                   
        # if i = 0, it means that  
        # Elements from a[] in the 
        # first half is an empty  
        # set and if j = m, it means 
        # that Elements from b[] in  
        # the second half is an empty  
        # set. so it is necessary to 
        # check that, because we compare  
        # elements from these two groups. 
        # searching on left 
        elif (i > 0 and j < m and b[j] < a[i - 1]) : 
            max_index = i - 1
           
        # we have found the 
        # desired halves. 
        else : 
          
            # this condition happens when  
            # we don't have any elements  
            # in the first half from a[]  
            # so we returning the last 
            # element in b[] from the  
            # first half. 
            if (i == 0) : 
                median = b[j - 1] 
                   
            # and this condition happens  
            # when we don't have any  
            # elements in the first half  
            # from b[] so we returning the  
            # last element in a[] from the  
            # first half. 
            elif (j == 0) : 
                median = a[i - 1]          
            else : 
                median = maximum(a[i - 1], b[j - 1])  
            break
          
      
       
    # calculating the median. 
    # If number of elements  
    # is odd there is  
    # one middle element. 
   
    if ((n + m) % 2 == 1) : 
        return median 
   
    # Elements from a[] in the  
    # second half is an empty set.  
    if (i == n) : 
        return ((median + b[j]) / 2.0) 
   
    # Elements from b[] in the  
    # second half is an empty set. 
    if (j == m) : 
        return ((median + a[i]) / 2.0) 
       
    return ((median + minimum(a[i], b[j])) / 2.0) 
  
   
# Driver code 
a = [3,5,10,11,17] 
b = [9,13,20,21,23,27] 
n = len(a) 
m = len(b) 
   
# we need to define the  
# smaller array as the  
# first parameter to make  
# sure that the time complexity 
# will be O(log(min(n,m))) 
if (n < m) : 
    print ("The median is : {}".format(findMedianSortedArrays(a, n, b, m))) 
else : 
    print ("The median is : {}".format(findMedianSortedArrays(b, m, a, n))) 