# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(values, target):
    for idx, value in enumerate(values):
        if(value == target):
            return idx
    return -1


print(find_element([1,2,3],3))
#>>> 2

print(find_element(['alpha','beta'],'gamma'))
#>>> -1

print(find_element(['CS101', 'CS373', 'CS212', 'CS101', 'CS373', 'CS262'], 'CS101'))