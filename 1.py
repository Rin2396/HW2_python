x=int(input())
s=0 # счетчик
n=1 # наименьший делитель (начинаем с 1)
while s!=1:
    n+=1 # перебор делителей с 1 
    if x%n==0: # первое число, на которое поделиться х, будет его НОД
        s+=1 # и цикл остановится
        print(n)