'''
Given a Directed Graph. Find any Topological Sorting of that Graph.

'''

def dfsUtil(v, visit, graph, s):
    
    visit[v] = True
    
    for i in graph[v]:
        if(not visit[i]):
            dfsUtil(i, visit, graph, s)
            
    s.append(v)

def topoSort(n, graph):
    
    visit = [False] * n
    s = []
    for i in range(n):
        if(not visit[i]):
            dfsUtil(i, visit, graph, s)
            
    print(s[::-1])