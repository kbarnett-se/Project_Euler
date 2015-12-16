"""
PROG::problem12.py
AUTHOR::Kevin.P.Barnett
DATE::Nov.5.2015
"""
import math

def numOfDiv(num):
    divs = 2
    if math.floor(math.sqrt(num)) == math.sqrt(num):
        return 0
    for div in range(2, math.floor(math.sqrt(num))+1):
        if num % div == 0:
            divs += 2
    return divs

def findHighDiv(numDiv):
    for i in range(1000000000000):
        if numOfDiv(int(.5*i*(i+1))) > numDiv:
            return .5*i*(i+1)

def main():
    x = int(input("Enter Number of Divisors: "))
    print("Triangle Number With (", x, ") Many Divisors: ", findHighDiv(x))

if __name__ == "__main__":
  main()
