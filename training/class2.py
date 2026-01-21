# for i in range(0,11):
#     print(3*i)
#
#
# summery = 0
# count = 0
# for i in range (1,11):
#     summery = summery + i
#     count += 1
#

# avg= summery/count
# print (avg)
#
# nums = [23,45,234,565,67,66,1,1,1,3]
# summery_list = 0
# for num in nums:
#     summery_list = summery_list + num
#
# amount= len(nums)
# avg_list= summery_list/amount
# print (avg_list)
#




# mails = ["abc@aa.com","ssss.com","sss@rerrr.com"]
# for mail in mails:
#     if "@"  in mail:
#         print(f"{mail} is a valid mail")
#     else:
#         print(f"{mail} is not a valid mail")
#         mails.remove(mail)





# evens=0
# odds=0
# lists=[1,2,3,4,5,6,7,8,9,10]
# for i in lists:
#     if i%2==0:
#         print(f"{i} is even")
#         evens+=i
#     else:
#         print(f"{i} is odd")
#         odds+=i
# print(f"the total of even numbers is {evens} and the total of  odd numbers is {odds}")
#
# citys2=["get","good"]
# if citys2[0] in citys2[1]:
#     print(f"{citys2[0]} is in {citys2[1]}")
# else :
#     print(f"{citys2[0]} is not in {citys2[1]}")


for i in range(1,31):
    if i%7==0 or "7" in str(i):
        print(i)


person= {
    "first_name":"John",
    "last_name":"Doe",
    "age":34,
    "is_singer":True

}

print(person["first_name"])
print(person["last_name"])
print (person["age"])
person["age"] = 33
