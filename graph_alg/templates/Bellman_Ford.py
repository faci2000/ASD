def Bellman_Ford(Graph, start, end):
    change=True
    loop=0
    Cost = [100000 for _ in range(len(Graph))]
    while(change):
        if loop>*len(Graph)-1 :
            return False
        loop+=1
        change=False
        for i in range(len(Graph)):
            for j in range(len(Graph[i])):
                if(Cost[Graph[i][j][0]]>Cost[i]+Graph[i][j][1]):
                    Cost[Graph[i][j][0]]=Cost[i]+Graph[i][j][1]
                    change=True
    return Cost

def find_path_dfs(Graph,Visited,x,dest):
    if x==dest:
        return True
    for i in range(len(Graph[x])):
        if not Visited[Graph[x][i][0]]:
            Visited[Graph[x][i][0]]=True
            if find_path_dfs(Graph,Visited,Graph[x][i][0],dest):
                return True
    return False

def reachable(Graph,start,dest):
    Visited=[False for _ in range(len(Graph))]
    Visited[start]=True
    temp =find_path_dfs(Graph,Visited,start, dest)
    return temp



Graph=[ (0, 1, 5), (0, 3, 9), (0, 6, 3),
        (1, 2, 9), (1, 4, 8), (1, 5, 6), (1, 7, 7),
        (2, 3, 9), (2, 4, 4), (2, 6, 5), (2, 7, 3),
        (3, 6, 8),
        (4, 5, 2), (4, 6, 1),
        (5, 6, 6),
        (6, 7, 9)]
start = 0 
end = 6
Cost = Bellman_Ford(Graph,start,end)
if Cost != False:
    print("CYCLE")
elif not reachable(Graph,start,end):
    print("NO")
else:
    print(Cost[end])
