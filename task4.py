'''
Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no

'''

width = int(input("Введите целое число (количество долек по ширине шоколадки): "))
length = int(input("Введите целое число (количество долек по длине шоколадки): "))
value = int(input("Введите целое число (количество долек, которое хотите отломить): "))

if value < width*length and (value%width==0 or value%length==0):
    print(f'{width} {length} {value} -> yes')
else:
    print(f'{width} {length} {value} -> no')
  