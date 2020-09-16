'''
Here the idea is to use BFS of Graph

https://www.geeksforgeeks.org/shortest-path-unweighted-graph/

 1) initialize dist[v] = [INF, INF, INF, ...]
 
 2) dist[s] = 0 where s = source vertex
 
 3) create queue q
 
 4) q.push(s) 
 
 5) mark visited[s] = True
 
 6)
    while(q is not empty):
        u = q.pop()
        for v in u: (for every adjacent of u)
            if(visited[v] == False):
                dist[v] = dist[u] + 1
                visited[v] = True
                q.push(v)
                
7) print dist[]


'''

            