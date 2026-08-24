# Memoization Method

memo = {}

def fib(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


while True:
    num = int(input("Enter Number: "))

    if num < 0:
        print("Please enter a non-negative number.")
    else:
        print("Fibonacci Number of", num, ":", fib(num))