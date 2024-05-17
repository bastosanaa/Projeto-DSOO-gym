from models.professor import Professor
from views.telaProfessor import TelaProfessor

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
        # mensagem_erro = "O professor inserido não está cadastrado"
        # self.__tela_professor.mostrar_mensagem(mensagem_erro)
        return None


    def cadastrar_professor(self, nome, telefone, email, turno, salario):
        if self.acessar_professor_pelo_nome(nome):
            self.__tela_professor.mostrar_mensagem("Já existe um professor cadastrado com esse nome")
            return None
        novo_professor = Professor(nome, telefone, email, turno, salario)
        
        self.__professores.append(novo_professor)

    def remover_professor(self, nome, email):
        for professor in self.__professores:
            if professor.nome == nome and professor.email == email:
                self.__professores.remove(professor)
            else:
                self.__tela_professor.mostrar_mensagem("professor nao encontrado")

    def alterar_turno(self):
        pass
        
        