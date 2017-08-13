def abs(n):
    return (n ^ (n >> 31)) + ( (n % 0x100000000) >> 31 )

def bigger(a, b):
    return ((a+b) +  abs(a-b) ) / 2;

def min(x,y):
    return y ^ ((x ^ y) & -(x < y))

def max(x,y):
    return x ^ ((x ^ y) & -(x < y))

print('use bigger functon')
print(bigger(10,7))
print(bigger(10,17))
print(bigger(-10,-7))
print(bigger(-10,-17))
print(bigger(10,10))

print('use min functon')
print(min(10,7))
print(min(10,17))
print(min(-10,-7))
print(min(-10,-17))
print(min(10,10))

print("use max function")
print(max(10,7))
print(max(10,17))
print(max(-10,-7))
print(max(-10,-17))
print(max(10,10))