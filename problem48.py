"""
PROG::problem48.py
AUTHOR::Kevin.P.Barnett
DATE::Dec.14.2015
"""

def pow(x, y):
    ret = 1
    for meh in range(y):
        ret*=x
    return ret

def main():
    tot = 0
    for val in range(1, 1001):
        tot += pow(val, val)
    print(tot)

if __name__ == "__name__":
    main()
