'''
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

Input:
The first line of input will be the number of test cases. Then T test cases follow. Each Test case contains 2 lines. The first line will contain an integer N denoting the number of petrol pumps and in the next line are N space separated values petrol and distance denoting the amount of petrol every petrol pump has and the distance to next petrol pump respectively .

Output:
The output of each test case will be the index of the the first point from where a truck will be able to complete the circle otherwise -1 .

Your Task:
Your task is to complete the function tour() which takes the required data as inputs 
and returns an integer denoting a point from where a truck will be able to complete the circle (The truck will stop at each petrol pump 
and it has infinite capacity). If there exists multiple such starting points, then the function must return the first one out of those.

Expected Time Complexity: O(N)
Expected Auxiliary Space : O(N)

Constraints:
1 <= T <= 100
1 <= N <= 10000
1 <= petrol, distance <= 1000

Example (To be used only for expected output)
Input:
1
4
4 6 6 5 7 3 4 5
Output:
1

Explanation:

Testcase 1: there are 4 petrol pumps with amount of petrol and distance to next petrol pump value pairs as {4, 6}, {6, 5}, {7, 3} and {4, 5}. 
The first point from where truck can make a circular tour is 2nd petrol pump. Output in this case is 1 (index of 2nd petrol pump).


'''
# O(n2) solution
def petrolPump(petrol, dist, n):
    
    for start in range(n):
        
        curr_petrol = 0
        end = start
        
        while(True):
            
            curr_petrol += (petrol[end] - dist[end])
            
            if(curr_petrol < 0):
                break
            
            end = (end + 1) % n
            
            if(end == start):
                return start + 1
            
# O(n) Solution
def petrolPump2(petrol, dist, n):
    
    start = 0
    curr_petrol = 0
    prev_petrol = 0
    
    for i in range(n):
        curr_petrol += (petrol[i] - dist[i])
        
        if(curr_petrol < 0):
            start = i + 1
            curr_petrol = 0
            prev_petrol += curr_petrol
            
    if(curr_petrol + prev_petrol > 0):
        return start + 1
    else:
        return -1
    
# this problem can also be solved using Deque with O(n) extra space
            
petrol = [4,8,7,4]
dist = [6,5,3,5]
n = len(petrol)
print(petrolPump(petrol, dist, n))
print(petrolPump2(petrol, dist, n))