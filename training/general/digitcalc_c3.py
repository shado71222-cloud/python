nums=[123,241,34]
for i in nums:
    l=str(i)
    if len(l) == 3:
        total = int(l[0]) + int(l[1]) + int(l[2])
        print(total)
    else :
        print("not a valid number")

for i in nums:
    if len(str(i)) == 3:
        total = sum(int(digit) for digit in str(i))
        print(total)
    else :
        print("not a valid number")

#ai
for i in nums:
    if len(s := str(i)) == 3:
        total = sum(int(d) for d in s)
        print(total)