


tab=[2,2,4,8,1,8,16]
tab.sort()
cap=27

i=len(tab)-1
while(i>=0):
    if cap>=tab[i]:
        print(tab[i])
        cap-=tab[i]
    i-=1


