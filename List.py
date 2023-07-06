# emp_no=[3321,3322,3323,3324,3325]
# print(emp_no)
# emp=[]
# for emp in emp_no:
#     if emp%2==0:
#         print(emp)

# List comprehension-> to write a concise line to create new sequences.
# emp_no=[3321,3322,3323,3324,3325]
# emp_comprehension =[emps for emps in emp_no if emps%2==0]
# print(emp_comprehension )

# num=[i for i in range(1,30) if i in 6]
# print(num)

string = "Practice Problems to Drill List Comprehension in Your Head."
countstring=len([i for i in string])
print(countstring)

# count=len([i for i in string if i==" "])
# print(count)

# space=[c for c in string if c.lower() not in "aeiou"]
# print(space)

# for c in string:
    # if c.split(" "):
        # print(c)