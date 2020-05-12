from random import randrange
# def partition(list, poczatek, koniec):
#     pivot=list[koniec]
#     i=poczatek
#     for j in range(poczatek,koniec):
#         if list[j]<=pivot:
#             i+=1
#             list[i], list[j]=list[j], list[i]
#     list[i+1],list[koniec]=list[koniec], list[i+1]
#     return i+1

# def partition(arr,left, right, pivotValue):
#     for i in range(left,right):
#         if arr[i] == pivotValue:
#             arr[i],arr[right]=arr[right],arr[i]
#             break
#     i = left
#     for j in range (left, right):
#         if arr[j]<= pivotValue:
#             arr[i],arr[j] = arr[j], arr[i]
#             i+=1
#     arr[i],arr[right] = arr[right],arr[i]

def partition(tab, left, right):
    pivot=median_of_medians(tab[left:(right+1)])
    while left<right:
        while tab[left]<pivot and left<right:
            left+=1
        while tab[right]>=pivot and left<right:
            right-=1
        if left<=right:
            tab[left],tab[right]=tab[right],tab[left]
            # left+=1
            # right-=1
    return left

def find_median_in_five(Tab,left,right):
    for i in range(3):
        for j in range(left,right-i-1):
            if Tab[j]>Tab[j+1]:
                Tab[j],Tab[j+1]=Tab[j+1],Tab[j]
    return Tab[(left+right)//2]        

def median_of_medians(Tab):
    if len(Tab)==1:
        return Tab[0]
    if len(Tab)%5==0:
        Median_tab=[None for i in range(len(Tab)//5)]
    else:
        Median_tab=[None for i in range(len(Tab)//5+1)]
    for i in range(0,len(Tab),5):
        Median_tab[i//5]=find_median_in_five(Tab,i,min(i+5,len(Tab)-1))
    return median_of_medians(Median_tab)

def quick_select(tab,index_to_find):
    left=0
    right=len(tab)-1
    while(True):
        middle=partition(tab,left,right)
        if(middle<index_to_find):
            left=middle+1
        elif middle>index_to_find:
            right=middle-1
        else:
            return tab[middle]


tab=[randrange(10)for i in range(10)]
print(tab)
print(quick_select(tab,2))