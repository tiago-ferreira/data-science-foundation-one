def abs(n):
    return (n ^ (n >> 31)) + ( (n % 0x100000000) >> 31 )

def bigger(a, b):
    return ((a+b) +  abs(a-b) ) / 2;

print(bigger(10,7))
print(bigger(10,17))
print(bigger(-10,-7))
print(bigger(-10,-17))
print(bigger(10,10))