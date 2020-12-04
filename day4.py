def part1():
    valids=0
    with open("day4") as f:
        x=f.read().replace(" ",";").split("\n\n")
    for i in x:
        x[x.index(i)]=i.replace("\n",";")
    for i in x:
        _list=[]
        byr,iyr,eyr,hgt,hcl,ecl,pid=False,False,False,False,False,False,False
        for a in i.split(";"):
            _list.append(a.split(":"))
        for i in _list:
            if i[0]=="byr":byr=True
            if i[0]=="iyr":iyr=True
            if i[0]=="eyr":eyr=True
            if i[0]=="hgt":hgt=True
            if i[0]=="hcl":hcl=True
            if i[0]=="ecl":ecl=True
            if i[0]=="pid":pid=True
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valids+=1
    print(valids)

def part2():
    valids=0
    with open("day4") as f:
        x=f.read().replace(" ",";").split("\n\n")
    for i in x:
        x[x.index(i)]=i.replace("\n",";")
    for i in x:
        _list=[]
        byr,iyr,eyr,hgt,hcl,ecl,pid=False,False,False,False,False,False,False
        for a in i.split(";"):
            _list.append(a.split(":"))
        for i in _list:
            if i[0]=="byr":
                if int(i[1])<2003 and int(i[1])>1919:
                    byr=True
            if i[0]=="iyr":
                if int(i[1])<2021 and int(i[1])>2009:
                    iyr=True
            if i[0]=="eyr":
                if int(i[1])<2031 and int(i[1])>2019:
                    eyr=True
            if i[0]=="hgt":
                e=i[1][-1]
                if e=="m":
                    x=int(i[1].replace("cm",""))
                    if x<194 and x>149:
                        hgt=True
                elif e=="n":
                    x=int(i[1].replace("in",""))
                    if x<77 and x>58:
                        hgt=True
            if i[0]=="hcl":
                x=i[1]
                if len(x)==7:
                    if x[0]=="#":
                        for y in range(1,len(x)-1):
                            if x[y] in list("0123456789abcdef"):
                                hcl=True
            if i[0]=="ecl":
                val="amb blu brn gry grn hzl oth".split()
                if i[1] in val:
                    ecl=True
            if i[0]=="pid":
                if len(i[1])==9:
                    pid=True
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valids+=1
    print(valids)