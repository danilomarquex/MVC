from model import *
from controller import *

print('Bem vindo ao cadastro de produtos e clientes!!!')

nome = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))
categoria = input('Digite a categoria do produto: ')
if ProdutoController.cadastrar(nome, preco, categoria):
    print('Produto Cadastrado!')
else:
    print('Houve um erro ao cadastrar o produto!')

nome = input('Digite o nome do cliente: ')
idade = input('Digite a idade do cliente: ')
cpf = input('Digite o CPF do cliente: ')
if ClienteController.cadastrar(nome, idade, cpf):
    print('Cliente Cadastrado!')
else:
    print('Houve um erro ao cadastrar o cliente!!!')