with open("day6") as f:
    groops=f.read().split("\n\n")
c=0
for groop in groops:
    persons=groop.split("\n")
    already=""
    for person in persons:
        for letter in person:
            if letter not in already:
                already+=letter
                c+=1
print(c)