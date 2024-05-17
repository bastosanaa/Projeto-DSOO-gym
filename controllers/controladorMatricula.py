from datetime import datetime, timedelta
from controllers.controladorAluno import ControladorAluno
from views.telaMatricula import TelaMatricula
from models.plano import Plano
from models.matricula import Matricula
import random

class ControladorMatricula():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_aluno = ControladorAluno()
        self.__tela_matricula = TelaMatricula()
        self.__matriculas = []
        self.__planos = [Plano.Diamond, Plano.Gold, Plano.Silver]
        
    @property
    def planos(self):
        return self.__planos
    
    @property
    def matriculas(self):
        return self.__matriculas
    
    def definir_data_inicio(self, ano, mes, dia):
        data_inicio_matricula = datetime(ano, mes, dia)
    
    def definir_data_vencimento_pagamento(self, data_inicio_matricula):
        data_vencimento_matricula += data_inicio_matricula + timedelta(days=30)
    
    def definir_data_termino(self, data_inicio_matricula):
        data_termino_matricula += data_inicio_matricula + timedelta(days=365)

    def alterar_plano(self, id_matricula: int, novo_plano: Plano):
        for matricula in self.__matriculas:
            if matricula.id_matricula == id_matricula:
                matricula.plano = novo_plano
                break
    
    def realizar_matricula(self, nome, turno, plano):
        aluno_existente = None
        for matricula in self.__matriculas:
            if matricula.aluno.nome == nome:
                aluno_existente = matricula
                break
        if aluno_existente:
            self.__tela_matricula.mostrar_mensagem("Aluno já está matriculado.")
        else:
            id_matricula = random.randint(1000, 9999)
            data_inicio = self.definir_data_inicio()
            mensalidade = self.definir_mensalidade_de_acordo_com_plano(plano)
            data_vencimento_pagamento = self.definir_data_vencimento_pagamento(data_inicio)
            data_termino = self.definir_data_termino(data_inicio)
            matricula = Matricula(id_matricula, turno, plano, data_inicio, mensalidade, data_vencimento_pagamento, data_termino)
            self.__matriculas.append(matricula)
            self.__controlador_sistema.controlador_matricula.matriculas.append(matricula)
            self.__tela_matricula.mostrar_mensagem("Matrícula realizada com sucesso.")
    
    
    def definir_mensalidade_de_acordo_com_plano(self, plano: Plano):
        mensalidade = 0
        if plano == Plano.Diamond:
            mensalidade += 200.00
        elif plano == Plano.Gold:
            mensalidade += 150.00
        else:
            mensalidade += 100.00
        return mensalidade
    
    def cancelar_matricula(self, id_matricula):
        matricula = None
        for matricula in self.__matriculas:
            if matricula.id_matricula == id_matricula:
                matricula = matricula
                break
        if matricula:
            self.__matriculas.remove(matricula)
            self.__tela_matricula.mostrar_mensagem("Matrícula cancelada com sucesso.")
        else:
            self.__tela_matricula.mostrar_mensagem("Matrícula não encontrada")
    
    def renovar_matricula(self, id_matricula):
        matricula = None
        for matricula in self.__matriculas:
            if matricula.id_matricula == id_matricula:
                matricula = matricula
                break
        if matricula:
            matricula.data_inicio = self.__controlador_sistema.controlador_matricula.definir_data_inicio()
            matricula.data_vencimento_pagamento = self.__controlador_sistema.controlador_matricula.definir_data_vencimento_pagamento(matricula.data_inicio)
            matricula.data_termino = self.__controlador_sistema.controlador_matricula.definir_data_termino(matricula.data_inicio)
            self.__tela_matricula.mostrar_mensagem("Matrícula renovada com sucesso.")
        else:
            self.__tela_matricula.mostrar_mensagem("Matrícula não encontrada.")
        
    def calcula_plano_mais_vendido(self):
        plano_mais_vendido = ''
        quantidade_vendas = 0
        for plano in self.__planos:
            vendas_plano = 0
            for matricula in self.__matriculas:
                if matricula.plano == plano:
                    vendas_plano += 1
                if vendas_plano > quantidade_vendas:
                    quantidade_vendas = vendas_plano
                    plano_mais_vendido = plano
            return plano_mais_vendido

    def calcular_mesalidade(self, id_matricula):
        mensalidade = 0
        for matricula in self.__matriculas:
            if matricula.id_matricula == id_matricula:
                mensalidade = matricula.mensalidade
                break
        return mensalidade

