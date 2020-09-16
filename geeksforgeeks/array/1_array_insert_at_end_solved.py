'''
Insertion is a basic but frequently used operation. Arrays in most languages cannnot be dynamically shrinked or expanded. Here, we will work with such arrays and try to insert an element at the end of array.

You are given an array arr. The size of the array is given by sizeOfArray. You need to insert an element at end  and print the modified array.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains three lines of input. The first line contains size of the array denoted by sizeOfArray. The second line contains sizeOfArray-1 elements separated by spaces. The third line contains element to be inserted at end.

Output Format:
For each testcase, in a new line, print the modified array.

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function insertAtEnd() that takes arr, sizeOfArray, element as input. The driver code takes care of the printing.

Constraints:
1 <= T <= 100
1 <= sizeOfArray <= 1000
0 <= element, arri <= 106

Examples:
Input:
2
6
1 2 3 4 5
90
4
1 2 3
50

Output:
1 2 3 4 5 90
1 2 3 50

Explanation:
Testcase 1: After inserting 90 at end, we have array elements as 1 2 3 4 5 90.
'''
def insertAtEnd(arr, sizeOfArr,element):
    arr.append(element)
    return arr

print(insertAtEnd([1,2,3], 3, 60))