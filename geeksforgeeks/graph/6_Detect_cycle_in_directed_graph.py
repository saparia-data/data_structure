'''
Given a Directed Graph. Check whether it contains any cycle or not.

https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

'''
def dfsutil(v, recs, visit, graph):
    
    if(visit[v] is False):
        
        visit[v] = True
        recs[v] = True
        
        for i in graph[v]:
            
            if(not visit[i] and dfsutil(i, recs, visit, graph)):
                return True
            
            elif(recs[i] is True):
                return True
        
    recs[v] = False
    return False
        


def isCyclic(n, graph):
    
    visit = [False] * n
    recs = [False] * n
    
    for i in range(n):
        
        if(visit[i] == False):
            
            if(dfsutil(i, recs, visit, graph) is True):
                return True
    return False