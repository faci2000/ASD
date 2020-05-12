import argparse
from random import randrange
def quickSort(tab,left,right):
    if (right-left)>0:
        middle_l,middle_r = partition(tab,left,right)
        quickSort(tab,left,middle_r)
        quickSort(tab,middle_l,right)

def partition(tab, left, right):
    pivot=tab[randrange(right-left)+left]
    while left<=right:
        while tab[left]<pivot and left<=right:
            left+=1
        while tab[right]>pivot and left<=right:
            right-=1
        if left<=right:
            tab[left],tab[right]=tab[right],tab[left]
            left+=1
            right-=1
    return left,right


CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--list",
  nargs="*", 
  type=int,
  default=[1,2,3], 
)
args = CLI.parse_args()

#print(args.list)
quickSort(args.list,0,len(args.list)-1)
print(args.list)
