# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(qtd):
    i = 1
    while(i <= qtd):
        print(i)
        i += 1
                  
print_numbers(3)
#>>> 1
#>>> 2
#>>> 3