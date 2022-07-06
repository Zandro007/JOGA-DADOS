# Calculando media de alunos em python #

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media do aluno: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'

elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'

else:
    aluno['situação'] = 'REPROVADO'
print(aluno)
