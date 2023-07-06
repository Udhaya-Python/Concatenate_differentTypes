lis=[5]
for i in lis:
    for j in range(1,i):
        i=i*j
    print(i)

res=[i*j for i in lis for j in range(1,i)]
print(res)



