#Marianna Gois de Campos RA221925
#O seguinte programa visa calcular o desempenho de um aluno no curso de graduação de Ciência da Computação, a partir de suas notas e médias em trabalhos e provas, para assim, determinar sua aprovação ou reprovação
P1 = float(input())
P2 = float(input())
M1 = float(input())
MP = ((2*P1)+(3*P2))/5
print('%.1f' %MP)
Mpre = ((3*MP)+(2*M1))/5
print('%.1f' %Mpre)
if MP<5 or M1<5:
 M = min(Mpre, 4.9)
else:
 M = Mpre
print('%.1f' %M)
if M>=2.5 and M<5:
 E = float(input())
 F = min((M+E)/2, 5.0) 
else: 
 F = M
print('%.1f' %F)

