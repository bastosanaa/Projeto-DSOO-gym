from models.aluno import Aluno
from views import AlunoView
from models.matricula import Matricula
from models.ficha import Ficha
import random
from controllers.matriculaController import ControladorMatricula

class ControladorAluno():
    def __init__(self):
        self.__tela_aluno = AlunoView()
        self.__controlador_aluno = ControladorAluno()
        self.__controlador_matricula = ControladorMatricula()
        self.__alunos = []
        self.__matriculas = []
    
    @property
    def matriculas(self):
        return self.__matriculas

    @property
    def alunos(self):
        return self.__alunos

    def realizar_matricula(self, nome, turno, plano):
        aluno_existente = None
        for aluno in self.__alunos:
            if aluno.nome == nome:
                aluno_existente = aluno
                break
        if aluno_existente:
            self.__tela_aluno.mostrar_mensagem("Aluno já está matriculado.")
        else:
            id_matricula = random.randint(1000, 9999)
            data_inicio = self.__controlador_matricula.definir_data_inicio()
            mensalidade = self.__controlador_matricula.definir_mensalidade_de_acordo_com_plano(plano)
            data_vencimento_pagamento = self.__controlador_matricula.definir_data_vencimento_pagamento(data_inicio)
            data_termino = self.__controlador_matricula.definir_data_termino(data_inicio)
            matricula = Matricula(id_matricula, nome, turno, plano, data_inicio, mensalidade, data_vencimento_pagamento, data_termino)
            self.__alunos.append(matricula)
            self.__controlador_matricula.matriculas.append(matricula)
            self.__tela_aluno.mostrar_mensagem("Matrícula realizada com sucesso.")

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
    
    def renovar_matricula(self, id_matricula):
        matricula = None
        for aluno in self.__alunos:
            for matri in aluno.matriculas:
                if matricula.id_matricula == id_matricula:
                    matricula = matri
                    break
        if matricula:
            matricula.data_inicio = self.__controlador_matricula.definir_data_inicio()
            matricula.data_vencimento_pagamento = self.__controlador_matricula.definir_data_vencimento_pagamento(matricula.data_inicio)
            matricula.data_termino = self.__controlador_matricula.definir_data_termino(matricula.data_inicio)
            self.__tela_aluno.mostrar_mensagem("Matrícula renovada com sucesso.")
        else:
            self.__tela_aluno.mostrar_mensagem("Matrícula não encontrada.")

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
            self.__tela_aluno.mostrar_dados_ficha(aluno_existente, ficha)
        else:
            self.__tela_aluno.mostrar_mensagem("Ficha não encontrada.")

    def retornar(self):
        self.__controlador_aluno.abre_tela()

