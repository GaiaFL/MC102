#Marianna Gois de Campos
#RA 221925
#O seguinte programa visa facilitar a modificação de textos a partir de dados de funções
import re
def remove(a, b):
 del(b[a])
pontuação = [',','.',':',';','?','!']
inv = ''
texto = str(input())
print(texto)
texto = texto.split()
for k in range(50):
 k = str(input())
 if k == 'D':
  deletar = str(input())
  deletar = deletar.lower()
  if deletar in [x.lower() for x in texto]:
   while deletar in [x.lower() for x in texto]:
    y = [x.lower() for x in texto]
    f = y.index(deletar)
    remove(f, texto)
   m = ' '.join(texto)
   print(m)
   texto = m.split()
  else:
   texto = ' '.join(texto)
   texto = re.findall(r"[\w]+|[.,!?:;]", texto)
   y = [x.lower() for x in texto]
   f = y.index(deletar)
   remove(f, texto)
   remove(f, texto)
   for c in texto:
    if c in pontuação:
     f = texto.index(c)
     texto[f-1:f+1] = [''.join(texto[f-1:f+1])]
   texto = ' '.join(texto)
   print(texto)
   texto = texto.split()   
 elif k =='I':
  inverter = str(input())
  inverter = inverter.lower()
  texto = ' '.join(texto)
  texto = re.findall(r"[\w]+|[.,!?:;]", texto)
  while inverter in [x.lower() for x in texto]:
   y = [x.lower() for x in texto]
   f = y.index(inverter)
   inverter1 = texto[f]
   for x in inverter1:
    invertida = x + inv
    inv = invertida
   inv = ''
   texto = ' '.join(texto)
   texto = texto.replace(inverter1,invertida)
   texto = texto.split()
   for c in texto:
    if c in pontuação:
     f = texto.index(c)
     texto[f-1:f+1] = [''.join(texto[f-1:f+1])]
  texto = ' '.join(texto)
  print(texto)
  texto = texto.split()  
 elif k == 'R':
  velha = str(input())
  nova = str(input())
  texto = ' '.join(texto)
  texto = re.findall(r"[\w]+|[.,!?:;]", texto)
  while velha in[x.lower() for x in texto]:
   y = [x.lower() for x in texto]
   f = y.index(velha)
   velha1 = texto[f]
   texto = ' '.join(texto)
   texto = texto.replace(velha1,nova)
   texto = texto.split()
   for c in texto:
    if c in pontuação:
     f = texto.index(c)
     texto[f-1:f+1] = [''.join(texto[f-1:f+1])]
  texto = ' '.join(texto)
  print(texto)
  texto = texto.split()  
 elif k == 'Q':
  break
