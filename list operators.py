print("\n\n\t\t\tlist operators")
l=[1,2,3,4,5,6,2,1,4,8,0,5,1]
i=[123,700,600,789]
print("List <l>:",l)
print("List <i>:",i)
print("\nLengt of list <l>:",len(l))
print("\nMaixmum value in the list l:",max(l))
print("Minimum value in the list l:",min(l))
i.append(2000)
print("\nAfter adding 2000 to the list i:",i)
print("\nCounting the number of times 1 is repeated in list l:",l.count(1))
a=[145,678,867]
print("\nlist a:",l)
i.extend(a)
print("\nextending list i with list a",i)
print("\nShowing the position of 789 in the list i:",i.index(789))
i.insert(4,3000)
print("\nAfter adding 3000 to the list i in index 4:",i)
l.remove(3)
print("\nAter removing 3 from list l:",l)
l.reverse()
print("\nAfter reversing the list l:",l)
l.sort()
print("\nater sorting list l:",l)