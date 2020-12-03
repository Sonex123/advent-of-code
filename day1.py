def part1():
    l = []
    for i in open("day1").readlines():
        l.append(int(i.replace("\n","")))

    for i in l:
        for x in l:
            if i+x==2020:
                print(i*x)

def part2():
    l = []
    for i in open("day1").readlines():
        x=int(i.replace("\n",""))
        l.append(x)

    for i in l:
        for x in l:
            for z in l:
                if i+x+z==2020:
                    print(i*x*z)