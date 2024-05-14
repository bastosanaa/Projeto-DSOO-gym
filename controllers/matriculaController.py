'''
- controlador_aluno: ControladorAluno
-tela_matricula: TelaMatricula
-matriculas: []

+ definir_data_inicio()
+ definir_data_vencimento_pagamento()
+ definir_data_termino()
+ definir_mensalidade_de_acordo_com_plano()
+ calcula_plano_mais_vendido()
'''
from datetime import datetime, timedelta
from alunoController import ControladorAluno
from views.matriculaView import matriculaView
from models.matricula import Matricula
from models.plano import Plano

class ControladorMatricula():
    def __init__(self):
        self.__controlador_aluno = ControladorAluno()
        self.__tela_matricula = matriculaView()
        self.__matriculas = matriculas
        self.__planos = planos
        
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
        
        def mostrar_matricula(self, id_matricula):
            pass
        
        def definir_mensalidade_de_acordo_com_plano(self, plano: Plano):
            mensalidade = 0
            if plano == Plano.diamond:
                mensalidade += 200.00
            elif plano == Plano.gold:
                mensalidade += 150.00
            else:
                mensalidade += 100.00
            return mensalidade
        
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
