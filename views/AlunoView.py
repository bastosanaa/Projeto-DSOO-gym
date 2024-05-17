from controllers.alunoController import ControladorAluno
from models.plano import Plano


class AlunoView():
    def __init__(self):
        self.__controlador_aluno = ControladorAluno()
        pass

    def mostra_opcoes(self):
        print("-------- Aluno ----------")
        print("Escolha a opção:")
        print("1 - Escolher turno")
        print("2 - Alterar turno")
        print("3 - Fazer matricula")
        print("4 - Mostrar Matricula")
        print("5 - Cancelar Matricula")
        print("6 - Mostrar Treino Ficha")
        print("0 - retornar")
        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            self.escolher_turno()
        elif opcao == 2:
            self.alterar_turno()
        elif opcao == 3:
            self.realizar_matricula()
        elif opcao == 4:
            self.mostrar_dados_matricula()
        elif opcao == 5:
            self.cancelar_matricula()
        elif opcao == 6:
            self.mostrar_treino_ficha()
        elif opcao == 0:
            return
        else:
            print("Opção inválida. Tente novamente.")
            self.mostra_opcoes()

    def realizar_matricula(self):
        nome = input("Digite o nome do aluno: ")
        turno = self.escolher_turno()
        plano = self.escolher_plano()
        self.__controlador_aluno.realizar_matricula(nome, turno, plano)
        print("Matrícula realizada com sucesso.")
    
    def escolher_turno(self):
        print("Escolha o turno:")
        print("1 - Manhã")
        print("2 - Tarde")
        print("3 - Noite")
        turno = int(input("Escolha o turno: "))

    def escolher_plano(self):
        print("Escolha o plano:")
        print("1 - Diamond")
        print("2 - Gold")
        print("3 - Silver")
        plano = int(input("Escolha o plano: "))
        if plano == 1:
            return Plano.diamond
        elif plano == 2:
            return Plano.gold
        else:
            return Plano.silver

    def mostrar_dados_matricula(self):
        nome = input("Digite o nome do aluno: ")
        matricula = self.__controlador_aluno.buscar_matricula_por_nome(nome)
        if matricula is not None:
            print("-------- Dados da Matrícula ----------")
            print("ID: ", matricula.id_matricula)
            print("Nome: ", matricula.nome)
            print("Plano: ", matricula.plano)
            print("Data de Início: ", matricula.data_inicio)
            print("Data de Término: ", matricula.data_termino)
            print("Valor: ", matricula.valor)
        else:
            print("Matrícula não encontrada.")
    
    def alterar_turno(self):
        nome = input("Digite o nome do aluno: ")
        turno = self.escolher_turno()
        self.__controlador_aluno.alterar_turno(nome, turno)
        print("Turno alterado com sucesso.")

    def mostrar_treino_ficha(self, ficha):
        print("-------- Treinos da Ficha ----------")
        for treino in ficha:
            print("Exercício: ", treino.exercicio)
            print("Repetições: ", treino.repeticoes)
            print("------------------------------")
    
    def cancelar_matricula(self):
        id_matricula = input("Digite a id da matricula do aluno: ")
        self.__controlador_aluno.cancelar_matricula(id_matricula)
        print("Matrícula cancelada com sucesso.")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
