'''
Given a postfix expression, the task is to evaluate the expression and print the final value. 
Operators will only include the basic arithmetic operators like *,/,+ and -.

Input:
The first line of input will contains an integer T denoting the no of test cases . Then T test cases follow. 
Each test case contains an postfix expression.

Output:
For each test case, in a new line, evaluate the postfix expression and print the value.

Your Task:
This is a function problem. You need to complete the function evaluatePostfixExpression() that takes the string denoting the expression 
as input and returns the evaluated value.

Expected Time Complexity : O(n)
Expected Auixilliary Space : O(n)

Constraints:
1 <= T <= 100
1 <= length of expression <= 1000

Example:
Input:
2
231*+9-
123+*8-
Output:
-4
-3

Explanation:
Testcase 1: After solving the given expression, we have -4 as result.
Testcase 2: After solving the given postfix expression , we have -3 as result.

Rules:

Following is algorithm for evaluation postfix expressions.
1) Create a stack to store operands (or values).
2) Scan the given expression and do following for every scanned element.
    a) If the element is a number, push it into the stack
    b) If the element is a operator, pop operands for the operator from stack. Evaluate the operator and push the result back to the stack
3) When the expression is ended, the number in the stack is the final answer

'''

class Evaluate: 
      
    # Constructor to initialize the class variables 
    def __init__(self, capacity): 
        self.top = -1
        self.capacity = capacity 
        # This array is used a stack  
        self.array = [] 
      
    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of the stack 
    def peek(self): 
        return self.array[-1] 
      
    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
      
    # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
  
  
    # The main function that converts given infix expression to postfix expression 
    def evaluatePostfix(self, exp): 
          
        # Iterate over the expression for conversion 
        for i in exp: 
              
            # If the scanned character is an operand (number here) push it to the stack 
            if i.isdigit(): 
                self.push(i) 
  
            # If the scanned character is an operator, pop two elements from stack and apply it. 
            else: 
                val1 = self.pop() 
                val2 = self.pop() 
                self.push(str(eval(val2 + i + val1))) 
  
        return int(self.pop()) 
                  
  
              
# Driver program to test above function 
exp = "231*+9-"
obj = Evaluate(len(exp)) 
print("postfix evaluation: %d"%(obj.evaluatePostfix(exp)))