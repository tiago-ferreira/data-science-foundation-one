# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

# def find_last(text, target):
#     result, pos = -1,0
#     while(True):
#         last = text.find(target, pos)
#         if(last > -1):
#             result = last
#             pos += 1 
#         else:
#             break
        
#     return result

def find_last(text, target):
    last_pos = -1
    while(True):
        pos = text.find(target, last_pos + 1)
        if(pos == -1):
            return last_pos
        last_pos = pos

print(find_last('aaaa', 'a'))
#>>> 3

print(find_last('aaaaa', 'aa'))
#>>> 3

print(find_last('aaaa', 'b'))
#>>> -1

print(find_last("111111111", "1"))
#>>> 8

print(find_last("222222222", ""))
#>>> 9
