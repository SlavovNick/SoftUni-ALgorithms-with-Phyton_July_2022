def GetFibonacci(num):
    if num == 0 or num == 1:
        return 1
    return GetFibonacci(num - 2) + GetFibonacci (num - 1)

def iterative_fib(number):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result

n = int(input())

#print(GetFibonacci(n))
print(iterative_fib(n))
