#Marianna Gois de Campos
#RA221925
#O seguinte programa visa prever os acontecimentos em uma sociedade pós-apocalíptica e determinar a sobrevivência da humanidade nessa situação
import copy
valores = input()
ints = [int(x) for x in valores.split()]
m = ints[0] 
n = ints[1]
dias = int(input())
matrix = [['0' for j in range(n+2)]for i in range(m+2)]
for i in range(1,m+1):
 matrix[i][1:n+1] = [str(i) for i in str(input()).split()]
print(matrix)
d = 0
print('iteracao',d)
for i in range(1,m+1):
 v = matrix[i][1:n+1]  
 o = ''.join(v)
 print(o)
aux = 1
d = 1
matrix1 = copy.deepcopy(matrix)
while d<=dias:
 print('iteracao',d)
 for i in range(1,m+1):
  for j in range(1,n+1):
   e = matrix[i][j]
   v1 = matrix[i-1][j-1]
   v2 = matrix[i-1][j]
   v3 = matrix[i-1][j+1]
   v4 = matrix[i][j-1]
   v5 = matrix[i][j+1]
   v6 = matrix[i+1][j-1]
   v7 = matrix[i+1][j]
   v8 = matrix[i+1][j+1]
   lista = [v1,v2,v3,v4,v5,v6,v7,v8]
   y = lista.count('0')
   x = lista.count('1')
   z = lista.count('2')
   if e == '1':
    if z>=1:
     matrix1[i][j] = '2'
   elif e == '2':
    if x>=2 or x==0:
     matrix1[i][j] = '0'
   elif e == '0':
    if x == 2:
     matrix1[i][j] = '1'
  v = matrix1[i][1:n+1]
  o = ''.join(v)
  print(o)
 d = aux + 1
 aux = d 
 matrix = copy.deepcopy(matrix1)

