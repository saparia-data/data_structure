'''
We hope you are familiar with using counter variables. Counting allows us to find how may times a certain element appears in an array or list.

You are given an array arr[] of size N. You are also given two elements x and y. Now, you need to tell which element (x or y) appears most in the array.
In other words, print the element, x or y, that has highest frequency in the array. If both elements have the same frequency,
then just print the smaller element.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 3 lines of input.
The first line contains size of array denoted by n. The second line contains the elements of the array separated by spaces.
The third line contains two integers x and y separated by a space.

Output Format:
For each testcase, in a newline, print the element with highest occurrence in the array. If occurrences are same, then print the smaller element.

Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code.
You just need to complete the function majorityWins() that takes array, n, x, y as parameters and return the element with highest 

Constraints:
1 <= T <= 100
1 <= n <= 103
0 <= arri , x , y <= 108

Examples:
Input:
2
11
1 1 2 2 3 3 4 4 4 4 5
4 5
8
1 2 3 4 5 6 7 8
1 7

Output:
4
1

Explanation:
Testcase 1: n=11; elements = {1,1,2,2,3,3,4,4,4,4,5}; x=4; y=5
x frequency in arr is = 4 times
y frequency in arr is = 1 times
x has higher frequency, so we print 4.

Testcase 2: n=8; elements = {1,2,3,4,5,6,7,8}; x=1; y=7
x frequency in arr is 1 times
y frequency in arr is 1 times
both have same frequency, so we look for the smaller element.
x=1 is smaller than y=7, so print 1.
'''

def majorityWins(arr, n, x, y):
    c_x = 0
    c_y = 0
    for i in range(n):
        if(arr[i] == x):
            c_x = c_x + 1
        elif(arr[i] == y):
            c_y = c_y + 1
        else:
            continue
    #print(c_x)
    #print(c_y)
    if(c_x > c_y):
        return x
    elif(c_x < c_y):
        return y
    elif(c_x == c_y):
        return min(x,y)
    


arr = [854,190,562,906,2,625,678,667,779,755,699,842,970,81,253,155,456,830,575,640,962,44,124,209,841,571,211,213,904,993,130,996,866,938,553,114,3,79,18,823,176,75,740,83,391,223,289,561,927,351,744]
n = len(arr)
x = 10
y = 40
print(majorityWins(arr,n,x,y))
    
        
            