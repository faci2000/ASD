def Compute_cost(Cost,Val,i,j):
    for x in range(-1,2,2):
        if i+x>=0 and i+x<=len(Cost):
            if Cost[i+x][j]>Val[i+x][j]+Cost[i][j]:
                Cost[i+x][j]=Val[i+x][j]+Cost[i][j]
        if j+x>=0 and j+x<=len(Cost):
            if Cost[i][j+x]>Val[i][j+x]+Cost[i][j]:
                Cost[i][j+x]>Val[i][j+x]+Cost[i][j]
         
def add_to_heap(Stack,i,value):
    Stack[i].val=value
    while (i//2)>0:
        if Stack[i//2].val>Stack[i].val:
            Stack[i//2],Stack[i]=Stack[i],Stack[i//2]
        else:
            break
        i//=2

def kings_path( A ):
    Cost = [(6*(len(A)*len(A[0])),i%(len(A)),i//len(A)) for i  in range(len(A)*len(A[0]))] 
    Prev = [[-1 for i  in range(len(A[0]))] for j in range(len(A))]
    To_take =[[True for i  in range(len(A[0]))] for j in range(len(A))]
    add_to_heap(Cost,0,0,A[0][0])
    #To_take[0][0]=False
    #for i in range((len(A)*len(A[0]))):
     #   for j in range((len(A)*len(A[0]))):






# policz koszt trasy
A = [[1,1,2],
     [5,1,3],
     [4,1,1]]
print( kings_path( A ) ) # wypisze 5