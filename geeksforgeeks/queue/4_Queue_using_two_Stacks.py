'''
Implement a Queue using 2 stacks s1 and s2 .

Input:
The first line of the input contains an integer 'T' denoting the number of test cases. Then T test cases follow.
First line of each test case contains an integer Q denoting the number of queries . 
A Query Q is of 2 Types
(i) 1 x (a query of this type means  pushing 'x' into the queue)
(ii) 2   (a query of this type means to pop element from queue and print the poped element)
The second line of each test case contains Q queries seperated by space.

Output:
The output for each pop query will be the space separated integers having -1 if the queue is empty else the element poped out from the queue .

Your Task:
Since this is a function problem, you don't need to take inputs. 
You are required to complete the two methods push which take one argument an integer 'x' to be pushed into the queue 
and pop which returns a integer poped out from other queue. The printing is done automatically by the driver code.

Expected Time Complexity : O(1) for both push() and O(N) for pop().
Expected Auxilliary Space : O(N).

Constraints:
1 <= T <= 100
1 <= Q <= 100
1 <= x <= 100

Example:
Input:
2
5
1 2 1 3 2 1 4 2
4
1 2 2 2 1 4
Output:
2 3
2 -1

Explanation:

Testcase1: In the first testcase
1 2    the queue will be {2}
1 3    the queue will be {2 3}
2       poped element will be 2 the queue will be {3}
1 4    the queue will be {3 4}
2       poped element will be 3.

Testcase 2: In the second testcase 
1 2    the queue will be {2}
2       poped element will be 2 and then the queue will be empty
2       the queue is empty and hence -1
1 4    the queue will be {4}.


'''

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []
    
class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):

        if self.out_stack.is_empty:
            while self.in_stack.size()>0:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.items.pop()