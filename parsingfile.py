
op=open("C:/Users/UdhayaParanthaman/Documents/MAP in Python.txt","r")
# print(op)
output=[i for i in op if "what" in i]
print(output)
op.close