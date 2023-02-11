import timeit

# 'Cache' for memoization of mem_func()
fib_cache = {}

# Memoization-optimized function
def mem_func(n):
    if n==1 or n==0:
        return n
    if n not in fib_cache:
        fib_cache[n] = mem_func(n-1) + mem_func(n-2)
    return fib_cache[n]

# Original function
def func(n):
    if n==1 or n==0:
        return n
    else: 
        return func(n-1) + func(n-2)

# Tests the functions for inputs 1 - 35.
# Times computations and outputs results to terminal.
def main():
    print("\n--- TESTING ORIGINAL FIBONACCI FUNCTION ---\n")
    for x in range (1,36):
        timer = timeit.timeit(lambda: func(x), number=1)
        print("Time used for Fibonacci number", x, ":", timer, "seconds.")
        #print(timer)
    print("\n--- TESTING MEMOIZATION-OPTIMIZED FIBONACCI FUNCTION ---\n")
    for x in range (1,36):
        timer = timeit.timeit(lambda: mem_func(x), number=1)
        print("Time used for Fibonacci number", x, "using memoization:", timer, "seconds.")
        #print(timer)
if __name__ == main():
    main()