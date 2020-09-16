'''
iven an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, 
leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size() : Returns number of elements in queue.
front() : Finds front item.
Input:
First line consists of T test cases. First line of every test case consists of 2 integers, N and K, 
denoting number of elements and number of elements to be reversed respectively. Second line of every test case consists of elements of array.

Output:
For each testcase, in a new line, print the modified queue.

Your Task:
Since this is a function problem, you don't need to take inputs. Just complete the provided function modifyQueue 
that takes queue and k as parameters and returns a modified queue. The printing is done automatically by the driver code.

Expected TIme Complexity : O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= K <= N

Example:
Input:
2
5 3
1 2 3 4 5
4 4
4 3 2 1
Output:
3 2 1 4 5
1 2 3 4

Explanation:
Testcase 1: After reversing the given input from the 3rd position the resultant output will be 3 2 1 4 5.
Testcase 2: After reversing the given input from the 4th position the resultant output will be 1 2 3 4.


hints:

-Use a stack to reverse the elements of list.

'''
def reverseK(queue,k,n):
    
    stack = []
    
    res_queue = []
    
    for i in range(k):
        stack.append(queue.pop(0))
        
    while(len(stack)):
        res_queue.insert(0, stack.pop(0))
        
    while(len(queue)):
        res_queue.append(queue.pop(0))
        
    return res_queue

queue = [1,2,3,4,5,6,7,8,9]
n = len(queue)
k = 5
print(reverseK(queue, k, n))