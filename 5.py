max=0
k=1 # в послед-ти есть как минимум 1 макс. число
while True:
    a=int(input())
    if a==0: # если 0, то СТОП
        break
    if a==max: # если число равно макс. числу,
        k+=1 # то прибавляем к счетчику +1
    if a>max: # если число больше макс.,
        max=a # то присваиваем иакс. числу знач. данного числа
        k=1 # и возращаем счетчик к значению = 1
print(k)