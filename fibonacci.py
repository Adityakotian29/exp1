def recursive_fibonacci(n):
   
    if n <= 2:
        return 1
    else:
        
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
position = 5  
result_recursive = recursive_fibonacci(position)
print(f"The Fibonacci sequence value at position {position} (calculated recursively) is: {result_recursive}")


def iterative_fibonacci(n):
    fib_sequence = [1, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence
position = 5 
result_iterative = iterative_fibonacci(position)
print(f"The Fibonacci sequence values up to position {position} (calculated iteratively) are: {result_iterative}")
