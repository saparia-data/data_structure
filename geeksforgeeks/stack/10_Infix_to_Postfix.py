'''
Given an infix expression in the form of string str. Conver this infix expression to postfix expression.

Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
​Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. 
Input:
The first line of input contains an integer T denoting the number of test cases. The next T lines contain an infix expression. 
The expression contains all characters and ^,*,/,+,-. 

Output:
For each testcase, in a new line, output the infix expression to postfix expression.

Your Task:
This is a function problem. You only need to complete the function infixToPostfix() 
that takes a string as a parameter and returns the postfix expression. The printing is done automatically by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 100
1 <= length of str <= 103

Example:
Input:
2
a+b*(c^d-e)^(f+g*h)-i
A*(B+C)/D
Output:
abcd^e-fgh*+^*+i-
ABC+*D/

Explanation:

Testcase 1: After converting the infix expression into postfix expression , the resultant expression will be abcd^e-fgh*+^*+i-

Testcase 2: After converting the infix expression into postfix expression , the resultant expression will be ABC+*D/

hints:

-Scan the infix expression from left to right.
-If the scanned character is an operand, output it.
-Else,
-If the precedence of the scanned operator is greater than the precedence of the operator in the stack push it.
-Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. 
 After doing that Push the scanned operator to the stack. 
 (If encounter parenthesis while popping then stop there and push the scanned operator in the stack.)
-If the scanned character is an ‘(‘, push it to the stack.
-If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis.
-Repeat steps 2-6 until infix expression is scanned.
-Print the output
-Pop and output from the stack until it is not empty.

Rules:

https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
https://www.youtube.com/watch?v=TB7qzDgX-pI

'''

class Conversion:
    
    def __init__(self, capacity):
        
        self.top = -1
        self.cacacity = capacity
        # This array is used a stack  
        self.array = [] 
        # Precedence setting
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        
    # check if the stack is empty 
    def isEmpty(self):
        return True if self.top == -1 else False
    
    # Return the value of the top of the stack 
    def peek(self):
        return self.array[-1]
    
    
    # Pop the element from the stack 
    def pop(self):
        if(not self.isEmpty()):
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
        
    # Push the element to the stack 
    def push(self, op):
        self.top += 1
        self.array.append(op)
        
    # A utility function to check is the given character is operand  
    def isOperand(self, ch):
        return ch.isalpha()
    
    # Check if the precedence of operator is strictly less than top of stack or not 
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
        
    # The main function that converts given infix expression to postfix expression 
    def infixToPostfix(self, exp):
        
        # Iterate over the expression for conversion 
        for i in exp: 
            # If the character is an operand, add it to output 
            if(self.isOperand(i)): 
                self.output.append(i)
                
            # If the character is an '(', push it to stack
            elif(i == '('):
                self.push(i)
                
            # If the scanned character is an ')', pop and  
            # output from the stack until and '(' is found 
            elif(i == ')'):
                while(not self.isEmpty() and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                    
                if(not self.isEmpty() and self.peek() != '('):
                    return -1
                else: 
                    self.pop()
                    
            # An operator is encountered 
            else: 
                while(not self.isEmpty() and self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(i)
                
        # pop all the operator from the stack 
        while not self.isEmpty(): 
            self.output.append(self.pop())
            
        print("".join(self.output))
        
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp)) 
obj.infixToPostfix(exp) 