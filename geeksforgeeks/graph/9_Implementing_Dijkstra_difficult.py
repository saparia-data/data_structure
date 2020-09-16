'''
Given a graph of V nodes represented in the form of the adjacency matrix. 
The task is to find the shortest distance of all the vertex's from the source vertex.

'''

def minDistance(dist, sptSet, V):
    
    min = float('inf')
    
    for v in range(V):
        if(dist[v] < min and sptSet[v] == False):
            min = dist[v]
            min_index = V
            
    return min_index

def dijkstra(src, V, graph):
    
    dist = [float('inf')] * V
    sptSet = [False] * V
    
    dist[src] = 0
    
    for count in range(V):
        
        u = minDistance(dist, sptSet, V)
        
        dist[u] = True
        
        for v in range(V):
            if(sptSet[v] == False and graph[u][v] > 0 and dist[v] > dist[u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]
                
    return dist