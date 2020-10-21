'''
Given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.

Note : The start time and end time of two activities may coincide.

Example 1:
Input:
N = 5
start[] = {1,3,2,5,8,5}
end[] = {2,4,6,7,9,9}
Output: 4
Explanation:Perform the activites 1,2,4,5

Example 2:
Input:
N = 4
start[] = {1,3,2,5}
end[] = {2,4,3,6}
Output: 4
Explanation:Perform the activities1,3,2,4

'''

def maximumActivities(n,start,end):
    '''
    :param n: number of activities
    :param start: array of start time of activities
    :param end: array of  end time of activities
    :return: Integer, maximum number of activities
    '''
    # stores pairwise start and end time of activities
    time_pair = []

    for i in range(n):
        # appends pairs
        time_pair.append([start[i],end[i]])
        
    # sort according to end time of activities in ascending order
    time_pair = sorted(time_pair, key = lambda item: item[1])
    
    # previous activity always 0
    prev = 0
    ans = 1
    
    for i in range(1, n):
        curr = time_pair[i][0]
        if(curr >= prev):
            ans += 1
            prev = curr
            
    return ans

N = 5
start = [1,3,2,5,8,5]
end = [2,4,6,7,9,9]
print(maximumActivities(N, start, end))