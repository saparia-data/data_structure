'''
Given a set of N jobs where each job i has a deadline and profit associated to it. 
Each job takes 1 unit of time to complete and only one job can be scheduled at a time. 
We earn the profit if and only if the job is completed by its deadline. The task is to find the maximum profit and the number of jobs done.

Jobs will be given in the form (Job id, Deadline, Profit) associated to that Job.

Example 1:
Input:
N = 4
Jobs = (1,4,20)(2,1,10)(3,1,40)(4,1,30)
Output: 2 60
Explanation: 2 jobs can be done with
maximum profit of 60 (20+40).

Example 2:
Input:
N = 
Jobs = (1,2,100)(2,1,19)(3,2,27)
(4,1,25)(5,1,15)
Output:2 127
Explanation: 2 jobs can be done with
maximum profit of 127 (100+27).

https://www.geeksforgeeks.org/job-sequencing-problem/

'''

def printJobScheduling(arr, t): 
  
    # length of array 
    n = len(arr) 
  
    # Sort all jobs according to  
    # decreasing order of profit 
    
    '''
    for i in range(n): 
        for j in range(n - 1 - i): 
            if arr[j][2] < arr[j + 1][2]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    '''
    
    arr = sorted(arr, key = lambda x: x[2], reverse = True)            
    print(arr)
  
    # To keep track of free time slots 
    result = [False] * t 
  
    # To store result (Sequence of jobs) 
    job = ['-1'] * t 
  
    # Iterate through all given jobs 
    for i in range(len(arr)): 
  
        # Find a free slot for this job  
        # (Note that we start from the  
        # last possible slot)
        mini = min(t - 1, arr[i][1] - 1)
        for j in range(mini, -1, -1): 
              
            # Free slot found 
            if result[j] is False: 
                result[j] = True
                job[j] = arr[i][0] 
                break
  
    # print the sequence 
    print(job)


arr = [['a', 2, 100], # Job Array 
       ['b', 1, 50], 
       ['c', 3, 30], 
       ['d', 1, 20], 
       ['e', 2, 10]] 

printJobScheduling(arr, 3)