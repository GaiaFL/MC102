#Marianna Gois de Campos
#RA 221925
#O seguinte programa visa simular as funções de uma lista de alunos universitários, facilitando o processo de montagem e ajustes
def imprimir(lista):
 if lista != []:
  print(*lista, sep=' ')
 else:
  return None

def crescente(lista):
 for i in range(1,len(lista)):
  aux = lista[i]
  j = i-1
  while j>=0 and lista[j]>aux:
   lista[j+1] = lista[j]
   j = j-1
  lista[j+1] = aux
 tabela.append('c')

def decrescente(lista):
 for i in range(0,len(lista)):
  maior = i
  for j in range(i,len(lista)):
   if lista[maior]<lista[j]:
    maior = j
  lista[i], lista[maior] = lista[maior], lista[i]
 tabela.append('d')

def busca(lista, tabela, RA,index ):
 if tabela[len(tabela)-1] == 'c':
  ini = 0
  fim = len(lista)-1
  while ini<= fim:
   meio = (ini+fim)//2
   index.append(meio)
   if lista[meio] == RA:
    tabela = []
    return meio
   elif lista[meio]> RA:
    fim = meio - 1
   else:
    ini = meio + 1
  tabela = []
  return -1
 elif tabela[len(tabela)-1] == 'd':
  ini = 0
  fim = len(lista)-1
  while ini<=fim:
   meio = (ini+fim)//2
   index.append(meio)
   if lista[meio] == RA:
    tabela = []
    return meio
   elif lista[meio]>RA:
    ini = meio + 1
   else:
    fim = meio - 1
  tabela = []
  return -1

def insert(lista,tabela,RA):
 if len(lista)-1 >= 150:
  print('Limite de vagas excedido!')
 else:
  for i in range(len(lista)):
   if lista[i] == RA:
    print('Aluno ja matriculado na turma!')
  if tabela == []:
   lista.append(RA)
  else:
   lista.append(RA)
   if tabela[len(tabela)-1] == 'c':
    for i in range(1,len(lista)):
     aux = lista[i]
     j = i-1
     while j>=0 and lista[j]>aux:
      lista[j+1] = lista[j]
      j = j-1
      lista[j+1] = aux
   elif tabela[len(tabela)-1] == 'd':
    for i in range(0,len(lista)):
     maior = i
     for j in range(i,len(lista)):
      if lista[maior]<lista[j]:
       maior = j
       lista[i], lista[maior] = lista[maior], lista[i]

def remove(lista,RA):
 if lista == []:
  print('Nao ha alunos cadastrados na turma!')
 elif RA not in lista:
  print('Aluno nao matriculado na turma!')
 else:
  for x in lista:
   if x == RA:
    a = lista.index(RA)
    del(lista[a])

index = []
valores = input()
tabela = [] 
lista = [int(x) for x in valores.split()]
for k in range(150):
 n = input()
 ints = [str(i) for i in n.split()]
 n = ints[0]
 if n == 'p':
  imprimir(lista)
 elif n == 'c':
  crescente(lista)
 elif n == 'd':
  decrescente(lista)
 elif n == 'b':
  RA = int(ints[1])
  a = tabela.count('c')
  b = tabela.count('d')
  if a == 0:
   if b == 0:
    print('Vetor nao ordenado!')
   else:
    meio = busca(lista,tabela,RA,index)
    print(*index, sep=' ')
    index = []
    if meio>=0:
     print('%d esta na posicao: %d'%(RA,meio))
    else:
     print('%d nao esta na lista!'%(RA))
  elif a!=0 or b!=0:
   meio = busca(lista,tabela,RA,index)
   print(*index, sep=' ')
   index = []
   if meio>=0:
    print('%d esta na posicao: %d'%(RA,meio))
   else:
    print('%d nao esta na lista!'%(RA))
 elif n == 'i':
  RA = int(ints[1])
  insert(lista,tabela,RA)
 elif n =='r':
  RA = int(ints[1])
  remove(lista,RA)
 else:
  break

