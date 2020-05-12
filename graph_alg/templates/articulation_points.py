def articulation_dfs(Graph,Visited,Dfs_num,Low,numerator,parent,x,Articulation_points):
    Visited[x]=True
    Dfs_num[x]=numerator[0]
    Low[x]=numerator[0]
    for i in range(len(Graph[x])):
        if not Visited[Graph[x][i]]:
            numerator[0]+=1
            temp = articulation_dfs(Graph,Visited,Dfs_num,Low,numerator,x,Graph[x][i],Articulation_points)
            if temp<Low[x]:
                Low[x]=temp
            elif x!=0:
                Articulation_points.append(x)
        elif Graph[x][i]!=parent:
            if Dfs_num[Graph[x][i]]<Low[x]:
                Low[x]=Dfs_num[Graph[x][i]]
    return Low[x]


def finding_articulation_points(Graph):
    numerator  = [0]
    Dfs_num =[0 for i in range(len(Graph))]
    Low = [100000 for i in range(len(Graph))]
    Visited = [False for i in range(len(Graph))]
    Articulation_points=[]
    articulation_dfs(Graph,Visited,Dfs_num,Low,numerator,0,0,Articulation_points)
    if(len(Graph[0])>=2):
        Articulation_points.append(0)
    return Articulation_points

Graph=[[1,2,3,5],
        [4,5,0],
        [3,0],
        [6,7,2,0],
        [5,1],
        [4,1,0],
        [3,7],
        [6,3]]
print(finding_articulation_points(Graph))