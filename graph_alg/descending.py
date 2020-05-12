max_val =100
def true_dfs(Graph,x,y,last_val):      
    if x==y:
        return True         
    for i in range(len(Graph[x])):         
        if Graph[x][i][1]<last_val:
            if true_dfs(Graph,Graph[x][i][0],y,Graph[x][i][1]):
                return True
            else:
                return False


G = [[(1,7),(2,1)],[(0,7),(2,4),(3,8)],[(3,2),(1,4),(0,1)],[(2,2),(1,8)]]
print( true_dfs(G,0,3,max_val) )