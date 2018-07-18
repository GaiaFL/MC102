def atualizaTabela(tabela,jogo):
 g = jogo.split()
 if g[1]>g[3]:
  for i in range(len(tabela)):
   if tabela[i][0] == g[0]:
    tabela[i][1] = tabela[i][1] + 3
    tabela[i][2] = tabela[i][2] + 1
    tabela[i][3] = tabela[i][3] + int(g[1]) - int(g[3])
    tabela[i][4] = tabela[i][4] + int(g[1])
   if tabela[i][0] == g[4]:
    tabela[i][3] = tabela[i][3] + int(g[3]) - int(g[1])
    tabela[i][4] = tabela[i][4] + int(g[3])
 elif g[1]<g[3]:
  for i in range(len(tabela)):
   if tabela[i][0] == g[4]:
    tabela[i][1] = tabela[i][1] + 3
    tabela[i][2] = tabela[i][2] + 1
    tabela[i][3] = tabela[i][3] + int(g[3]) - int(g[1])
    tabela[i][4] = tabela[i][4] + int(g[3])
   if tabela[i][0] == g[0]:
    tabela[i][3] = tabela[i][3] + int(g[1]) - int(g[3])
    tabela[i][4] = tabela[i][4] + int(g[1])
 elif g[1] == g[3]:
  for i in range(len(tabela)):
   if tabela[i][0] == g[0]:
    tabela[i][1] = tabela[i][1] + 1
    tabela[i][3] = tabela[i][3] + int(g[1]) - int(g[3])
    tabela[i][4] = tabela[i][4] + int(g[1])
  for i in range(len(tabela)):
   if tabela[i][0] == g[4]:   
    tabela[i][1] = tabela[i][1] + 1
    tabela[i][3] = tabela[i][3] + int(g[3]) - int(g[1])
    tabela[i][4] = tabela[i][4] + int(g[3])
def comparaTimes(time1,time2): #Lembre de que se usar o 'or', o terminal vai avaliar todas as possibilidades da linha antes do próximo 'if'
 if time1[1]>time2[1]:
  return 1
 elif time1[1]<time2[1]:
  return -1
 else:
  if time1[2]>time2[2]:
   return 1
  elif time1[2]<time2[2]:
   return -1
  else:
   if time1[3]>time2[3]:
    return 1
   elif time1[3]<time2[3]:
    return -1
   else:
    if time1[4]>time2[4]:
     return 1
    elif time1[4]<time2[4]:
     return -1
    else:
     return 0

def ordenaTabela(tabela):
 for i in range(len(tabela)):
  for x in range(i+1,len(tabela)):
   if comparaTimes(tabela[i], tabela[x]) == 1:
    tabela[i], tabela[x] = tabela[i], tabela[x]
   elif comparaTimes(tabela[i], tabela[x]) == -1:
    tabela[i], tabela[x] = tabela[x], tabela[i]
def imprimeTabela(tabela):
  print(tabela)

