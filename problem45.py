"""
PROG::problem45.py
AUTHOR::Kevin.P.Barnett
DATE::Dec.8.2015
"""

def triag(n):
    return n*(n+1)//2

def pentag(n):
    return n*((3*n)-1)//2

def hexag(n):
    return n*((2*n)-1)//1

def valCompare():
    tList, pList, hList= [], [], []
    for x in range(2,100000):
        tList.append(triag(x))
        pList.append(pentag(x))
        hList.append(hexag(x))
        if (val in pList) and (val in tList):
            if val != 40755:
                return val

def main():
    print("Num is:", valCompare())

if __name__ == "__main__":
    main()
