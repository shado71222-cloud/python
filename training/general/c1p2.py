for i in range(1,100):
    n=i*i
    if n>20:
        print(i)
        break

for i in range(1,100):
    if i*4 == i*i:
        print(i)
        break

name="loading, loading, loading, get fucked lol"
for i in range(0,100):
    print(name[0:i])
    if i == len(name):
        break

name="loading, loading, loading, get fucked lol"
for i in range(0,len(name)):
    print(name[0:i])

name="loading, loading, loading, get fucked lol"
for i in range(0,len(name)):
    print(name[0:i])
    cs=name[i]
    if cs == 'c':
        break