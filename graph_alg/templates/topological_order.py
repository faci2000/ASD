import queue

def dfs(Graph,Visited,Order,x):
    for i in range(len(Graph[x])):
        if not Visited[Graph[x][i]]:
            Visited[Graph[x][i]]=True
            dfs(Graph,Visited,Order,Graph[x][i])
    Order.append(x)

def topological_ordering(Graph):
    Visited = [False for i in range(len(Graph))]
    Order = []
    for i in range(len(Graph)):
        if (not Visited[i]):
            Visited[i]=True
            dfs(Graph,Visited,Order,i)
    return Order

Graph=[ [],
        [6,5,3],
        [1],
        [],
        [0,2,3],
        [],
        []]
print(topological_ordering(Graph))