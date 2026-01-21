prices = ["25$","50$","48ILS","34$","25$","100ILS"]
dollars =[]
nis=[]
for i in prices:
    if "$" in i:
        i = int(i.replace("$", "")) * 1.2
        dollars.insert(0,i)
    elif "ILS" in i:
        i = int(i.replace("ILS", "")) * 1.18
        nis.append(i)

print(dollars)
print(nis)