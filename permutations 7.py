from itertools import permutations
list1=[]
m=int(input("enter the number of values to be entered in a list"))
for i in range(0,m):
    h=int(input())
    list1.append(h)
l = list(permutations(list1))
print(l)
