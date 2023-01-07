from model import Aluno
class AlunoDao:
    @classmethod
    def salvar(cls, aluno:Aluno):
        with open("alunos.txt","a") as arq:            
            arq.write(aluno.nome +" - "+ str(aluno.idade) +" - "+ aluno.cpf + "\n")
        arq.close()
    
    @classmethod
    def ler(cls):
        lista = []
        arq = open("alunos.txt", "r")    
        for linha in arq.readlines():
            l = linha.split("-")
            nome = l[0]
            idade = l[1]
            cpf = l[2].strip("\n")
            lista.append(Aluno(nome, idade, cpf))
        return lista
            
                
