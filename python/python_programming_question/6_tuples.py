from operator import itemgetter, attrgetter

data = []
print(" name, age, and score  ")
while True:
    strdata = input()
    if not strdata:
        break
    data.append(tuple(strdata.split(",")))

print(sorted(data,key=itemgetter(0, 1, 2)))