from models.professor import Professor
from views.professorView import TelaProfessor

class ControladorProfessor():
    def __init__(self):
        self.__tela_professor = TelaProfessor()
        self.__professores = [Professor]

    @property
    def professores(self):
        return self.__professores

    def definir_salario(self):
        pass

    def acessar_professor_pelo_nome(self, nome):
        for prof in self.professores:
            if prof.nome == nome:
                return prof
        mensagem_erro = "O professor inserido não está cadastrado"
        self.__tela_professor.exibir_mensagem_erro(mensagem_erro)
        return None


    def cadastrar_professor(self, nome:str, telefone, email, turno, salario):
        novo_professor = Professor(nome, telefone, email, turno, salario)
        #VERIFICAR SE PROFESSOR JA EXISTE, CASO JA, EXIBIR NA TELA
        self.__professores.append(novo_professor)

    def remover_professor(self, nome, email):
        for professor in self.__professores:
            if professor.nome == nome and professor.email == email:
                self.__professores.remove(professor)
            else:
                self.__tela_professor.exibir_mensagem_erro("professor nao encontrado")

    def adicionar_turno_professor(self,professor, turno):
        pass

    def remover_turno_professor(self, professor, turno):
        pass

        
        