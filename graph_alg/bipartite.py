def true_dfs(Graph,Color,x):              
    for i in range(len(Graph[x])):         
        if Color[Graph[x][i]]==0:
            Color[Graph[x][i]]=Color[x]*-1
            if true_dfs(Graph,Color,Graph[x][i]):
                
        elif Color[Graph[x][i]]==Color[x]:
            return false