
import tfidf


def transfer(word, no):
    li = []
    for i in range(no):
        li.append(word)
    return li


sport = []

f = open("sport.txt", "r")
for x in f:
    g = x.split("   ")

    li = transfer(g[0], int(g[1][:-1]))
    sport.extend(li)

print(sport)
food = []

f = open("food.txt", "r")
for x in f:
    g = x.split("   ")

    li = transfer(g[0], int(g[1][:-1]))
    food.extend(li)


a,b = tfidf.run(sport,food)



ggg = sorted(a.items(), key =
            lambda kv:(kv[1], kv[0]))
with open("sporttf2.txt", mode='w') as f:
    for k,v in ggg:
        f.write( ("%s   %s\n") % (k,v))
print("######################################################")

lll = sorted(b.items(), key =
            lambda kv:(kv[1], kv[0]))

with open("foodttf2.txt", mode='w') as f:
    for k,v in lll:
        f.write( ("%s   %s\n") % (k,v))