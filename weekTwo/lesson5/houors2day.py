def hours2days(h):
    days = int(h / 24)
    hours = h % 24
    return days, hours


print(hours2days(24)) # 24 horas é um dia e zero horas
#(1, 0)
print(hours2days(25)) # 25 horas é um dia e uma hora
#(1, 1)
print(hours2days(10000))
#(416, 16)