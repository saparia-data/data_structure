'''
Given a string str containing alphanumeric characters. The task is to calculate sum of all the numbers present in the string.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains a string containing alphanumeric characters.

Output:
Print the sum of all the numbers present in the string.

User Task:
The task is to complete the function findSum() which finds and returns the sum of numbers in the string.

Constraints:
1 <= T <= 105
1 <= length of the string <= 105

Example:
Input:
4
1abc23
geeks4geeks
1abc2x30yz67
123abc
Output:
24
4
100
123

Explanation:
Testcase 1: 1 and 23 are numbers in the string which is added to get the sum as 24.
Testcase 2: 4 is the only number , so the sum is 4.
Testcase 3: 1 , 2 , 30 and 67 are the numbers in the string which is added to get the sum as 100.
Testcase 4: 123 is a single number, so sum is 123.

'''
#using isdigit() function
def findSum(s):
    temp = ""
    Sum = 0
    
    for ch in s: 
        if (ch.isdigit()): 
            temp += ch
        else:
            Sum += int(temp) 
            temp = "0"
            
    return Sum + int(temp)    

#using regular expression
import re 
def find_sum(s):
    return sum(map(int, re.findall('\d+', s)))

#using ord() function
def find_str_sum(s):
    n = len(s)
    total_sum = 0
    tens = 1
    
    for i in range(n-1, -1, -1):
        face_value = ord(s[i]) - ord('0')
        
        if(face_value <=9 and face_value >=0):
            total_sum += face_value*tens
            tens *= 10
        else:
            tens = 1
    return total_sum
            

s = "1abc23"
print(findSum(s))
print(find_sum(s))
print(find_str_sum(s))