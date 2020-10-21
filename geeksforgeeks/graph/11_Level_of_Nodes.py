'''
Given an connected undirected graph of N edges and a node X is given. 
The task is to find the level of X. if X does not exist in the graph then print -1.


'''
import queue

def levels(g,n,x):
    
    vis = [0 for i in range(n)] # mark each edge as not visited
    levels = [float("inf") for i in range(n)]
    
    q=queue.Queue()
    q.put(0) # insert root in queue
    vis[0] = 1 # mark root as visited
    levels[0] = 0 # initialize the level of root as 0
    
    while(q.qsize()):
        xx = q.get()
        
        for nodes in g[xx]:
            if(vis[xx] == 0):
                q.put(nodes)
                levels[nodes] = levels[xx] + 1
                vis[nodes] = 1
                
    if(x < n):
        return levels[x]
    else:
        return -1