from modelaluno2 import Aluno
from controlleraluno2 import AlunoController

nome = input("Digite o nome do aluno:")
idade = int(input("Digite a idade do aluno:"))
cpf =input("Digite o cpf do aluno:")

aluno1 = Aluno(nome,idade,cpf)


if AlunoController.cadastrar(nome, idade, cpf):
   print('Aluno Cadastrado!')
else :
   print('Insira credenciais válidas!')