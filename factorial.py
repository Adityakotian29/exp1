def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
number = int(input("Enter a number to calculate its factorial: "))
result_iterative = iterative_factorial(number)
print(f"The factorial of {number} (calculated iteratively) is: {result_iterative}")



def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        
        return n * recursive_factorial(n - 1)
number = int(input("Enter a number to calculate its factorial: "))
result_recursive = recursive_factorial(number)
print(f"The factorial of {number} (calculated recursively) is: {result_recursive}")
