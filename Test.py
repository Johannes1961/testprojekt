from random import uniform
sum = 0
Nam = []
zähl = 0
for i in range(1, 10):
     fl = uniform(0, 10)
     if fl < 3:
        print('Ersatzvariable ist kleiner 3:   ')
        zähl += 1
     Nam = str(round(fl, 2))
     sum += fl 
     print(Nam, ' ')

print('')
print('Summe = ', sum, '    Anzahl der Zahlen < 3 = ', zähl)