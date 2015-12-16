"""
PROG::problem25.py
AUTHOR::Kevin.P.Barnett
DATE::Nov.19.2015
"""
def fib(fib1, fib2):
    return fib2, fib1+fib2

def power(x, y):
    ret = 1
    for val in range(y):
        ret *= x
    return ret

def main():
    fib1, fib2 = 1, 1
    idCount = 2
    high = power(10, 999)
    while not(fib2 > high):
        fib1, fib2 = fib(fib1, fib2)
        idCount += 1
    print(idCount)

if __name__ == "__name__":
    main()
