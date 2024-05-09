from models.professor import Professor
from views.professor import ProfessorView

class ControladorProfessor():
    def __init__(self):
        self.__tela_professor = ProfessorView()
        self.__professores = [Professor]

    @property
    def professores(self):
        return self.__professores

    def definir_salario(self):
        pass

    def cadastrar_professor(self,nome, telefone, email, turno, salario):
        novo_professor = Professor(nome, telefone, email, turno, salario)
        #VERIFICAR SE PROFESSOR JA EXISTE, CASO JA, EXIBIR NA TELA
        self.__professores.append(novo_professor)

    def remover_professor(self, nome, email):
        for professor in self.__professores:
            if professor.nome == nome and professor.email == email:
                self.__professores.remove(professor)
            else:
                self.__tela_professor.exibir_mensagem_erro("professor nao encontrado")
        
        