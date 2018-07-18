#Marianna Gois de Campos
#RA221925
#O seguinte programa visa disponibilizar aos jogadores do jogo PokéaMãe informações sobre o possível poder futuro da criatura que eles dispõem em mãos, a partir de uma biblioteca de dados.
import math
F = [0 for j in range(1,500)]
N = int(input())
list = []
for linha in range(N):
 linha = input()
 ints = [int(i) for i in linha.split()]
 I = ints[0]
 PCa = ints[1]
 PCf = ints[2]
 M = PCf/PCa
 list.append(I)
 if F[I]==0:
  F[I] = M
 elif F[I]!=0:
  F[I] = F[I]+M
for i in range(1000):
 linha = input()
 ints = [int(i) for i in linha.split()]
 I = ints[0]
 PCa = ints[1]
 if I==0 and PCa==0:
  break
 T = list.count(I)
 M = F[I]/T
 PCf = math.ceil(PCa * M)
 print(PCf)

