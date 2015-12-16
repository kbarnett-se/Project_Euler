"""
PROG::problem11.py
AUTHOR::Kevin P. Barnett
DATE::Oct.22.2015
"""
def numListMake(fileName, list):
    for lines in open(fileName):
        list.append(lines.split())
    for lists in list:
        for vals in range(len(lists)):
            lists[vals] = int(lists[vals])

def evalFourInRow(list):
    retList = []
    #list[line][valInLine]
    for line in range(20):
        for val in range(20):
            if val < 17:
                retList.append(list[line][val]*list[line][val+1]*list[line][val+2]*list[line][val+3])
            if line < 17 and val < 17:
                retList.append(list[line][val]*list[line+1][val+1]*list[line+2][val+2]*list[line+3][val+3])
            if line < 17:
                retList.append(list[line][val]*list[line+1][val]*list[line+2][val]*list[line+3][val])
            if line < 17 and val > 2:
                retList.append(list[line][val]*list[line+1][val-1]*list[line+2][val-2]*list[line+3][val-3])
    return retList

def retHighVal(list):
    high = 0
    for vals in list:
        if vals > high:
            high = vals
    return high

def main():
    list = []
    numListMake("prob11nums.txt", list)
    list = evalFourInRow(list)
    for val in list:
        print(val)
    print("Highest 4 in Row: ", retHighVal(list))
if __name__ == "__main__":
  main()
