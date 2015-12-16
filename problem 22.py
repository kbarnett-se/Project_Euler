"""
PROG::problem22.py
AUTHOR::Kevin.P.Barnett
DATE::DEC.8.2015
"""

def formList(fileName):
    retList = {}
    lst = ""
    for name in open(fileName):
        lst = name.strip().split(",")
    for item in range(len(lst)):
        retList[lst[item].strip("\"")] = ordCount(lst[item].strip("\""))
    return list(retList.items())

def ordCount(name):
    total = 0
    for let in name:
        total += ord(let)-ord('A')+1
    return total

def main():
    total = 0
    list = formList("testNames.txt")
    list = sorted(list, key=lambda name: name[0])
    for item in range(len(list)):
        total += (item+1) * list[item][1]
    print(total)

if __name__ == "__main__":
  main()
