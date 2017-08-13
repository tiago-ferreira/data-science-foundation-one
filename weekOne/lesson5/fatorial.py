# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    result, i = 1,1
    while(i <= n):
        result = result * i
        i += 1
    return result



print(factorial(4))
#>>> 24
print(factorial(5))
#>>> 120
print(factorial(6))
#>>> 720