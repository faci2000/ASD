def knapsack2d( V, max_w, max_h ):
    Thebest=[[[0 for i in range(max_h+1)]for j in range(max_w+1)] for h in range(len(V)+1)]
    for i in range(1,len(V)+1,1):
        for w in range(1,max_w+1,1):
            for h in range(1,max_h+1,1):
                if V[i-1][1]<=w and V[i-1][2]<=h:
                    Thebest[i][w][h]=max(Thebest[i-1][w-V[i-1][1]][h-V[i-1][2]]+V[i-1][0],Thebest[i-1][w][h])
                else:
                    Thebest[i][w][h]=Thebest[i-1][w][h]
    return Thebest[len(V)][max_w][max_h]

# tu proszę umieścić swoją implementację
P = [(5,10,3), (7,8,12), (2,7,3)]#wartosc,waga,wysokosc
print( knapsack2d( P, 16, 15 ))