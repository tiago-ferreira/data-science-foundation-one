def print_list(l, numbered = False, bullet_character=' - '):
    """Prints a list on multiple lines, with numbers or bullets
    
    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))


#print_list(["cats", "in", "space"])
#print_list(["cats", "in", "space"], True)


def todo_list(new_task, base_list=['wake up']):
    base_list.append(new_task)
    return base_list

print(todo_list("check the mail"))
print(todo_list("begin orbital transfer"))

# Está certo! O objeto de lista base_list é criado somente uma vez: 
# quando a função todo_list é definida. As listas são objetos mutáveis. 
# Este objeto de lista é usado sempre que a função é chamada, 
# não é redefinido cada vez que a função é chamada. 
# Porque todo_list anexa um item à lista, base_list pode ficar mais longo cada vez que todo_list é chamado.