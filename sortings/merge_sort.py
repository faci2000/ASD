from random import randrange

def merge(tabA,tabB):
    tabC=[0]*(len(tabA)+len(tabB))
    a=0;b=0;c=0
    while a<len(tabA) or b<len(tabB):
        if(a<len(tabA) and b<len(tabB)):
            if(tabA[a]<=tabB[b]):
                tabC[c]=tabA[a]
                c+=1
                a+=1
            else:
                tabC[c]=tabB[b]
                c+=1
                b+=1
        elif(a<len(tabA)):
            tabC[c]=tabA[a]
            c+=1
            a+=1
        else:
            tabC[c]=tabB[b]
            c+=1
            b+=1
    return tabC

def recursive_merge_sort(tab):
    if len(tab)==1:
        return tab
    tabA=recursive_merge_sort(tab[:len(tab)//2])
    tabB=recursive_merge_sort(tab[len(tab)//2:])
    return merge(tabA,tabB)

# def itrative_merge_sort(tab):
#     current_size=1
#     while current_size<len(tab):
#         left=0
#         while left<len(tab)-1:
#             mid=min(current_size+left,len(tab)-1)
#             right=min(mid+current_size,len(tab)-1)
#             #merge dla tab
#             left=right+1
#         current_size*=2
        

tabA=[randrange(50) for i in range(10)]
tabB=tabA
tabB=recursive_merge_sort(tabB)
tabA.sort()
print(tabA)
print(tabB)