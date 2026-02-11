fn= "dor aharoni"
space= fn.index(" ")
firstname=fn[:space]
lastname=fn[space+1:]
if len(firstname)>len(lastname):
    print(f"{firstname} is longer than {lastname}")
else:
    print(f"{lastname} is longer or equal to {firstname}")

grade=90
if grade<50:
    ngrade=grade*1.1
if grade>=50 and grade<=80:
    print(f"your grade is {grade}")
if grade>80:
    grade=grade+20
    print(f"your grade is {grade}")