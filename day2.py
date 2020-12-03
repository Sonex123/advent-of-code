def part1():
    l = []
    for i in open("day2").readlines():
        x=i.replace("\n","").split(":")
        l.append(x)
    x=0
    for i in l:
        v=i[0]
        pw=i[1]
        v=v.split()
        mindestens = int(v[0].split("-")[0])
        höchstens = int(v[0].split("-")[1])
        c = pw.count(v[1])
        if c>=mindestens and c<=höchstens:
            x+=1
    print(x)

def part2():
    l=[]
    for i in open("day2").readlines():
        x=i.replace("\n","").split(":")
        l.append(x)
    x = 0
    for i in l:
        v=i[0]
        pw=i[1]
        v=v.split()
        pos1 = int(v[0].split("-")[0])
        pos2 = int(v[0].split("-")[1])
        searched = v[1]
        if pw[pos1]==searched and pw[pos2]==searched or pw[pos1]!=searched and pw[pos2]!=searched:
            x+=1
    print(1000-x)