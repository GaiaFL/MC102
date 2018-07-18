#Marianna Gois de Campos
#RA 221925
#O seguinte programa visa imitar uma possível partida batalha naval, cujo o vencendor será aquele que destruir todos os navios de seu oponente
import re
def ataque(l, c, v, G, H, a):
 if l < G - 1: #Verifica se não está fora do tabuleiro
  if v[l+1][c] == '@':
   lista = list(v[l+1]) #Transforma numa lista para poder substituir a string, que é imutável
   lista[c] = a
   lista = ''.join(lista)
   v[l+1] = lista
   ataque(l+1, c, v, G, H, a)
 if l > 0:
  if v[l-1][c] == '@':
   lista = list(v[l-1])
   lista[c] = a
   lista = ''.join(lista)
   v[l-1] = lista 
   ataque(l-1, c, v, G, H, a)
 if c < H - 1:
  if v[l][c+1] == '@':
   lista = list(v[l])
   lista[c+1] = a
   lista = ''.join(lista)
   v[l] = lista  
   ataque(l, c+1, v, G, H, a)
 if c > 0 :
  if v[l][c-1] == '@':
   lista = list(v[l])
   lista[c-1] = a
   lista = ''.join(lista)
   v[l] = lista
   ataque(l, c-1, v, G, H, a)

def check(matrix, G, H): #Verifica se a matriz atende à condição de ter algum navio restante
 ind = []
 for i in range(G):
  for j in range(H):
   if matrix[i][j] == '-':
    ind.append(i)
 if len(ind) == G*H:
  return False
 else:
  return True
 
aspas = '-' 
v = input()
valores = re.findall(r'\d+', v)
linha = int(valores[0])
coluna = int(valores[1])
campo1 = [[0 for j in range(coluna)]for i in range(linha)]
campo2 = [[0 for j in range(coluna)]for i in range(linha)]
for i in range(linha):
 campo1[i] = input()
for i in range(linha):
 campo2[i] = input()

while all(campo1) != '-' or all(campo2) != '-': #Não funciona a condição do loop
 try:
  c = input()
  coordenadas = re.findall(r'\w+', c)
  l = int(coordenadas[0])-1
  c = int(coordenadas[1])-1
  if campo2[l][c] == '@':
   lista = list(campo2[l])
   lista[c] = aspas
   lista = ''.join(lista)
   campo2[l] = lista
   ataque(l, c, campo2, linha, coluna, aspas)
  print('Ataque em (' + coordenadas[0] + ',' + coordenadas[1] + ') do jogador 1')
  for i in range(linha):
   print(campo2[i])
  if check(campo2, linha, coluna) == False:
   break
  c = input()
  coordenadas = re.findall(r'\w+', c)
  l2 = int(coordenadas[0])-1
  c2 = int(coordenadas[1])-1
  if campo1[l2][c2] == '@':
   lista = list(campo1[l2])
   lista[c2] = aspas
   lista = ''.join(lista)
   campo1[l2] = lista
   ataque(l2, c2, campo1, linha, coluna, aspas)
  print('Ataque em ('+ coordenadas[0] + ','+ coordenadas[1] +') do jogador 2') 
  for i in range(linha):
   print(campo1[i])
  if check(campo1, linha, coluna) == False:
   break
 except:
  break
