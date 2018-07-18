import re
#Marianna Gois de Campos
#RA 221925
#O seguinte programa visa receber dados de alunos de um instituto e facilitar qualquer mudança atribuída para estes.
class EmailInvalido(Exception):
    pass

class SenhaFraca(Exception):
    pass

class RAInvalido(Exception):
    pass

class Repositorio:
 def __init__(self):
  self.alunos = []
  self.RA = []
#Este método recebe o parâmetro aluno e o insere no repositório
 def adicionar(self, aluno):
  if aluno.ra in self.RA:
   raise RAInvalido
  else:
   key = re.compile(r'\w{5}\S{1}\D{1,50}?')
   senha = re.findall(r'[\w]', aluno.senha)
   if len(senha)>=7 and key.findall(aluno.senha):
    em = re.compile(r'\w+([_.+-])?(\w+)?@\w+\.\D{2,4}')
    if em.findall(aluno.email):
     self.RA.append(aluno.ra)
     self.alunos.append(aluno)
     return True
    else:
     raise EmailInvalido
   else:
    raise SenhaFraca


#Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra
 def alterar(self, aluno):
  if aluno.ra not in self.RA:
   raise RAInvalido
  else:
   key = re.compile(r'\w{5}\S{1}\D{1,50}?')
   senha = re.findall(r'[\w]', aluno.senha)
   if len(senha) >= 8 and key.findall(aluno.senha):
    em = re.compile(r'\w+([_.+-])?(\w+)?@\w+\.\D{2,4}')
    if em.findall(aluno.email):
     i = self.RA.index(aluno.ra)
     self.alunos[i] = aluno
     return True
    else:
     raise EmailInvalido
   else:
    raise SenhaFraca

#Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
 def achaAluno(self, ra):
  if ra not in self.RA:
   raise RAInvalido
  else:
   i = self.RA.index(ra)
   return self.alunos[i]

#Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
 def remover(self, ra):
  if ra not in self.RA:
   raise RAInvalido
  else:
   i = self.RA.index(ra)
   del(self.alunos[i])
   return True
#Este método exclui todos os alunos do repositório.
 def limparRepositorio(self):
  if self.alunos != []:
   for i in range(len(self.alunos),1):
    del(self.alunos[i])
   return True
  else:
   return True
