def count_down(n, depth=0):
    print("" * depth, f"Call depth: {depth}, n = {n}")
    if n == 0:
        return
    
    count_down(n - 1,depth + 1)
    

def recursive_sum(n, depth=0):
    print("" * depth, f"Call depth: {depth}, n = {n}")

    if n == 0:
        return 0
    
    return n + recursive_sum(n - 1, depth + 1)


def fib(n, depth=0):
     
    print("" * depth, f"Call depth: {depth}, n = {n}")
    if n <= 1:
        return n
    
    return fib(n - 1, depth + 1) +  fib(n - 2, depth + 1)

count_down(5)
print("sum =", recursive_sum(5))
print("fibonacci(5)", fib(5))