def sort_first(value):
    return value[0]

def tasks(Classes):
    if len(Classes)==0:
        return 0
    Classes.sort(key=sort_first)
    taken=1
    last_taken=0
    for index,lesson in enumerate(Classes):
        if Classes[last_taken][1]<=lesson[0]:
            taken+=1
            last_taken=index
        elif Classes[last_taken][1]>lesson[1]:
            last_taken=index    
    return taken

# elementarny test, powinien wypisać 2
print( tasks([   (0,10), (10,20), (5,15)  ] ))