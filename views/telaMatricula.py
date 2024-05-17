from controllers.matriculaController import ControladorMatricula
from controllers.controladorAluno import ControladorAluno
from models.plano import Plano

class TelaMatricula():
    def __init__(self):
        self.__controlador_matricula = ControladorMatricula()
        self.__controlador_aluno = ControladorAluno()
    
    def opcoes(self):
        print("OPÇÕES")
        print("1 - Mostrar mensalidade")
        print("2 - Alterar plano de matrícula")
        print("3 - Cancelar matrícula")
        print("4 - Renovar matrícula")    
        opcao = int(input("Escolha a opção: "))
        if opcao == "1":
            self.mostrar_mensalidade()
        elif opcao == "2":
            self.alterar_plano_matricula()
        elif opcao == "3":
            self.cancelar_matricula()
        else:
            print("Opção inválida!")
            self.mostra_opcoes()
    
    def alterar_plano(self):
        id_matricula = input("Insira o número da matrícula (id): ")
        novo_plano = input("Insira o novo plano desejado: ")
        self.__controlador_matricula.alterar_plano(id_matricula, novo_plano)
        print("Plano de matrícula alterado com sucesso!")
    
    def mostrar_mensalidade(self):
        id_matricula = input("Insira o número da matrícula (id): ")
        mensalidade = self.__controlador_matricula.calcular_mensalidade(id_matricula)
        print(f"A mensalidade da matrícula {id_matricula} é: R${mensalidade}")
    
    def cancelar_matricula(self):
        id_matricula = input("Insira o número da matrícula (id): ")
        self.__controlador_aluno.cancelar_matricula(id_matricula)
        print("Matrícula cancelada com sucesso!")
    
    def renovar_matricula(self):
        id_matricula = input("Insira o número da matrícula (id): ")
        self.__controlador_aluno.renovar_matricula(id_matricula)
        print("Matrícula renovada com sucesso!")
    
    def mostrar_mensagem(self, mensagem):
        print(mensagem)
