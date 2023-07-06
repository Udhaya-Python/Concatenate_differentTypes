
# emp_name=['udhaya','saravana','mani']
# name=[emp.upper() for emp in emp_name]
# print(name) 

# name1=[i for i in emp_name if i=='mani']
# print(name1)

words="This is my LAptop"
vowels=[i for i in words if i.lower() in 'aeiou']
print(vowels)

name=['arp','strong']
name1=['argument','sharp','armstrong']

name2=[n1 for n in name for n1 in name1 if n in n1]
print(name2)