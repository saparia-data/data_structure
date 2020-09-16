'''
Given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use recursive approach.

https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

'''

def dfsUtil(g, vis, root, res):
    
    res.append(root)
    vis[root] = True
    
    for nodes in root:
        if(vis[nodes] == False):
            dfsUtil(g, vis, nodes, res)

def dfs(g, N):
    
    vis = [False for i in range(N)]
    res = []
    
    dfsUtil(g, 0, vis, res)
    return res