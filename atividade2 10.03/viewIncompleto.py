from modelaluno import Aluno
from controlleraluno import AlunoController

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
cpf =input("Digite o cpf do aluno: ")
aluno1 = Aluno(nome,idade,cpf)

if AlunoController.cadastrar(nome, idade, cpf):
   print('Aluno Cadastrado!')
else :
   print('Insira credenciais válidas!')

'''
1- usando a classe AlunoDao salve os dados do objeto aluno1 no arquivo alunos.txt
2- usando a classe AlunoDao leia os dados gravados do arquivo alunos.txt e imprima os dados gravados
   (sugestao: coloque os dados lidos dentro de uma lista) 
'''  