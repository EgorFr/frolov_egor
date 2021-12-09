# -- coding: utf-8 --
n = int(input())
m = int(input())
k = int(input())
k1 = 0
def F(n,m,k,k1):
  k1 = (n*m) / 2
  if (k1==k): 
    return 'Да'
  elif (k1!=k): return 'Нет'
print(F(n,m,k,k1))