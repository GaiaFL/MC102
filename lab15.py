#Marianna Gois de Campos
#RA 221925
#O seguinte programa visa realizar operações matemáticas envolvendo conjuntos
def pertence(conj, num):
 for x in conj:
  if x == num:
   return True
 if num not in conj:
  return False

def contido(conj1, conj2):
 if set(conj1).issubset(set(conj2)):
  return True
 else:
  return False

def adicao(conj, num):
 if num in conj:
  return False
 else:
  conj.append(num)
  for i in range(1, len(conj)):
   aux = conj[i]
   j = i-1
   while j>=0 and conj[j]>aux:
    conj[j+1] = conj[j]
    j = j-1
   conj[j+1] = aux
  return True

def subtracao(conj, num):
 if num not in conj:
  return False
 else:
  conj.remove(num)
  for i in range(1, len(conj)):
   aux = conj[i]
   j = i-1
   while j>=0 and conj[j]>aux:
    conj[j+1] = conj[j]
    j = j-1
   conj[j+1] = aux
  return True

def uniao(conj1, conj2):
 a = conj1[:]
 for x in conj2:
  if x not in conj1:
   a.append(x)
 for i in range(1, len(a)):
  aux = a[i]
  j = i-1
  while j>=0 and a[j]>aux:
   a[j+1] = a[j]
   j = j-1
  a[j+1] = aux
 return a

def intersecao(conj1, conj2):
 d = []
 for x in conj1:
  for y in conj2:
   if y == x:
    d.append(y)
 for i in range(1, len(d)):
  aux = d[i]
  j = i-1
  while j>=0 and d[j]>aux:
   d[j+1] = d[j]
   j = j-1
  d[j+1] = aux
 return d

def diferenca(conj1, conj2):
 f = []
 for x in conj1:
  if x not in conj2:
   f.append(x)
 for i in range(1, len(f)):
  aux = f[i]
  j = i-1
  while j>=0 and f[j]>aux:
   f[j+1] = f[j]
   j = j-1
  f[j+1] = aux
 return f
 
def uniao_disjunta(conj1, conj2):
 u = []
 for x in conj1:
  if x not in conj2:
   u.append(x)
 for y in conj2:
  if y not in conj1:
   u.append(y)
 for i in range(1, len(u)):
  aux = u[i]
  j = i-1
  while j>=0 and u[j]>aux:
   u[j+1] = u[j]
   j = j-1
  u[j+1] = aux
 return u
