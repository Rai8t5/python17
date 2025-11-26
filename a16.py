
def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n - 1)

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

count_down(5)
print("sum of 1 to 5 is :",recursive_sum(5))
print("fibonacci(5)", fib(5))
print("fibonacci(10)", fib(10))