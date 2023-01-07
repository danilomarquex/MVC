from model import *
from dao import *

class ProdutoController:
    @classmethod
    def cadastrar(cls, nome, preco, categoria):
        if len(nome) > 2 and len(str(preco)) >= 1 and len(categoria) > 2:
            try:
                ProdutoDao.salvar(Produto(nome, preco, categoria))
                return True
            except:
                return False
        else:
            return False

class ClienteController:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 2 and len(idade) > 0 and len(idade) < 125 and len(cpf) == 11 :
            try:
                ClienteDao.salvar(Cliente(nome, idade, cpf))
                situacaoT = [True]
                situacaoF = [False]
                return len(situacaoT)
            except:
                return len(situacaoF)
        else:
            return False