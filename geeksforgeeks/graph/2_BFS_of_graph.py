'''
Given a directed graph. The task is to do Breadth First Search of this graph.

https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

'''
import queue

def bfs(g, N):
    
    res = []
    
    q = queue.Queue
    
    vis = [False for i in range(N)]
    
    q.put(0)
    
    while(not q.empty()):
        
        node = q.get()
        vis[node] = True
        res.append(node)
        
        for nodes in node:
            if(not vis[nodes]):
                q.put(nodes)
                vis[nodes] = True
                
    return res