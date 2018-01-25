def day_of_week(day):
    if day == 0:
        return 'Segunda'
    elif day == 1:
        return 'Terca'
    elif day == 2:
        return 'Quarta'
    elif day == 3:
        return 'Quinta'
    elif day == 4:
        return 'Sexta'
    elif day == 5:
        return 'Sabado'
    elif day == 6:
        return 'Domingo'
    else:
        raise Exception('Dia invalido')