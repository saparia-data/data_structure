'''
Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”.

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Your Task:
This is a function problem. You only need to complete the function ispar() that takes string as parameter 
and returns true if brackets are balanced else returns false. The printing is done automatically by the driver code.

Expected Time Complexity : O(n)
Expected Auixilliary Space : O(n)

Constraints:
1 ≤ T ≤ 100
1 ≤ |x| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced

Explanation:

Testcase 1: { ( [ ] ) }. Same colored brackets can form balaced pairs, with 0 number of unbalanced bracket.

Testcase 2: () . Same bracket can form balanced pairs, and here only 1 type of bracket is present and in balanced way.

Testcase 3: ([] . Here square bracket is balanced but the small bracket is not balanced and Hence , the output will be unbalanced.

hints:

-Push the element into the stack.
-Pop the element from the stack if the top of stack has the opposite parenthesis.
-At the end check if the stack size is empty or not.
-The answer is balanced if stack is empty or else it is unbalanced .

'''
def ispar(s):
    
    stack = []
    
    for char in s:
        
        if(char in ['[','{','(']):
            stack.append(char)
            
        else:
            
            if(len(stack) == 0):
                return False
            
            if(char == ']'):
                if(stack[-1] == '['):
                    stack.pop()
                    continue
                
            if(char == '}'):
                if(stack[-1] == '{'):
                    stack.pop()
                    continue
                
            if(char == ')'):
                if(stack[-1] == '('):
                    stack.pop()
                    continue
                
            return False
    
    if(len(stack)):
        return False
    
    return True

s = "{([])}"
print(ispar(s))