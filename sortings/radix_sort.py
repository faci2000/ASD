def counting_sort(Words,left,right,index):
    Letters=[0 for i in range(25)]
    for i in range(left,right+1):
        Letters[ord(Words[i][index])-ord('a')]+=1

    for i in range(1,len(Letters)):
        Letters[i]+=Letters[i-1]

    Words_copy=['  ' for i in range(left,right+1)]
    for i in range(right,left-1,-1):
        Words_copy[Letters[ord(Words[i][index])-ord('a')]-1]=Words[i]
        Letters[ord(Words[i][index])-ord('a')]-=1

    for i in range(left,right+1):
        Words[i]=Words_copy[i-left]



def radix_sort(Words):
    mx = max(len(i) for i in Words)
    count_sort_by_lenght(Words,mx)
    for i in range((mx-1),-1,-1):
        j=0
        while( j< len(Words)):
            h=j
            while h<len(Words) and len(Words[h])>=(i+1):
                h+=1
            if(h-j>1):
                counting_sort(Words,j,h-1,i)
            if h!=j:
                j=h
            else:
                j+=1
    return Words
            
def count_sort_by_lenght(Words,mx):
    counter_arr=[0 for i in range(mx)]
    
    for i in range(len(Words)):
        counter_arr[len(Words[i])-1]+=1
    
    for i in range(1,mx):
        counter_arr[i]+=counter_arr[i-1]

    Words_copy=['  ' for i in range(len(Words))]
    for i in range(len(Words)-1,-1,-1):
        Words_copy[counter_arr[len(Words[i])-1]-1]=Words[i]
        counter_arr[len(Words[i])-1]-=1

    for i in range(len(Words)):
        Words[i]=Words_copy[i]

tab=["aab","asdf","aaaa","aaca","aa","asbcd","asbca"]
print(radix_sort(tab))