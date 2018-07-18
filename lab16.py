#Marianna Gois de Campos
#RA221925
#O seguinte programa busca relacionar uma sentença procurada pelo usuário com diversos links de pesquisas, a fim de filtrar e achar aquele que se associa melhor ao pesquisado. 
import re

def removePalavras(s, vs):
 s = s.split()
 for x in vs:
  if x in s:
   while x in s:
    pos = s.index(x)
    del(s[pos])
 s = ' '.join(s)
 return s

def pagsResposta(paginas, termosBusca):
 buscas = []
 resp = []
 for i in range(0,len(paginas)):
  all_words = re.findall(r'\w+', paginas[i])#separa cada algarismo alfanúmerico da sentença, possibilitando maior facilidade na busca
  for word in termosBusca:
   if word in all_words:
    buscas.append(word)
  if len(buscas) == len(termosBusca):
   resp.append(1)
  else:
   resp.append(0)
  buscas = []
 return resp

def linksResposta(links, resp):
 indices = []
 numLinks = [0 for g in range(0,len(resp))]
 for i in range(0,len(resp)):
  if resp[i] == 0:
   numLinks[i] = -1
  else:
   for j in range(0,len(links)):
    if links[j][i] == 1 and resp[j]!=0:
     numLinks[i] = numLinks[i]+1
 return numLinks 
