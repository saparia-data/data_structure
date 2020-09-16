'''
Given a quadratic equation in the form ax2 + bx + c. You need to print roots of it.

Input Format:
First line of input contains an integer, the number of test cases T. 
Each test case contains three positive numbers a, b and c in the same line seperated by space.

Output Format: 
If roots of equations exits, then print the two roots separated by space (Higher valued root should be printed before lower valued).
Else if a = 0, then print "Invalid" as equation is not quadratic.  If roots are imaginary, then print "Imaginary".

Note 1 :  Please do NOT to add "\n" or newline after printing output in your function.  Newline is added by the driver code.
Note 2 : Please do float division like (-b+sqrt(b2-4ac)) / 2.0*a.

Your Task:
This is a function problem. You only need to complete the function quadraticRoots that takes a,b,c as parameters and prints the floor value of roots.
The other tasks are already performed by the driver function. The newline is already appended by the driver code.

Constraints:
1 <= T <= 50
1 <= a <= 103
1 <= b <= 103
1 <= c <= 103

Example:
Input:
3
1 -2 1
1 -7 12
1 4 8

Output:
1 1
4 3
Imaginary

Explanation:
Testcase 1: Roots of equation x2 - 7x + 12 are 4 and 3.
Testcase 3: Roots of equation x2 + 4x + 8 are imaginary since it's discriminant is less than 0.

Hints:
1) use quadratic equations
2) If b2-4ac >=0, then roots are real else imaginary.

def quadraticRoots(a,b,c):
'''
from math import sqrt, pow, floor

def quadraticRoots(a,b,c):
    d = sqrt(pow(b,2) -4*a*c)
    if(d < 0):
        print("Imaginary")
    else:
        r1 = floor((-b + sqrt(d)) / (2.0 * a))
        r2 = floor((-b - sqrt(d)) / (2.0 * a))
        r1,r2 = (r1,r2) if r1>r2 else (r2,r1)
        print(r1,r2)
    
quadraticRoots(2,8,8)  
    
    