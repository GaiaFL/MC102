#Marianna Gois de Campos RA221925
#O seguinte programa busca imitar catracas de um estacionamento; o valor dado representa o tamanho do veículo que esteja entrando ou saindo, e, a partir deste, calcular o quanto resta de capacidade nesse espaço. 
C = int(input())
i =[-5, -4, -3, -2, -1, 1, 2, 3 , 4, 5]
for n in range(1,120):
 n = int(input())
 if n==0:
  break
 elif n>0 and n<C or n==C:
  CAPACIDADE = C - n 
  C = C - n
  print('Seja bem-vindo! Capacidade restante:',CAPACIDADE)
  if n>CAPACIDADE:
   continue
 elif n>C:
  print('Veiculo muito grande! Capacidade restante:',CAPACIDADE)
 elif n<0:
  CAPACIDADE = CAPACIDADE - n
  C = CAPACIDADE
  print('Volte sempre! Capacidade restante:',CAPACIDADE)
