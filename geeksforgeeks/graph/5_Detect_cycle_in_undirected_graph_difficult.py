'''
Given a Undirected Graph. Check whether it contains a cycle or not. 

https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

'''
def dfs(g,node,parent,vis):
    
    vis[node] = 1
    
    for nodes in g:
        
        if(vis[nodes] == 0):
            
            if(dfs(g, nodes, node, vis) == 1):
                return 1
            
            else:
                if(nodes != parent):
                    return 1
    
    return 0

def isCyclic(g,n):
    
    # mark each edge as not visited
    vis = [0 for i in range(n)]
    
    for node in range(n):
        if(vis[node] == False):
            if(dfs(g, node, -1, vis)):
                return 1
    return 0