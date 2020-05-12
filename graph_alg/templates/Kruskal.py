from random import randrange
def quickSort(tab,left,right):
    if (right-left)>0:
        middle_l,middle_r = partition(tab,left,right)
        quickSort(tab,left,middle_r)
        quickSort(tab,middle_l,right)

def partition(tab, left, right):
    pivot=tab[randrange(right-left)+left][2]
    while left<=right:
        while tab[left][2]<pivot and left<=right:
            left+=1
        while tab[right][2]>pivot and left<=right:
            right-=1
        if left<=right:
            tab[left],tab[right]=tab[right],tab[left]
            left+=1
            right-=1
    return left,right


def find_set(Parent,Rank,vert):
    if(Parent[vert]==vert):
        return vert
    Parent[vert]=find_set(Parent,Rank,Parent[vert])
    Rank[vert]=1
    return Parent[vert]
    

def union_sets(Parent,Rank,vert_a,vert_b):
    if Rank[vert_a]>Rank[vert_b]:
        if Parent[vert_b]!=vert_b:
            Parent[Parent[vert_b]]=Parent[vert_a]
            Rank[Parent[vert_b]]=Rank[vert_a]
            Rank[vert_b]=Rank[Parent[vert_b]]+1
        else:
            Parent[Parent[vert_b]]=Parent[vert_a]
            Rank[vert_b]=Rank[Parent[vert_b]]+1
    else:
        if Parent[vert_a]!=vert_a:
            Parent[Parent[vert_a]]=Parent[vert_b]
            Rank[Parent[vert_a]]=Rank[vert_b]
            Rank[vert_a]=Rank[Parent[vert_a]]+1
        else:
            Parent[Parent[vert_a]]=Parent[vert_b]
            Rank[vert_a]=Rank[Parent[vert_a]]+1


def kruskal(Graph,vertices):
    quickSort(Graph,0,len(Graph)-1)
    Parent = [i for i in range(vertices)] #creating own sets
    Rank = [0 for i in range(vertices)]
    MST=[[] for i in range(vertices)]
    MST_cost=0
    for i in range(len(Graph)):
        if find_set(Parent,Rank,Graph[i][0])!=find_set(Parent,Rank,Graph[i][1]):
            union_sets(Parent,Rank,Graph[i][0],Graph[i][1])
            MST[Graph[i][0]].append((Graph[i][1],Graph[i][2]))
            MST[Graph[i][1]].append((Graph[i][0],Graph[i][2]))
            MST_cost+=Graph[i][2]
    print(MST)
    print(MST_cost)

            

    
vertices=8
Graph=[ (0, 1, 5), (0, 3, 9), (0, 6, 3),
        (1, 2, 9), (1, 4, 8), (1, 5, 6), (1, 7, 7),
        (2, 3, 9), (2, 4, 4), (2, 6, 5), (2, 7, 3),
        (3, 6, 8),
        (4, 5, 2), (4, 6, 1),
        (5, 6, 6),
        (6, 7, 9)]
kruskal(Graph,vertices)