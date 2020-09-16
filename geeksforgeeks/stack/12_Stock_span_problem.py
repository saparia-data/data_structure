'''
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock 
and we need to calculate the span of stock’s price for all n days. 

The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, 
for which the price of the stock on the current day is less than or equal to its price on the given day.

For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, 
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the size of the array. The second line of each test case contains N input C[i].

Output:
For each testcase, print the span values for all days.

User Task:
The task is to complete the function calculateSpan() which finds the span of stock's price for all N days and returns an array of length N denoting the span for the i-th day.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 105
1 ≤ C[i] ≤ 105

Example:
Input:
2
7
100 80 60 70 60 75 85
6
10 4 5 90 120 80
Output:
1 1 1 2 1 4 6
1 1 2 4 5 1

Explanation:

Testcase 1: Traversing the given input span for 100 will be 1,80 is smaller than 100 so the span is 1 , 
            60 is smaller than 80 so the span is 1 , 70 is greater than 60 so the span is 2 and so on. 
            Hence the output will be 1 1 1 2 1 4 6.
            
Testcase 2: Traversing the given input span for 10 will be 1, 4 is smaller than 10 so the span will be 1 , 
            5 is greater than 4 so the span will be 2 and so on. Hence, the output will be 1 1 2 4 5 1.

hints:

-The stack contains the index of the prices in decreasing order of prices.
-Add the very first stock index in the stack, from next iteration, if (price[i] < price[stack.top()] ) insert it in the stack 
 else pop from the stack till you find a greater value in the stack and calculate the span, if the stack is empty i+1 will be your span

'''

def calculateSpan(a,n):
    
    # list consisting of span values.
    S = [0 for i in range(n+1)] 

    # Create a stack and push index of fist element to it
    st = []
    st.append(0)

    # Span value of first element is always 1
    S[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):

        # Pop elements from stack while stack is not
        # empty and top of stack is smaller than price[i]
        while (len(st) > 0 and a[st[-1]] <= a[i]):
            st.pop()

            # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i] is
        # greater than elements after top of stack
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1])

        # Push this element to stack
        st.append(i)
    
    # return first n-1 entries from the span list, as last entry is dummy.
    return S[0:n] 

a = [100, 80, 60, 70, 60, 75, 65]
n = len(a)

print(calculateSpan(a, n)) 