name1='Udhaya'
lname='kumar'
print('My name is '+name1+lname)

name='kumaran'
score=20
company='Infotech'
# Cast to string
print(name+" Secured "+str(score)+" marks")

# Interpolation
print(name+" Secured %d"%(score)+" marks")

# String format
print(name+" Secured {}".format(score)+" marks")

print("Your company name is {i1} {i2}".format(i1=name1,i2=company))
# f-string
print(name+f" Secured {score} marks")

