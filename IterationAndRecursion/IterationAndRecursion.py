#KalvinBlowe #CIS261 #IterationAndRecursion
#iteration
def factorial_iterative_while(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result 
#recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


