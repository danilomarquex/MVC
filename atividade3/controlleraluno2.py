from modelaluno2 import Aluno
from daoaluno2 import AlunoDao

class AlunoController:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 2 and len(idade > 0 and idade <125) and len(cpf) == 11:
            try:
                AlunoDao.salvar(Aluno(nome, idade, cpf))
                return True
            except:
                return False
        else:
            return False