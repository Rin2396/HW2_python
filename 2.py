n=int(input())
s=0 # счетчик
for i in range(n):
    x=int(input())
    if x==0: # если число = 0, то прибавляем к счетчику
        s+=1
if s>0:
    print('YES') # если счетчик не нулевой
else:
    print('NO') # если счетчик = 0