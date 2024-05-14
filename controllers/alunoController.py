
from models.aluno import Aluno
from views import AlunoView
from models.matricula import Matricula
from models.ficha import Ficha

class ControladorAluno():
    def __init__(self):
        self.__tela_aluno = AlunoView()
        self.__controlador_aluno = ControladorAluno()
        self.__alunos = []
    
    @property
    def alunos(self):
        return self.__alunos

    def inserir_turno(self, nome):
        aluno_existente = None
        for aluno in self.__alunos:
            if aluno.nome == nome:
                aluno_existente = aluno
                break
        if aluno_existente:
            self.__tela_aluno.mostrar_mensagem("Aluno já está inserido em um turno.")
        else:
            novo_aluno = Aluno(nome)
            self.__alunos.append(novo_aluno)
            self.__tela_aluno.mostrar_mensagem("Aluno inserido em turno com sucesso.")
    
    def buscar_matricula_por_nome(self, nome):
        matricula_encontrada = None
        for aluno in self.__alunos:
            for matricula in aluno.matriculas:
                if matricula.aluno.nome == nome:
                    matricula_encontrada = matricula
                    break
            if matricula_encontrada:
                break
        if matricula_encontrada:
            self.__tela_aluno.mostrar_dados_matricula(matricula_encontrada)
        else:
            self.__tela_aluno.mostrar_mensagem("Matrícula não encontrada.")
        
    def retirar_turno(self, nome):
        pass

    def mostrar_treino_ficha(self, ficha: Ficha):
        pass

    def dados_matricula(self, id_matricula):
        matricula = None
        for aluno in self.__alunos:
            for m in aluno.matriculas:
                if m.id_matricula == id_matricula:
                    matricula = m
                    break
            if matricula:
                break
        if matricula:
            self.__tela_aluno.mostrar_dados_matricula(matricula)
        else:
            self.__tela_aluno.mostrar_mensagem("Matrícula não encontrada.")

    def calcular_aluno_por_turno(self):
        pass

    def cancelar_matricula(self, id_matricula):
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
