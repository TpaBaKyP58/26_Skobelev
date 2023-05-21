[200~numlist = list(int(x) for x in "57383502919374282019465759391572910475829238364859572924")

x = int(input())
firstelementindex = numlist.index(x)
newlist = tuple(numlist[firstelementindex:(numlist.index(x, firstelementindex+1))+1])
print(newlist)~ 
