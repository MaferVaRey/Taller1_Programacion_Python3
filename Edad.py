from time import localtime

t = localtime()
day = t.tm_mday
month = t.tm_mon
year = t.tm_year

apio = int(input('Ingrese su año de nacimiento: '))
mes = int(input('Ingrese su mes de nacimiento (en números): '))
dia = int(input('Ingrese su día (del mes) de nacimiento: '))

age = 0

if month > mes:
    age = year - apio
elif month == mes:
    if day == dia or dia > day:
        age = year - apio
    elif dia < day:
        age = (year-1) - apio
elif month < mes:
    age = (year-1) - apio

print('Su edad es: ', age)
