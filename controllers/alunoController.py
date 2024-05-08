
from models.aluno import Aluno
from views import AlunoView
from models.matricula import Matricula

class ControladorAluno():
    def __init__(self):
        self.__tela_aluno = AlunoView()
        self.__controlador_aluno = ControladorAluno()
        self.__alunos = []
    
    @property
    def alunos(self):
        return self.__alunos

    def inserir_turno(self):
        pass

    def retirar_turno(self):
        pass

    def mostrar_treino_ficha(self):
        pass

    def dados_matricula(self):
        

    def calcular_aluno_por_turno(self):
        pass

    def cancelar_matricula(self):
        pass

    def retornar(self):
        self.__controlador_aluno.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inserir_turno, 2: self.__retirar_turno,
                        3: self.__mostrar_treino_ficha,
                        4: self.__mostrar_matricula,
                        5: self.__cancelar_matrocula,
                        6: self.__calcular_aluno_por_turno,
                        0: self.__retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
