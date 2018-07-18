#Marianna Gois de Campos
#RA221925
import sys
import copy
arq1 = open(sys.argv[1], mode = 'r', encoding = 'utf-8')
arq2 = open(sys.argv[2], mode = 'r', encoding = 'utf-8')
tipo = arq1.readline()
ints = arq1.readline().split() 
coluna = int(ints[0])
linha = int(ints[1])
matriz = [[0 for j in range(coluna)]for i in range(linha)]
maximo = int(arq1.readline())
lista = arq1.readline().split()
lista = [int(x) for x in lista]
i = 0
while len(lista) == coluna:
 matriz[i] = lista[:]
 i = i+1 
 lista = arq1.readline().split()
 lista = [int(x) for x in lista]
div = int(arq2.readline())
M = [[0 for h in range(3)]for g in range(3)]
lista2 = arq2.readline().split()
lista2 = [int(x) for x in lista2]
g = 0
while len(lista2) == 3:
 M[g] = lista2[:]
 g = g+1
 lista2 = arq2.readline().split()
 lista2 = [int(x) for x in lista2]

matriz2 = copy.deepcopy(matriz)

for l in range(1, linha-1):
 for m in range(1, coluna-1):
  a = M[0][0] * matriz[l-1][m-1]
  b = M[0][1] * matriz[l-1][m]
  c = M[0][2] * matriz[l-1][m+1]
  d = M[1][0] * matriz[l][m-1]
  e = M[1][1] * matriz[l][m]
  f = M[1][2] * matriz[l][m+1]   
  g = M[2][0] * matriz[l+1][m-1]
  h = M[2][1] * matriz[l+1][m]
  i = M[2][2] * matriz[l+1][m+1]
  soma = (a+b+c+d+e+f+g+h+i)/div
  if soma < 0:
   matriz2[l][m] = 0
  elif soma > maximo:
   matriz2[l][m] = 255
  else:
   matriz2[l][m] = int(soma) 
print(tipo, end='')
print(coluna, linha)
print(maximo)
for l in range(linha):
 for m in range(coluna):   
  if m == coluna - 1:
   print(str(matriz2[l][m]) + ' ' + ' ')
  else:
   print(str(matriz2[l][m]) + ' ', end='')
arq1.close()
arq2.close()
