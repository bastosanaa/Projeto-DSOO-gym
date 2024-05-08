from controllers.alunoController import ControladorAluno
from models.plano import Plano


class AlunoView():
    def __init__(self):
        self.__controlador_aluno = ControladorAluno()
        pass

    def mostra_opcoes(self):
        print("-------- Aluno ----------")
        print("Escolha a opção:")
        print("1 - Inserir Turno")
        print("2 - Retirar Turno")
        print("3 - Mostrar Treino Ficha")
        print("4 - Mostrar Matricula")
        print("5 - Cancelar Matricula")
        print("6 - Calcular Aluno Por Turno")
        print("0 - retornar")
        opçao = int(input("Escolha a opção: "))

        return opçao

    def mostrar_matricula(self, dados_matricula):
        print("ID da matrícula: ", dados_matricula["id_matricula"])
        if isinstance(plano, Plano):
            print("Plano: ", dados_matricula["plano"])
        print("Data de inicio: ", dados_matricula["data_inicio"])
        print("Data de termino: ", dados_matricula["data_termino"])
        print("Data de vencimento do pagamento: ",
              dados_matricula["data_vencimento_pagamento"])
        print("Mensalidade: ", dados_matricula["mensalidade"])
        print("\n")
