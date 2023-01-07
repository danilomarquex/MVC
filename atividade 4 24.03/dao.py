from model import Produto
from model import Cliente

class ProdutoDao:
    @classmethod
    def salvar(cls, produto:Produto):
        with open('produtos.txt', 'a') as arq:
            arq.write(produto.nome+'|'+str(produto.preco)+'|'+produto.categoria+'\n')
        arq.close()
    
    @classmethod
    def ler_produtos(cls):
        lista = []
        arq = open('produtos.txt', 'r')
        for linha in arq.readlines():
            l = linha.split('|')
            nome = l[0]
            preco = l[1]
            categoria = l[2].strip('\n')
            lista.append(Produto(nome, preco, categoria))
        return lista

class ClienteDao:
    @classmethod
    def salvar(cls, cliente:Cliente):
        with open('cliente.txt', 'a') as arq:
            arq.write(cliente.nome +'|'+ str(cliente.idade) +'|'+ cliente.cpf + '\n')
        arq.close()

    @classmethod
    def ler_clientes(cls):
        lista = []
        arq = open('cliente.txt', 'r')
        for linha in arq.readlines():
            l = linha.split('|')
            nome = l[0]
            idade = l[1]
            cpf = l[2].strip('\n')
            lista.append(Cliente(nome, idade, cpf))