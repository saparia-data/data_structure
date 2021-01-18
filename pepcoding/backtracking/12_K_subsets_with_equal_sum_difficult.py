'''
1. You are given an array of n distinct integers.
2. You have to divide these n integers into k non-empty subsets such that sum of integers of every 
   subset is same.
3. If it is not possible to divide, then print "-1".


Sample Input:

6

1
2
3
4
5
6

3

Sample Output:

[1, 6] [2, 5] [3, 4] 



https://www.youtube.com/watch?v=rszwy53vaP0&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=14

'''

def solution(arr, vidx, n, k, subSetSum, ssf, ans):
    
    if(vidx == n):
        
        if(ssf == k):
            flag = True
            
            for i in range(len(subSetSum) - 1):
                if(subSetSum[i] != subSetSum[i+1]):
                    flag = False
                    break
                
            if(flag == True):
                
                for partition in ans:
                    print(partition, end = " ")
                    
        return
                
    
    
    for j in range(len(ans)):
        
        if(len(ans[j]) > 0):
            ans[j].append(arr[vidx])
            subSetSum[j] += arr[vidx]
            solution(arr, vidx + 1, n, k, subSetSum, ssf, ans)
            ans[j].pop() # remove last element
            subSetSum[j] -= arr[vidx]
        else:
            ans[j].append(arr[vidx])
            subSetSum[j] += arr[vidx]
            solution(arr, vidx + 1, n, k, subSetSum, ssf + 1, ans)
            ans[j].pop()
            subSetSum[j] -= arr[vidx]
            break


if __name__ == "__main__":
    
    arr = [1,2,3,4,5,6]
    n = len(arr)
    k = 3
    
    ans = [[] for i in range(3)]
    
    summ = 0
    for element in arr:
        sum += element
        
    subSetSum = [0] * k # list to store 
    #print(subset)
    
    if(k == 0):
        print("[")
        for element in arr:
            print(element, end = ",")
        print("]")
        
    if(k > n or summ % k != 0):
        print(-1)
        
    solution(arr, 0, n, k, subSetSum, 0, ans)