from controllers.controladorAluno import ControladorAluno
from models.plano import Plano


class TelaAluno():
    def __init__(self):
        self.__controlador_aluno = ControladorAluno()
        pass

    def mostrar_menu_inicial(self):
        print("-------- Aluno ----------")
        print("Escolha a opção:")
        print("1 - Alterar Turno")
        print("2 - Mostrar Treino Ficha")
        print("3 - Mostrar Matricula")
        print("5 - Cancelar Matricula")
        print("6 - Fazer matricula")
        print("0 - retornar")
        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            self.inserir_turno()
        elif opcao == 2:
            self.retirar_turno()
        elif opcao == 3:
            self.mostrar_treino_ficha()
        elif opcao == 4:
            nome = input("Digite o nome do aluno: ")
            self.mostrar_dados_matricula(nome)
        elif opcao == 5:
            nome = input("Digite o nome do aluno: ")
            self.cancelar_matricula(nome)
        elif opcao == 6:
            self.calcular_aluno_por_turno()
        elif opcao == 0:
            return
        else:
            print("Opção inválida. Tente novamente.")
            self.mostrar_menu_inicial()

    def mostrar_dados_matricula(self, nome):
        matricula = self.__controlador_aluno.buscar_matricula_por_nome(nome)
        if matricula is not None:
            print("-------- Dados da Matrícula ----------")
            print("Nome: ", matricula.nome)
            print("Plano: ", matricula.plano)
            print("Data de Início: ", matricula.data_inicio)
            print("Data de Término: ", matricula.data_termino)
            print("Valor: ", matricula.valor)
        else:
            print("Matrícula não encontrada.")

    
    def mostrar_treino_ficha(self, ficha):
        print("-------- Treinos da Ficha ----------")
        for treino in ficha:
            print("Exercício: ", treino.exercicio)
            print("Repetições: ", treino.repeticoes)
            print("------------------------------")
    
    def cancelar_matricula(self):
        nome = input("Digite o nome do aluno: ")
        self.__controlador_aluno.cancelar_matricula(nome)
        print("Matrícula cancelada com sucesso.")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
