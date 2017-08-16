# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(p):
    if(len(p)  == 0):
        return True
    if(p[0] and len(p) != len(p[0])):
        return False
    row_size = len(p[0])
    colum_size = len(p)
    if(row_size == 1 and colum_size == 1):
        return True
    row1_value, column1_value, row2_value, column2_value = [],[],[],[]
    for i in range(row_size):
        row1_value.append(p[0][i])
        row2_value.append(p[1][i])
    for i in range(colum_size):
        column1_value.append(p[i][0])
        column2_value.append(p[i][1])
    if(row1_value == column1_value and row2_value == column2_value):
        return True
    else:
        return False 
    

print(symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                 ["fish", "fish", "cat"]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish","fish","cat"]]))
#>>> False

print(symmetric([[1, 2],
                 [2, 1]]))
#>>> True

print(symmetric([[1, 2, 3, 4],
                 [2, 3, 4, 5],
                 [3, 4, 5, 6]]))
#>>> False

print(symmetric([[1,2,3],
                  [2,3,1]]))
#>>> False

print(symmetric([]))

print(symmetric([[1]]))