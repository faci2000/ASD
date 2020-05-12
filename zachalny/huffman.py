class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.val=None

def add_to_stack(Stack,i,value):
    Stack[i].val=value
    while (i//2)>0:
        if Stack[i//2].val>Stack[i].val:
            Stack[i//2],Stack[i]=Stack[i],Stack[i//2]
        else:
            break
        i//=2
            
def push_down(Cheap,size):
    temp=1
    while (temp*2)<size:
        if Cheap[temp*2].val<Cheap[temp].val:
            if (Cheap[temp*2].val<Cheap[temp*2+1].val)or((temp*2+1)>=(size)):
                Cheap[temp],Cheap[temp*2]=Cheap[temp*2],Cheap[temp]
                temp*=2
            else:
                Cheap[temp],Cheap[temp*2+1]=Cheap[temp*2+1],Cheap[temp]
                temp=temp*2+1
        elif Cheap[temp*2+1].val<Cheap[temp].val and(temp*2+1)<(size):
            Cheap[temp],Cheap[temp*2+1]=Cheap[temp*2+1],Cheap[temp]
            temp=temp*2+1
        else:   
            break

def almost_dfs_count(node,depth):
    if node.right==None and node.left==None:
        return depth*node.val
    elif node.right!=None and node.left!=None:
        return almost_dfs_count(node.left,depth+1)+almost_dfs_count(node.right,depth+1)
    elif node.left!=None:
        return almost_dfs_count(node.left,depth+1)
    else:
        return almost_dfs_count(node.right,depth+1)


def huffman_len(Tab):
    if len(Tab)==1:
        return Tab[0]
    Stack=[Node() for i in range(len(Tab)+1)]
    for i in range(len(Tab)):
        add_to_stack(Stack,(i+1),Tab[i])
    length=len(Stack)-1
    for i in range(length-1):
        Stack[1],Stack[length-i]=Stack[length-i],Stack[1]
        push_down(Stack,length-i)
        item = Node()
        item.left=Stack[1]
        item.right=Stack[length-i]
        item.val=Stack[1].val+Stack[length-i].val
        Stack.append(item)
        Stack[1],Stack[len(Stack)-1]=Stack[len(Stack)-1],Stack[1]
        push_down(Stack,length-i)
    return almost_dfs_count(Stack[1],0)

# elementarny test, powinien wypisać 2600
print( huffman_len([ 100] ))