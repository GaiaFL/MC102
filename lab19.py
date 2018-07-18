#Marianna Gois de Campos
#RA221925
def crescente(lista):
 for i in range(1,len(lista)):
  aux = lista[i]
  j = i-1
  while j>=0 and lista[j]>aux:
   lista[j+1] = lista[j]
   j = j-1
  lista[j+1] = aux

def rastrear(q, f, matriz, lista=None):
 if q == 1:
  return f
 else:
  if lista is None:
   lista = [] #Permanece com a mesma lista mesmo com inúmeras chamadas da função
  i = 0
  while i < len(matriz):
   if matriz[f][i] == 1:
    lista.append(f) #Adiciona à lista o elemento da linha
    rastrear(q-1, i, matriz, lista) #Retorna se a quantidade determinada já foi atingida ou se naquela linha(funcionário) não tive nenhum subalterno
    lista.append(i)#Adiciona à lista o último funcionário ou o que não tem subalternos
   i += 1
 lista.append(f) 
 return lista    

ID = []
n = input()
ind = [int(x) for x in n.split()]
quantidade = ind[0]; funcionário = ind[1]
matriz = [[0 for j in range(quantidade)]for i in range(quantidade)]
for u in range(0, quantidade):
 matriz[u][0:quantidade+1] = [int(g) for g in str(input()).split()]

ID = rastrear(quantidade, funcionário, matriz) 
ID = list(set(ID))#Tiras as repetições
ID.remove(funcionário)
crescente(ID)
ID = [funcionário] + ID
for i in range(0, len(ID)):
 if i == len(ID)-1:
  print(ID[i])
 else: 
  print(ID[i], end=' ')
