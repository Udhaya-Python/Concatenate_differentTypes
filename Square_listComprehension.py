# res=[i**2 for i in range(1,5) if i>2]
# print(res)

# list=[1,4,3]
# list1=[2,4,5]
# common=[e for e in list for e1 in list1 if e==e1]
# print(common)

# uncommon=[(e,e1) for e in list for e1 in list1 if e!=e1]
# print(uncommon) 

num=[1,2,3,4]
res=[(num1**2,num1**3) for num1 in num ]
print(res)
