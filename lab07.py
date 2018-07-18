#Marianna Gois de Campos
#RA: 221925
N = int(input())
aux = 0
list = []
for i in range(1,N+1):
 for j in range(1,N+1):
  if j%i==0 or i%j==0:
   list.append('*')
   aux = 1 + aux
   aux = aux
   m = ''.join(list)
  elif j%i!=0 or i%j!=0:
   list.append('-')
   m = ''.join(list)
 print(m, end='')
 list = []
 print()
print(aux)



