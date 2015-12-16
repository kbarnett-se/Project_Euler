"""
PROG::problem13.py
AUTHOR::Kevin.P.Barnett
DATE::Nov.3.2015
"""

def getNums(fileName):
    """
    :param fileName: file containing numbers for problems 13
    :return: list containing numbers
    """
    retList = []
    for line in open(fileName):
        retList.append(int(line.strip()))
    return retList

def add(list):
    """
    :param list: list containing numbers to be added
    :return: total
    """
    total = 0
    for vals in list:
        total += vals
    return total

def main():
    print("Total Value is: ", add(getNums(input("Enter File to Grab Numbers From: "))))

if __name__ == "__main__":
    main()
