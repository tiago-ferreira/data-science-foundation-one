# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def bigger(x , y):
    if(x > y):
        return x
    return y

def biggest(x, y, z):
    big = bigger(x, y)
    result = bigger(big, z) 
    return result


print(biggest(3, 6, 9))
#>>> 9

print(biggest(6, 9, 3))
#>>> 9

print(biggest(9, 3, 6))
#>>> 9

print(biggest(3, 3, 9))
#>>> 9

print(biggest(9, 3, 9))
#>>> 9

print(biggest(2, 2, 1))
#>>> 9

print(biggest(1, 2, 2))
#>>> 9

print(biggest(2, 2, 2))
#>>> 9