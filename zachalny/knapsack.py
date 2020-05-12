def sort_first(value):
    return value[0]

def knapsack(A, k):
    Tab=[(A[i][0]/A[i][1],i) for i in range(len(A))]
    Tab.sort(key=sort_first,reverse=True)
    temp_poj=0
    temp_val=0
    i=0
    while i<len(A) and temp_poj+A[Tab[i][1]][1]<=k:
        temp_poj+=A[Tab[i][1]][1]
        temp_val+=A[Tab[i][1]][0]
        i+=1
    if(i<len(A)):
        temp_val+=Tab[i][0]*(k-temp_poj)
    return temp_val

# elementarny test, powinien wypisać 12
print( knapsack( [  (1,1), (10,2), (6,3)  ], 3 ))
