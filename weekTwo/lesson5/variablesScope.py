egg_count = 0

def buy_eggs():
    egg_count += 12

buy_eggs()


# Isto é um UnboundLocalError. 
# Python não permite que as funções modifiquem variáveis ​​que não estejam no escopo da função. 
# A melhor maneira de reescrever isso seria assim:

def buy_eggs(count):
    return count + 12  # comprar uma dúzia de ovos
egg_count = 0
egg_count = buy_eggs(12)