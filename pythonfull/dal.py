from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
    
    @classmethod
    def ler(cls):
        nome = 'Danilo'
        idade = 16
        cpf = 145353
        return Pessoa(nome, idade, cpf)

p1 = Pessoa('Caio', 20, '5345352')
print(PessoaDal.ler())