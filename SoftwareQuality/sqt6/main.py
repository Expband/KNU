import random
ListToChek = []
ListOfIndex = list()
i = 0
NeighborIndex = 1
numbersOfIteration = 100
while i < numbersOfIteration:
    ListToChek.append(random.randint(0,100))
    i = i + 1
print(ListToChek)
for i in range(1,len(ListToChek)):
    if ListToChek[i-1]<ListToChek[i]:
        ListOfIndex.append([ListToChek[i],i])
        print(ListToChek[i],i)




