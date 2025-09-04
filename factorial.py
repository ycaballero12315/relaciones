def factorial(n):
    if n == 0 or n == 1:
        return 1
    while(n):
        return n* factorial(n-1)
    
    
print(factorial(-1))