def dfs_sprint(Graph,Visited,Vert_stack,x):
    for i in range(len(Graph[x])):
        if not Visited[Graph[x][i]]:
            Visited[Graph[x][i]]=True
            dfs_sprint(Graph,Visited,Vert_stack,Graph[x][i])
    Vert_stack.append(x)

def dfs_scc(Graph,Visited,Scc,x,const):
    for i in range(len(Graph[x])):
        if not Visited[Graph[x][i]]:
            Visited[Graph[x][i]]=True
            dfs_scc(Graph,Visited,Scc,Graph[x][i],const)
    Scc[x]=const

def scc(Graph):
    Visited = [False for i in range(len(Graph))]
    Vert_stack = []
    for i in range(len(Graph)):
        if not Visited[i]:
            Visited[i]=True
            dfs_sprint(Graph,Visited,Vert_stack,i)
    Reversed_graph=[[] for i in range(len(Graph))]
    for i in range(len(Graph)):
        for j in range(len(Graph[i])):
            Reversed_graph[Graph[i][j]].append(i)
    Visited = [False for i in range(len(Graph))]
    Scc=[None for i in range(len(Graph))]
    for i in range(len(Graph)-1,-1,-1):
        if not Visited[Vert_stack[i]]:
            Visited[Vert_stack[i]]=True
            dfs_scc(Reversed_graph,Visited,Scc,Vert_stack[i],Vert_stack[i])
    return Scc

Graph=[ [],
        [6,5,3],
        [0,4,1],
        [5],
        [0,2,3],
        [7],
        [7],
        [1]]
print(scc(Graph))
    