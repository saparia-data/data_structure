'''
1. You are given two integers n and k, where n represents number of elements and k represents 
   number of subsets.
2. You have to partition n elements in k subsets and print all such configurations.

Sample Input:

3
2

Sample Output:

1. [1, 2] [3] 
2. [1, 3] [2] 
3. [1] [2, 3] 

https://www.youtube.com/watch?v=TvvGj1FtHIk&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=11


'''

def kPartitions(i, n, k, ssf, ans):
    
    if(i > n):
        
        if(ssf == k):
            for s in ans:
                if(len(s) > 0):
                    print(s, end = " ")
            print()
            
        return
    
    
    for j in range(len(ans)):
        
        if(len(ans[j]) > 0):
            ans[j].append(i)
            kPartitions(i+1, n, k, ssf, ans)
            ans[j].pop() # remove last element
        else:
            ans[j].append(i)
            kPartitions(i+1, n, k, ssf+1, ans)
            ans[j].pop()
            break
            


if __name__ == "__main__":
    
    n = 3
    k = 2
    ans = [[] for i in range(3)]
    
    kPartitions(1, n, k, 0, ans)