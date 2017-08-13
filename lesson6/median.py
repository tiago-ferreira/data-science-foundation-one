# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if(a > b):
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def lower(a,b):
    if(a < b):
        return a
    else:
        return b

def lowest(a,b,c):
    return lower(a, lower(b,c))

def has_two_equals(a,b,c):
    if(a == b):
        return a
    elif(b == c):
        return b
    else:
        return -1
    

def median(a,b,c,):
    result = a
    lower = lowest(a,b,c)
    bigger = biggest(a,b,c)
    if(a == b and b == c):
        result = a
    elif(has_two_equals(a,b,c) != -1):
        result = has_two_equals(a,b,c)
    elif(a > lower and a < bigger):
        result = a
    elif(b > lower and b < bigger):
            result = b
    else:
            result = c
    return result


print(median(1,2,3))
# #>>> 2

print(median(9,3,6))
# #>>> 6

print(median(7,8,7))
# #>>> 7

print(median(2,2,1))
#>>> 2

print(median(1,3,2))
#>>> 2