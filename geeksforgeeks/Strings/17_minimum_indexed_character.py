'''
Given a string str and another string patt. Find the character in patt that is present at the minimum index in str. 
If no character of patt is present in str then print 'No character present'.

Input:
The first line of input contains an integer T denoting the number of test cases. Then the description of T test cases follow. 
Each test case contains two strings str and patt respectively.

Output:
Print the character in patt that is present at the minimum index in str.
Print "No character present" (without quotes) if no character of patt is present in str.

Your Task:
This is a function problem. You only need to complete the function printMinIndexCharN that prints the answer. 
The newline is auomatically appended by the driver code.

Constraints:
1 <= T <= 105
1 <= |str|,|patt| <= 105

Example:
Input:
2
geeksforgeeks
set
adcffaet
onkl
Output:
e
No character present

Explanation:
Testcase 1: e is the character which is present in given patt "geeksforgeeks" and is first found in str "set".
Testcase 2: There is none of the characters which is common in patt and str.

hints

1)
Try to use the concept of Hashing to solve the problem.

2)
-Create a hash table with tuple represented as (character, index) tuple.
-Store the first index of each character of str in the hash table.
-Now, for each character of patt check if it is present in the hash table or not.
-If present then get its index from the hash table and update minIndex (minimum index encountered so far).
-For no matching character print 'No character present'.

3)
we can also use set()

https://www.geeksforgeeks.org/find-character-first-string-present-minimum-index-second-string/

'''
def minIndexchar(s,p):
    
    mySet = set()
    
    for ch in p:
        mySet.add(ch)
    #print(mySet)
    for char in s:
        if(char in mySet):
            #print(char,end="")
            return True
    return False
    
s = "geeksforgeeks"
p = "set"
print(minIndexchar(s, p))
