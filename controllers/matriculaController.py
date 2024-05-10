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
from models.plano import Plano
from alunoController import ControladorAluno


class ControladorMatricula():
    def __init__(self):
        self.__controlador_aluno = ControladorAluno()
        
        