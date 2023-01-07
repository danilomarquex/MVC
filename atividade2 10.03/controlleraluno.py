from modelaluno import Aluno
from daoIncompleto import AlunoDao

class AlunoController:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 2 and (idade > 0 and idade <200) and len(cpf) == 11:
            try:
                AlunoDao.salvar(Aluno(nome, idade, cpf))
                return True
            except:
                return False
        else:
            return False