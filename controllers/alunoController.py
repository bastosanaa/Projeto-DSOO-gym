
from models.aluno import Aluno
from views import AlunoView
from models.matricula import Matricula
from models.ficha import Ficha

class ControladorAluno():
    def __init__(self):
        self.__tela_aluno = AlunoView()
        self.__controlador_aluno = ControladorAluno()
        self.__alunos = []
        self.__turnos = []
    
    @property
    def alunos(self):
        return self.__alunos

    @property
    def turnos(self):
        return self.__turnos
    
    def inserir_aluno_tuno(self, nome, turno):
        aluno_existente = None
        for aluno in self.__alunos:
            if aluno.nome == nome:
                aluno_existente = aluno
                break
        if aluno_existente:
            self.__tela_aluno.mostrar_mensagem("Aluno já está inserido em um turno.")
        else:
            novo_aluno = Aluno(nome, turno)
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
            self.__tela_aluno.mostrar_dados_matricula(matricula_encontrada)
        else:
            self.__tela_aluno.mostrar_mensagem("Matrícula não encontrada.")
        
    def retirar_turno(self, nome):
        aluno_existente = None
        for aluno in self.__alunos:
            if aluno.nome == nome:
                aluno_existente = aluno
                break
        if aluno_existente:
            self.__alunos.remove(aluno_existente)
            self.__tela_aluno.mostrar_mensagem("Aluno removido do turno com sucesso.")
        else:
            self.__tela_aluno.mostrar_mensagem("Aluno não encontrado.")
    

    def mostrar_treino_ficha(self, ficha: Ficha):
        aluno_existente = None
        for aluno in self.__alunos:
            for matricula in aluno.matriculas:
                if matricula.ficha == ficha:
                    aluno_existente = aluno
                    break
        if aluno_existente:
            self.__tela_aluno.mostrar_dados_ficha(aluno_existente, ficha)
        else:
            self.__tela_aluno.mostrar_mensagem("Ficha não encontrada.")
    

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
        

    def cancelar_matricula(self, id_matricula):
        matricula = None
        for aluno in self.__alunos:
            for matri in aluno.matriculas:
                if matricula.id_matricula == id_matricula:
                    matricula = matri
                    break
        if matricula:
            self.__alunos.remove(matricula)
            self.__tela_aluno.mostrar_mensagem("Matrícula cancelada com sucesso.")
        else:
            self.__tela_aluno.mostrar_mensagem("Matrícula não encontrada")

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
