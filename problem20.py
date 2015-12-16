"""
PROG::problem20.py
AUTHOR::Kevin.P.Barnett
DATE::Nov.2.2015
"""

def factorial(n):
    total = 1
    for vals in range(1, n+1):
        total *= vals
    return total

def addDigits(num):
    total = 0
    for digits in str(num):
        total += int(digits)
    return total

def main():
    n = int(input("Enter a Max Range: "))
    print("Sum of Factorials Below(", n, ") is: ", addDigits(factorial(n)))

if __name__ == "__main__":
    main()
