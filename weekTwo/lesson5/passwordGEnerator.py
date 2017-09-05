# Use an import statement at the top
from random import randint
word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function here
# It should return a string consisting of three random words 
# concatenated together without spaces

def generate_password():
    global word_list
    word = ''
    for i in range(3):
        word += word_list[randint(0, len(word_list) - 1)]
    return word

print(generate_password())


# Your code passes all of our tests, nice work!


# We used import random and then the function definition was simply:


# def generate_password():
#     return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

# Alternatively, you could use the random.sample function and .join method for strings:


# def generate_password():
#     return str().join(random.sample(word_list,3))