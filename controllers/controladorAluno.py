from models.aluno import Aluno
from views.telaAluno import TelaAluno
from models.matricula import Matricula
from models.ficha import Ficha
# from controllers.controladorMatricula import ControladorMatricula

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()
        # self.__controlador_aluno = ControladorAluno()
        # self.__controlador_matricula = ControladorMatricula()
        self.__alunos = []
        self.__matriculas = []
    
    @property
    def matriculas(self):
        return self.__matriculas

    @property
    def alunos(self):
        return self.__alunos
    
    def mostrar_menu_inicial(self):
        self.__tela_aluno.mostrar_menu_inicial()


    def buscar_matricula_por_nome(self, nome):
        matricula_encontrada = None
        for aluno in self.__alunos:
            for matricula in aluno.matriculas:
                if matricula.aluno.nome == nome:
                    matricula_encontrada = matricula
                    break
        if matricula_encontrada:
            self.__tela_aluno.mostrar_dados_matricula(matricula_encontrada)
        else:
            self.__tela_aluno.mostrar_mensagem("Matrícula não encontrada.")

    def dados_matricula(self, id_matricula):
        matricula = None
        for aluno in self.__alunos:
            for m in aluno.matriculas:
                if m.id_matricula == id_matricula:
                    matricula = m
                    break
        if matricula:
            self.__tela_aluno.mostrar_dados_matricula(matricula)
        else:
            self.__tela_aluno.mostrar_mensagem("Matrícula não encontrada.")
    
    def alterar_turno(self, nome, turno):
        aluno_existente = None
        for aluno in self.__alunos:
            if aluno.nome == nome:
                aluno_existente = aluno
                break
        if aluno_existente:
            aluno_existente.turno = turno
            self.__tela_aluno.mostrar_mensagem("Turno alterado com sucesso.")
        else:
            self.__tela_aluno.mostrar_mensagem("Aluno não encontrado.")
    
    def calcular_aluno_por_turno(self):
        alunos_por_turno = {}
        for aluno in self.__alunos:
            turno = aluno.turno
            if turno in alunos_por_turno:
                alunos_por_turno[turno] += 1
            else:
                alunos_por_turno[turno] = 1
        
        for turno, quantidade in alunos_por_turno.items():
            print(f"Turno: {turno} - Quantidade de alunos: {quantidade}")

    def mostrar_treino_ficha(self, ficha: Ficha):
        aluno_existente = None
        for aluno in self.__alunos:
            for matricula in aluno.matriculas:
                if matricula.ficha == ficha:
                    aluno_existente = aluno
                    break
        if aluno_existente:
            self.__tela_aluno.mostrar_treino_ficha(aluno_existente.ficha)
        else:
            self.__tela_aluno.mostrar_mensagem("Ficha não encontrada.")
