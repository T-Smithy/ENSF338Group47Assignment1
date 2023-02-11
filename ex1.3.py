fib_cache = {}

def mem_func(n):
    if n==1 or n==0:
        return n
    if n not in fib_cache:
        fib_cache[n] = mem_func(n-1) + mem_func(n-2)
    return fib_cache[n]

# Tests memoization-optimized function for inputs 1 - 35.
def main():
    for x in range (1,36):
        y = mem_func(x)
        print("Fibonacci number", x, ":", y)
    
if __name__ == main():
    main()
