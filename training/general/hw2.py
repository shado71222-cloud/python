nums = [1,88,5,13,8,123,76,12]
new = []
while len(nums) > 0:
    max=nums[0]
    for i in nums:
        if i > max:
            max=i
    new.insert(0,max)
    nums.remove(max)

print(new)


person1= {
    "first_name":"luffy",
    "last_name":"monkey.d",
    "age":19,
}
person2= {
    "first_name":"robin",
    "last_name":"nico",
    "age":30,
}
if person1["age"]>person2["age"]:
    print(f"{person1["first_name"]} is older")
elif person1["age"]<person2["age"]:
    print(f"{person2["first_name"]} is older")
else:
    print("both are the same age")

if len(person1["first_name"])>len(person2["first_name"]):
    print(person1["len.first_name"])
elif len(person1["first_name"])<len(person2["first_name"]):
    print(person2["len.first_name"])
else:
    print("both first names are the same length")